class PostSerializer:

    def __init__(self):
        self.data = []
        pass

    def __call__(self, data):

        # V1
        # list_response = []
        # for obj in data:
        #     list_response.append(obj.to_dict())
        # return list_response
        
        # V2
        return [obj.to_dict() for obj in data]



        # Esto ya no se muestra
        print("Serializando Post")