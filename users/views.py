# from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework import status
# from rest_framework.decorators import api_view, permission_classes
# from drf_yasg.utils import swagger_auto_schema
# from drf_yasg import openapi
from rest_framework.generics import GenericAPIView,RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework.permissions import IsAuthenticated

from users.models import User
from users.serializers import UserSerializer


# Function based
""" Class based views
        Generic api view
        APIView
        Viewset
        ModelViewSet
        ListAPIView, CreateAPIView, ListCreateAPIView RetrieveAPIView, UpdateAPIView, DestroyAPIView
"""
class RegisterAPIView(GenericAPIView):
    serializer_class = UserSerializer


    def post(self, request, *args, **kwargs):
        user_data = self.get_serializer(data=request.data)
        user_data.is_valid(raise_exception=True)

        # Create user
        if user_data.validated_data.get("is_superuser", False):
            user = User.objects.create_superuser(**user_data.validated_data)
        else:
            user = User.objects.create_user(**user_data.validated_data)

        # Generate JWT tokens
        refresh = RefreshToken.for_user(user)
        tokens = {
            "access": str(refresh.access_token),
            "refresh": str(refresh),
        }

        return Response(
            data={"msg": "User registered successfully", "tokens": tokens},
            status=status.HTTP_200_OK,
        )


# @api_view(["GET"])
# @permission_classes([IsAuthenticated])
# def get_my_details(request):
#     user_details = request.user
#     user_serializer = UserSerializer(user_details).data
#     return Response(user_serializer)

class GetMyDetails(RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    
# class CreatePost(CreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializers
#     permission_classes = [IsAuthenticated]  # Faqat login bo‘lgan user qo‘sha oladi

#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)  # JWT token orqali userni avtomatik qo‘shadi
# class CreatePost(CreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = [IsAuthenticated]  # faqat login bo‘lgan user yaratadi

#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)  # owner avtomatik qo‘shiladi


# class ListPosts(ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = [IsAuthenticated]

# class MyPosts(ListAPIView):
#     serializer_class = PostSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         return Post.objects.filter(owner=self.request.user)
    
# # Ichida savol qosha olish kerak +
# # Savolga javob yoza olishi kerak  
# # har bir berilgan javob ichida comment ham bolishi kerak
# # savol bergan odam hohlagan javobini foydali deb topishi mumkin, checkbox bosib quyiladigan holatda