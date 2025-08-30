- Add DBT client:
    - `cd bible/services`
```
export PATH="/opt/homebrew/opt/openjdk/bin:$PATH" && openapi-generator generate -i dbt_openapi.json -g python -o dbt_client --skip-validate-spec
```
- `db_backups/local_db_backup.sh`
  - Runs a local db backup
- Command `python manage.py import_esv_verses` on local machine took
    - For local SQLite: 0:02:52.066889
    - For remote free Aiven PostgreSQL: 0:46:01.924594

