# from posts import PATH_TO_POST_IN_JP

class PostSerializer:

    def __init__(self):
        self.data = []

    def __call__(self, data):
        print("Serializando Posts")
        self.data = [obj.to_dict() for obj in data]

# print(PATH_TO_POST_IN_JP)