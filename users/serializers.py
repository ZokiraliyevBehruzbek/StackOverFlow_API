from rest_framework import serializers
# from django.db import models

from users.models import User


# class Role(models.TextChoices):
#     Admin = "Admin", "Admin"
#     Teacher = "Teacher", "Teacher"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "password",
            "is_superuser",
        ]


# class PostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = ["id", "title", "content", "owner", "created_at"]
#         read_only_fields = ["id", "owner", "created_at"]  # owner foydalanuvchidan kirmaydi