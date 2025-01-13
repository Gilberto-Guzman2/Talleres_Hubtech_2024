import requests

class JSONPlaceHolderAdapter:
    def __init__(self):
        self.base_url = "https://jsonplaceholder.typicode.com"

    def get_all_posts(self, ruta):
        try:
            response = requests.get(f"{self.base_url}/{ruta}")
            response_json = response.json()
            return response_json
        except requests.exceptions.RequestException as e:
            print(f"Error al obtener las publicaciones: {e}")
            return []
        
    def get_posts_by_user(self, user_id):
        try:
            response = requests.get(f"{self.base_url}/posts", params={"userId": user_id})
            response_json = response.json()
            return response_json
        except requests.exceptions.RequestException as e:
            print(f"Error al obtener las publicaciones del usuario {user_id}: {e}")
            return None

    def create_post(self, title, body, user_id):
        try:
            payload = {
                "title": title,
                "body": body,
                "userId": user_id
            }
            response = requests.post(f"{self.base_url}/posts", json=payload)
            response_json = response.json()
            return response_json
        
        except requests.exceptions.RequestException as e:
            print(f"Error al crear la publicación: {e}")
            return None
    
    def get_all_comments(self):
        try:
            response = requests.get(f"{self.base_url}/comments")
            response_json = response.json()
            return response_json
        except requests.exceptions.RequestException as e:
            print(f"Error al obtener las publicaciones: {e}")
            return []

    def get_all_comments_by_post(self, post_id):
        try:
            response = requests.get(f"{self.base_url}/comments", params={"postId": post_id})
            response_json = response.json()
            return response_json
        except requests.exceptions.RequestException as e:
            print(f"Error al obtener las publicaciones del usuario {post_id}: {e}")
            return None

    def create_comment(self, post_id, name, email, body):
        try:
            payload = {
                "postId": post_id,
                "name": name,
                "email": email,
                "body": body
            }
            response = requests.post(f"{self.base_url}/comments", json=payload)
            response_json = response.json()
            return response_json
        
        except requests.exceptions.RequestException as e:
            print(f"Error al crear la publicación: {e}")
            return None

    