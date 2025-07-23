#!/usr/bin/env python
"""
Script to create a test user for the Bible Research project.
Run this script with: python scripts/create_test_user.py
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


def create_test_user():
    """Create a test user if it doesn't already exist."""
    username = 'testuser'
    email = 'testuser@example.com'
    password = 'password123'

    # Check if user already exists
    if User.objects.filter(username=username).exists():
        print(f'User {username} already exists')
        user = User.objects.get(username=username)
    else:
        # Create new user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        print(f'Created new user: {username} (ID: {user.id})')

    # List all users
    print('\nAll users in the system:')
    for u in User.objects.all():
        print(f'Username: {u.username}, Email: {u.email}, ID: {u.id}')

    return user


if __name__ == '__main__':
    create_test_user()
