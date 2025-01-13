class Post:
    def __init__(self, post_id, title, body, user_id):
        self.post_id =post_id
        self.title = title
        self.body = body
        self.user_id = user_id

    @classmethod
    def from_dict(cls, data):
        return cls(
            post_id = data.get("id"),
            title = data.get("title"),
            body = data.get("body"),
            user_id = data.get("userId")
        )
    
    def to_dict(self):
        return {
            "id": self.post_id,
            "title": self.title,
            "body": self.body,
            "userId": self.user_id
        }

    # Métodos magicos
    def __str__(self):
        return f"Post(ID: {self.post_id}, Title: {self.title}, Body: {self.body}, UserID: {self.user_id})"

posts_data = [
      {
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
  },
  {
    "userId": 1,
    "id": 2,
    "title": "qui est esse",
    "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"
  },
  {
    "userId": 1,
    "id": 3,
    "title": "ea molestias quasi exercitationem repellat qui ipsa sit aut",
    "body": "et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et velit aut"
  }
]
