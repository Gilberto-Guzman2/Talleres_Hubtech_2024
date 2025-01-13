from posts import PATH_TO_POST_IN_JP, PostSerializer
from posts.services import PostService
from json_placeholder import JSONPlaceHolderAdapter
from comments.services import CommentService
from comments.serializers import CommentSerializer

json_placeholder_adapter = JSONPlaceHolderAdapter()
post_service = PostService(json_placeholder_adapter)
comments_service = CommentService(json_placeholder_adapter)



# get_posts = post_service.get_all_posts()
# get_posts_serializer = PostSerializer()
# get_posts_serializer(get_posts)
# print(get_posts_serializer.data)

# response_user_posts = post_service.get_posts_by_user(user_id=5)
# for post in response_user_posts:
#     print(post)

# response_create_post = post_service.create_post(title="Mi primer Post", body="Este es mi primer post en la API", user_id="1001")
# print(response_create_post)




# comments = comments_service.get_all_comments()
# comment_serializer = CommentSerializer()
# comment_serializer(comments)
# print(comment_serializer.data)

response_comment_posts = comments_service.get_all_comments_by_post(post_id=5)
for post in response_comment_posts:
    print(post)

# response_create_comment = comments_service.create_comment(post_id ="1" , name ="Este es mi primer comentario", email ="example@gmail.com", body="Este es mi primer comentario en la API")
# print(response_create_comment)













# response = post_service.get_all_posts()
# response = post_service.get_all_posts(ruta = PATH_TO_POST_IN_JP)
# serializer = PostSerializer()
# serializer(response)
# print(PATH_TO_POST_IN_JP)
# print(serializer.data)