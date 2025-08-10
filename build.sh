#!/usr/bin/env bash
# exit on error
set -o errexit

# Upgrade pip first
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Run migrations
echo "Running database migrations..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

# Create default superuser if needed
echo "Creating default users..."
python manage.py create_default_superuser

echo "Build completed successfully!"
