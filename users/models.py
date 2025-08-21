from django.db import models
from django.contrib.auth.models import AbstractUser

# from users.managers import BaseUserManager


class User(AbstractUser):
    """
    Custom user model that extends the default Django user model.
    You can add additional fields here if needed.
    """

    def __str__(self):
        return self.title

    class Meta:
        db_table = "users"


# class Post(models.Model):
#     """
#     Model representing a movie.
#     """
#     title = models.CharField(max_length=255)
#     content = models.TextField(max_length=255)
#     owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
#     created_at = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return self.title

#     class Meta:
#         db_table = "posts"