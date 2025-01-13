# Comandos

    pip install virtualenv
    python -m venv .venv
    .\.venv\Scripts\Activate

    pip install Django
    pip freeze > requirements.txt

    py -m django --version
    django-admin startproject core

    python manage.py runserver
    python manage.py startapp movies
    python manage.py migrate

    python manage.py createsuperuser
        example
        example@gmail.com
        examplepassword

# Extra

    Get-NetTCPConnection -State Listen
