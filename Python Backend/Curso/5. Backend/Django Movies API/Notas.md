# Comandos

    mkdir django-movies
    cd django-movies

    python -m venv .venv
    .\.venv\Scripts\Activate

    pip install Django
    pip freeze > requirements.txt

    django-admin startproject core
    ls
    cd core

    python manage.py
    python manage.py runserver

    python manage.py migrate
    python manage.py makemigrations

    python manage.py createsuperuser
        gilbe
        gilbe@gmail.com
        admin

    python manage.py startapp movies
    python manage.py makemigrations
    python manage.py migrate

    pip install djangorestframework

    python manage.py makemigrations

# Simbologia de Errores de estatus

    https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
    https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

# Pruebas con Thunder Client

http://127.0.0.1:8000/api/movies/movie/

    {
        "name": "Shrek",
        "year": 2022,
        "synopsis": "Un ogro llamado Shrek vive en su pantano, pero su preciada soledad se ve súbitamente interrumpida por la invasión de los ruidosos personajes de los cuentos de hadas. Todos fueron expulsados de sus reinos por el malvado Lord Farquaad."
    }
