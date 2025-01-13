from client import APIClient
from serializer import PostSerializer

client = APIClient("https://jsonplaceholder.typicode.com")

# response_create_post = client.create_post(title="Mi primer Post", body="Este es mi primer post en la API", user_id="1001")
# print(response_create_post)

response_user_posts = client.get_posts_by_user(user_id=5)
for post in response_user_posts:
    print(post)

# V1
# response = client.get_all_posts()

# print(response)

# serializer = PostSerializer()
# serializer_response = serializer(response)

# print(serializer_response)  
