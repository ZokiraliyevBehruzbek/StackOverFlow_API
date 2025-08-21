from django.urls import path

from users.views import RegisterAPIView, GetMyDetails

urlpatterns = [
    # path("register/", register, name="hello_world"),
    path("me/", GetMyDetails.as_view(), name='get me'),
    path('register/', RegisterAPIView.as_view(), name='register_post'),  # POST uchun
    # path('posts/create/',CreatePost.as_view(), name='create_posts'),
    # path('posts/list', ListPosts.as_view(), name='posts_list'),
    # path('posts/myposts', MyPosts.as_view(), name='my_posts'),
]
