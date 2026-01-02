#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Start Django server with Gunicorn
gunicorn inventory_management.wsgi:application --bind 0.0.0.0:$PORT
