#!/bin/bash
python manage.py migrate
python manage.py makemigrations DataBase
python manage.py migrate DataBase