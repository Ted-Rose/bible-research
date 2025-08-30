#!/bin/bash

# This script backs up a PostgreSQL database using pg_dump.
# It reads database connection details from a config.yaml file.

# --- Configuration ---
CONFIG_FILE="config.yaml"
BACKUP_DIR="db_backups" # Directory to store backups
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="${BACKUP_DIR}/backup_${TIMESTAMP}.dump"

# --- Create backup directory if it doesn't exist ---
mkdir -p "$BACKUP_DIR"

# --- Extract database credentials from config.yaml ---
# We use grep and sed to parse the YAML file.
# Note: This is a basic YAML parser and assumes the structure from config_template.yaml
# with database credentials under DATABASES > default

echo "Reading database configuration from $CONFIG_FILE..."

# Extract values with more robust parsing
DB_ENGINE=$(grep -A15 'default:' "$CONFIG_FILE" | grep -E '\s*ENGINE:' | head -1 | sed 's/.*ENGINE:\s*\([^#]*\).*/\1/' | tr -d ' ')
DB_NAME=$(grep -A15 'default:' "$CONFIG_FILE" | grep -E '\s*NAME:' | head -1 | sed 's/.*NAME:\s*\([^#]*\).*/\1/' | tr -d ' ' | sed "s/'//g")
DB_USER=$(grep -A15 'default:' "$CONFIG_FILE" | grep -E '\s*USER:' | head -1 | sed 's/.*USER:\s*\([^#]*\).*/\1/' | tr -d ' ')
DB_PASSWORD=$(grep -A15 'default:' "$CONFIG_FILE" | grep -E '\s*PASSWORD:' | head -1 | sed 's/.*PASSWORD:\s*\([^#]*\).*/\1/' | tr -d ' ' | sed "s/'//g")
DB_HOST=$(grep -A15 'default:' "$CONFIG_FILE" | grep -E '\s*HOST:' | head -1 | sed 's/.*HOST:\s*\([^#]*\).*/\1/' | tr -d ' ')
DB_PORT=$(grep -A15 'default:' "$CONFIG_FILE" | grep -E '\s*PORT:' | head -1 | sed 's/.*PORT:\s*\([^#]*\).*/\1/' | tr -d ' ')

# Check for SSL options if they exist
if grep -q 'OPTIONS:' "$CONFIG_FILE"; then
    DB_SSLMODE=$(grep -A10 'OPTIONS:' "$CONFIG_FILE" | grep -E '\s*sslmode:' | head -1 | sed 's/.*sslmode:\s*\([^#]*\).*/\1/' | tr -d ' ')
    DB_SSLROOTCERT=$(grep -A10 'OPTIONS:' "$CONFIG_FILE" | grep -E '\s*sslrootcert:' | head -1 | sed 's/.*sslrootcert:\s*\([^#]*\).*/\1/' | tr -d ' ' | sed "s/'//g" | sed 's/"//g')
fi

# Debug output
echo "Extracted values:"
echo "ENGINE: $DB_ENGINE"
echo "NAME: $DB_NAME"
echo "USER: $DB_USER"
echo "HOST: $DB_HOST"
echo "PORT: $DB_PORT"

# SSL options are handled differently in pg_dump
# We'll use PGSSLMODE and PGSSLROOTCERT environment variables instead
if [ ! -z "$DB_SSLMODE" ]; then
    export PGSSLMODE="$DB_SSLMODE"
    echo "Setting SSL mode: $DB_SSLMODE"
fi

if [ ! -z "$DB_SSLROOTCERT" ]; then
    export PGSSLROOTCERT="$DB_SSLROOTCERT"
    echo "Setting SSL root cert: $DB_SSLROOTCERT"
fi

# --- Validate extracted information ---
if [ -z "$DB_NAME" ] || [ -z "$DB_USER" ] || [ -z "$DB_PASSWORD" ] || [ -z "$DB_HOST" ] || [ -z "$DB_PORT" ]; then
    echo "Error: Could not extract all database credentials from $CONFIG_FILE. Please check the file format."
    exit 1
fi

# --- Set environment variable for pg_dump to use password ---
# This is crucial for non-interactive password entry.
export PGPASSWORD="$DB_PASSWORD"

echo "Starting database backup for '$DB_NAME' on '$DB_HOST:$DB_PORT'..."
echo "Backup will be saved to: $BACKUP_FILE"

# --- Check pg_dump version compatibility ---
PG_DUMP_VERSION=$(pg_dump --version | grep -oE '[0-9]+\.[0-9]+' | head -1)
echo "Local pg_dump version: $PG_DUMP_VERSION"

# Try to get server version
echo "Checking PostgreSQL server version..."
SERVER_VERSION=$(PGPASSWORD="$DB_PASSWORD" psql -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER" -d "$DB_NAME" -t -c "SELECT version();" 2>/dev/null | grep -oE '[0-9]+\.[0-9]+' | head -1)

if [ ! -z "$SERVER_VERSION" ]; then
    echo "PostgreSQL server version: $SERVER_VERSION"
    
    # Compare major versions
    PG_DUMP_MAJOR=$(echo "$PG_DUMP_VERSION" | cut -d. -f1)
    SERVER_MAJOR=$(echo "$SERVER_VERSION" | cut -d. -f1)
    
    if [ "$PG_DUMP_MAJOR" != "$SERVER_MAJOR" ]; then
        echo "⚠️ WARNING: Version mismatch detected! Server is $SERVER_VERSION but pg_dump is $PG_DUMP_VERSION"
        echo "This may cause compatibility issues. Consider upgrading pg_dump:"
        echo "  brew upgrade postgresql@$SERVER_MAJOR"
        echo "  brew link --force postgresql@$SERVER_MAJOR"
        
        read -p "Do you want to continue anyway? (y/N): " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            echo "Backup aborted by user."
            exit 1
        fi
    fi
else
    echo "Could not determine server version. Proceeding with backup anyway."
fi

# --- Perform the pg_dump ---
# Using the custom format (-Fc) is recommended for flexibility with pg_restore.
# The SSL options are passed directly to pg_dump.
pg_dump \
    -h "$DB_HOST" \
    -p "$DB_PORT" \
    -U "$DB_USER" \
    -d "$DB_NAME" \
    -F c \
    --no-owner \
    --no-privileges \
    --verbose \
    --create \
    --clean \
    --if-exists \
    --compress=9 \
    --file="$BACKUP_FILE"

# Clear the password and SSL settings from environment variables for security
unset PGPASSWORD
unset PGSSLMODE
unset PGSSLROOTCERT

# --- Check if pg_dump was successful ---
PG_DUMP_STATUS=$?
if [ $PG_DUMP_STATUS -eq 0 ]; then
    if [ -f "$BACKUP_FILE" ] && [ -s "$BACKUP_FILE" ]; then
        echo "Database backup completed successfully! 🎉"
        echo "Backup file size: $(du -h "$BACKUP_FILE" | awk '{print $1}')"
    else
        echo "Error: Backup file was not created or is empty."
        exit 1
    fi
else
    echo "Error: Database backup failed with exit code $PG_DUMP_STATUS! ❌"
    
    # Provide guidance based on common error codes
    if [ $PG_DUMP_STATUS -eq 1 ]; then
        echo "This may be due to a version mismatch between pg_dump and the PostgreSQL server."
        echo "Your server is likely running PostgreSQL 16.x but your pg_dump is version 14.x."
        echo "To fix this, you can upgrade your local PostgreSQL client tools:"
        echo "  brew install postgresql@16"
        echo "  brew link --force postgresql@16"
    elif [ $PG_DUMP_STATUS -eq 2 ]; then
        echo "This may be due to invalid command line arguments."
    elif [ $PG_DUMP_STATUS -eq 3 ]; then
        echo "This may be due to a connection issue. Check your network and credentials."
    fi
    
    exit 1
fi

exit 0
