from django.db import models
from django.contrib.auth.models import AbstractUser

# from users.managers import BaseUserManager


class User(AbstractUser):
    """
    Custom user model that extends the default Django user model.
    You can add additional fields here if needed.
    """
    STATUS_CHOICES = [
        ("accept", "Accept"),
        ("reject", "Reject"),
        ("none","None"),
    ]
    ball = models.IntegerField(default=0)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="none"
    )
    ban = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        # faqat update bo‘lsa eski statusni tekshirish
        if self.pk:  
            old = User.objects.get(pk=self.pk)
            if old.status != self.status:
                if self.status == "accept":
                    self.ball += 1
                elif self.status == "reject":
                    self.ball -= 1
        else:
            # yangi user yaratilganda
            if self.status == "accept":
                self.ball = 1
            elif self.status == "reject":
                self.ball = -1

        # ban qo‘yish qismi
        if self.ball <= -1:
            self.ban = True
        else:
            self.ban = False

        super().save(*args, **kwargs)    

    def __str__(self):
        return str(self.username)


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