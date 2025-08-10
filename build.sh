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

# Run migrations
echo "Running database migrations..."
python manage.py makemigrations --noinput
echo "Applying migrations..."
python manage.py migrate --noinput

# Check if migrations were successful
echo "Verifying database structure..."
python manage.py showmigrations

# Create default superuser if needed
echo "Creating default users..."
python manage.py create_default_superuser

# Populate sample data
echo "Populating sample data..."
python manage.py populate_realistic_data

echo "Build completed successfully!"
