from client import APIClient

client = APIClient("https://jsonplaceholder.typicode.com")

response = client.get_all_posts()
# print(response)

posts_json_uno = response[0]
print(posts_json_uno.to_dict())