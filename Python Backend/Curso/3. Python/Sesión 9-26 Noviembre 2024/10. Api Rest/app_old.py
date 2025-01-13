import requests

try:
    # url = "https://jsonplaceholder.typicode.com/posts"
    url = "https://jsonplaceholder.typicode.com/postsloop"

    response = requests.get(url)
    print(response.status_code)

    response_json = response.json()
    print(response_json[0]["title"])  
        # print(response_json)
except KeyError as e:
    print(f"Hubo u problema: {e}")
# except Exception as e:
#     print(f"Hubo u problema: {e}")

