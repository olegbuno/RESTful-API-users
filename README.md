# Restfull-API-users
Python + PostgreSQL Task

It creates RESTful API:
1. /users POST - create user with the next fields: first_name (required, only letters),
last_name (only letters), email (required, unique, correct format), phone (correct format),
password (hash)
2. /login POST - create API for user login by email and password. Use JWT authentication
3. /users/:id GET - get 1 user by id.
4. /users/:id PUT, DELETE - update/delete user, add validation.

To run project:

virtualenv env - create virtual environment

.\env\Scripts\activate - activate venv

pip install -r requirements.txt - install requirements

python manage.py makemigrations - create migrations

python manage.py migrate - run migrations

python manage.py createsuperuser - create admin

python manage.py runserver
