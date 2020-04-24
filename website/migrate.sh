#!/bin/bash
python manage.py migrate
python manage.py makemigrations Database
python manage.py migrate Database