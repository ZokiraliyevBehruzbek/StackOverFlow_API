from django.urls import path

from posts.views import CreatePost,ListPosts,MyPosts,CreateAnswer,CreateComment,LikeAnswers

urlpatterns = [
    # path("register/", register, name="hello_world"),
    path('me/', MyPosts.as_view(), name='my_posts'),
    path('create/',CreatePost.as_view(), name='create_posts'),
    path('list/', ListPosts.as_view(), name='posts_list'),
    path('answer/create', CreateAnswer.as_view(), name='create_answer'),
    path('coment/create', CreateComment.as_view(), name='create_coment'),
    path('answers/like', LikeAnswers.as_view(), name='liked'),
]
