# Comandos

    pip install virtualenv
    python -m venv .venv
    .\.venv\Scripts\Activate

    pip install Django
    pip install djangorestframework
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
