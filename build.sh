#!/usr/bin/env bash
# exit on error
set -o errexit

# Upgrade pip first
echo "Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --no-input

# Initialize database with comprehensive setup
echo "Initializing database with all required data..."
python manage.py initialize_database --force

echo "Build completed successfully!"
