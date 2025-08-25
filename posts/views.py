# from django.shortcuts import render
# from django.shortcuts import render

# Create your views here.
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.decorators import api_view, permission_classes
# from drf_yasg.utils import swagger_auto_schema
# from drf_yasg import openapi
from django.forms import ValidationError
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from posts.permissions import IsPostOwnerToLike
# from rest_framework_simplejwt.tokens import RefreshToken
from posts.models import Post,Answer,Comment,Like
from posts.serializers import PostSerializer, AnswerSerializers, CommentSerializers, LikeSerializer


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
    permission_classes = [IsAuthenticated, IsAdminUser]

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

# class LikeAnswers(CreateAPIView):
#     queryset = GetMyPostAnswers.objects.all()
#     serializer_class = MyPostSerializers
#     permission_classes = [IsAuthenticated, IsOwnerOfPostAnswer]

#     def perform_create(self, serializer):
#         answer = serializer.validated_data.get("answer_id")

#         # Avval like bosganmi yo‘qmi tekshirish
#         if GetMyPostAnswers.objects.filter(owner=self.request.user, answer_id=answer).exists():
#             raise ValidationError("Siz bu kommentga allaqachon like bosgansiz.")

#         # Agar hali bosmagan bo‘lsa, saqlaymiz
#         serializer.save(owner=self.request.user)
class LikeCreateAPIView(CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated, IsPostOwnerToLike]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# Ichida savol qosha olish kerak +
# Savolga javob yoza olishi kerak  +
# har bir berilgan javob ichida comment ham bolishi kerak +
# savol bergan odam hohlagan javobini foydali deb topishi mumkin, checkbox bosib quyiladigan holatda +