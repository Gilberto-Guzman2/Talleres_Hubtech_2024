from .models import Comment
import requests


class CommentService:
    def __init__(self, json_placeholder_adapter):
        self.json_place_holder_service = json_placeholder_adapter

    def get_all_comments(self):
        try:
            response_json = self.json_place_holder_service.get_all_comments()
            return [Comment.from_dict(comment) for comment in response_json]
        except requests.exceptions.RequestException as e:
            print(f"Error al obtener las publicaciones: {e}")
            return []
    

    def create_comment(self, post_id, name, email, body):
        try:
            response = self.json_place_holder_service.create_comment(post_id, name, email, body)
            return Comment.from_dict(response)
        except requests.exceptions.RequestException as e:
            print(f"Error al crear el comentario: {e}")
            return None

    def get_all_comments_by_post(self, post_id):
        try:
            response_json = self.json_place_holder_service.get_all_comments_by_post(post_id)
            return [Comment.from_dict(comment) for comment in response_json]
        except requests.exceptions.RequestException as e:
            print(f"Error al obtener las publicaciones del usuario {post_id}: {e}")
            return None