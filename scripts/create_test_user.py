#!/usr/bin/env python
"""
Script to create users for the Bible Research project.

This script can create both a guest user (for anonymous access) and a test user
(for development and testing purposes).

Usage:
    # Create both guest and test users
    python scripts/create_test_user.py
    
    # Create only guest user
    python scripts/create_test_user.py guest
    
    # Create only test user
    python scripts/create_test_user.py test
"""

import os
import sys
import django
from pathlib import Path

# Add the project root directory to the Python path
project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bible_research.settings')
django.setup()

# Import Django models
from django.contrib.auth import get_user_model
User = get_user_model()


def create_user(username, email, password, is_staff=False):
    """Create a user if it doesn't already exist.
    
    Args:
        username (str): Username for the user
        email (str): Email address for the user
        password (str): Password for the user
        is_staff (bool): Whether the user should have staff privileges
        
    Returns:
        User: The created or existing user object
    """
    # Check if user already exists
    if User.objects.filter(username=username).exists():
        print(f'User {username} already exists')
        user = User.objects.get(username=username)
    else:
        # Create new user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            is_staff=is_staff
        )
        print(f'Created new user: {username} (ID: {user.id})')
    
    return user


def create_guest_user():
    """Create a guest user for anonymous access.
    
    This user will be used when no authenticated user is available.
    
    Returns:
        User: The guest user object
    """
    return create_user(
        username='guest',
        email='guest@example.com',
        password='guest_password_123',  # This password won't be used for login
        is_staff=False
    )


def create_test_user():
    """Create a test user for development and testing.
    
    Returns:
        User: The test user object
    """
    return create_user(
        username='testuser',
        email='testuser@example.com',
        password='password123',
        is_staff=True
    )


def list_all_users():
    """List all users in the system."""
    print('\nAll users in the system:')
    for user in User.objects.all():
        print(f'Username: {user.username}, Email: {user.email}, ID: {user.id}, Staff: {user.is_staff}')


if __name__ == '__main__':
    # Check command line arguments
    if len(sys.argv) > 1:
        if sys.argv[1].lower() == 'guest':
            create_guest_user()
        elif sys.argv[1].lower() == 'test':
            create_test_user()
        else:
            print(f"Unknown user type: {sys.argv[1]}")
            print("Valid options are 'guest' or 'test'")
            sys.exit(1)
    else:
        # Create both users by default
        create_guest_user()
        create_test_user()
    
    # List all users
    list_all_users()
