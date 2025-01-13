from rest_framework import serializers

from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    """
    Serializer para POST

    JSON:

        {
            "user": 3,
            "movie": 4,
            "content": "Me encanto la pelicula"
        }

    """
    
    class Meta:
        model = Review
        fields = '__all__'

class ReviewDetailSerializer(serializers.ModelSerializer):
    """
    Serializer para GET (Listar detalles)

    JSON Response:

    [
        {
            "id": 1,
            "user": "gilbe",
            "content": "La pelicula que todos los fans estabamos esperando.",
            "created_at": "2025-01-06T14:41:55.076252-06:00",
            "last_updated": "2025-01-06T14:41:55.076252-06:00",
            "movie": {
            "id": 2,
            "name": "Gato con botas: el último deseo",
            "year": 2022,
            "synopsis": "El Gato con Botas descubre que, debido a su pasión por la aventura, ha gastado ya 8 de sus 9 vidas. Por tanto, emprende un peligroso viaje en busca del legendario Último Deseo para solicitar que le restauren las vidas que ya perdió."
            }
        },
        {
            "id": 2,
            "user": "jhon",
            "content": "chida la pelicula esa",
            "created_at": "2025-01-06T14:56:04.680802-06:00",
            "last_updated": "2025-01-06T14:56:04.680802-06:00",
            "movie": {
            "id": 3,
            "name": "Shrek",
            "year": 2022,
            "synopsis": "Un ogro llamado Shrek vive en su pantano, pero su preciada soledad se ve súbitamente interrumpida por la invasión de los ruidosos personajes de los cuentos de hadas. Todos fueron expulsados de sus reinos por el malvado Lord Farquaad."
            }
        },
        {
            "id": 3,
            "user": "jhon",
            "content": "epaaaaaaaaaaaaaaaaaa",
            "created_at": "2025-01-07T11:17:26.865456-06:00",
            "last_updated": "2025-01-07T11:17:26.865456-06:00",
            "movie": {
            "id": 2,
            "name": "Gato con botas: el último deseo",
            "year": 2022,
            "synopsis": "El Gato con Botas descubre que, debido a su pasión por la aventura, ha gastado ya 8 de sus 9 vidas. Por tanto, emprende un peligroso viaje en busca del legendario Último Deseo para solicitar que le restauren las vidas que ya perdió."
            }
        },
        {
            "id": 4,
            "user": "Kate",
            "content": "Me encanto la pelicula",
            "created_at": "2025-01-07T12:17:00.462288-06:00",
            "last_updated": "2025-01-07T12:17:00.462288-06:00",
            "movie": {
            "id": 4,
            "name": "Red2222",
            "year": 2027,
            "synopsis": "Red es una películaaaa estadounidense de comedia, de aventuras y que trata a la pubertad de una manera metafórica, animada por computadora, dirigida por Domee Shi, producida por Pixar Animation Studios y lanzada por Walt Disney Pictures."
            }
        }
    ]

    JSON Response por ID:

        [
            {
                "id": 2,
                "user": "jhon",
                "content": "chida la pelicula esa",
                "created_at": "2025-01-06T14:56:04.680802-06:00",
                "last_updated": "2025-01-06T14:56:04.680802-06:00",
                "movie": {
                "id": 3,
                "name": "Shrek",
                "year": 2022,
                "synopsis": "Un ogro llamado Shrek vive en su pantano, pero su preciada soledad se ve súbitamente interrumpida por la invasión de los ruidosos personajes de los cuentos de hadas. Todos fueron expulsados de sus reinos por el malvado Lord Farquaad."
                }
            }
        ]
    """
        
    user = serializers.StringRelatedField()
    class Meta:
        model = Review
        fields = '__all__'
        # fields = ['id', 'content']
        # fields = ['id', 'user', 'movie', 'content']
        depth = 1
