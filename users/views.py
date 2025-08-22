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
    

# ball qoshish userga
# status reject yoki accept reject berganda -1 ball 
# agar userni bali <= 0 bolsa foydalanuvchiga ban beradi