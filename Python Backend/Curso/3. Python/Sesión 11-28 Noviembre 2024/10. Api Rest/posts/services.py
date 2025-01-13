from posts import Post
import requests
from posts import PATH_TO_POST_IN_JP

class PostService:
    def __init__(self, json_placeholder_adapter):
        self.json_place_holder_service = json_placeholder_adapter

    # def get_all_posts(self, ruta):
    #     try:
    #         response = requests.get(f"{self.base_url}/{ruta}")
    #         response_json = response.json()
    #         return [Post.from_dict(post) for post in response_json]
    #     except requests.exceptions.RequestException as e:
    #         print(f"Error al obtener las publicaciones: {e}")
    #         return []

    def get_all_posts(self):
        try:
            response_json = self.json_place_holder_service.get_all_posts(ruta = PATH_TO_POST_IN_JP)
            return [Post.from_dict(post) for post in response_json]
        except requests.exceptions.RequestException as e:
            print(f"Error al obtener las publicaciones: {e}")
            return []
        
    # Tarea
    def get_posts_by_user(self, user_id):
        try:
            response_json = self.json_place_holder_service.get_posts_by_user(user_id)
            return [Post.from_dict(post) for post in response_json]
        except requests.exceptions.RequestException as e:
            print(f"Error al obtener las publicaciones del usuario {user_id}: {e}")
            return None
        
    def create_post(self, title, body, user_id):
        try:
            response = self.json_place_holder_service.create_post(title, body, user_id)
            return Post.from_dict(response)
        
        except requests.exceptions.RequestException as e:
            print(f"Error al crear la publicación: {e}")
            return None