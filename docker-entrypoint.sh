#!/bin/bash

echo "Applying migrations..."
poetry run python manage.py migrate

echo "Collecting static files..."
poetry run python manage.py collectstatic --no-input

echo "Starting server..."
poetry run python manage.py runserver 0.0.0.0:8000

