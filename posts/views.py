# from django.shortcuts import render
# from django.shortcuts import render

# Create your views here.
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.decorators import api_view, permission_classes
# from drf_yasg.utils import swagger_auto_schema
# from drf_yasg import openapi
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
# from rest_framework_simplejwt.tokens import RefreshToken
from posts.models import Post,Answer,Comment,GetMyPostAnswers
from posts.serializers import PostSerializer, AnswerSerializers, CommentSerializers, MyPostSerializers


# Create your views here.
class CreatePost(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]  # faqat login bo‘lgan user yaratadi

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)  # owner avtomatik qo‘shiladi

class ListPosts(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

class MyPosts(ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Post.objects.filter(owner=self.request.user)
    

class CreateAnswer(CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializers
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CreateComment(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class LikeAnswers(CreateAPIView):
    queryset = GetMyPostAnswers.objects.all()
    serializer_class = MyPostSerializers
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# Ichida savol qosha olish kerak +
# Savolga javob yoza olishi kerak  +
# har bir berilgan javob ichida comment ham bolishi kerak +
# savol bergan odam hohlagan javobini foydali deb topishi mumkin, checkbox bosib quyiladigan holatda +