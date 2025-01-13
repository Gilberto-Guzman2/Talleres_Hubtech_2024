# Comandos

    pip install virtualenv
    python -m venv .venv
    .\.venv\Scripts\Activate

    pip install Django
    pip install djangorestframework
    pip install Pillow
    pip freeze > requeriments.txt

    django-admin startproject core
    cd core
    python manage.py runserver
    python manage.py makemigrations
    python manage.py migrate

    python manage.py createsuperuser
        example@gmail.com
        example
        examplepassword

    python manage.py startapp authentication

    python manage.py makemigrations
    python manage.py migrate

    python manage.py migrate

    python manage.py startapp products

    python manage.py startapp cart
    python manage.py startapp orders
    python manage.py startapp feedback
    python manage.py startapp sellers

    python manage.py makemigrations
    python manage.py migrate

    python manage.py makemigrations
    python manage.py migrate

    python manage.py runserver
