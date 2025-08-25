
from django.db import models
from django.utils import timezone
from users.models import User

class Post(models.Model):
    """
    Model representing a movie.
    """
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

    class Meta:
        db_table = "posts"

class Answer(models.Model):
    post_id = models.ForeignKey(Post,on_delete=models.CASCADE, related_name="post_id")
    content = models.TextField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post_answers")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
    
    class Meta:
        db_table = "answers"
    
class Comment(models.Model):
    answer_id = models.ForeignKey(Answer,on_delete=models.CASCADE,related_name="answer_id")
    content = models.TextField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post_comment")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    class Meta:
        db_table = "coments"

# class GetMyPostAnswers(models.Model):
#     answer_id = models.ForeignKey(Answer,on_delete=models.CASCADE,related_name="answers_id")
#     checkbox = models.BooleanField(default=False, null=False)

#     def __str__(self):
#         return self.answer_id
    
#     class Meta:
#         db_table = "like"

class GetMyPostAnswers(models.Model):
    # post_id = models.ForeignKey(Post,on_delete=models.CASCADE, related_name="posts_id")
    answer_id = models.ForeignKey(
        Answer,
        on_delete=models.CASCADE,
        related_name="answers_id"
    )
    checkbox = models.BooleanField(default=False)
    owner = models.ForeignKey(
        User,  # sening user modelinga qarab to‘g‘rila
        on_delete=models.CASCADE,
        related_name="answer_likes"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.answer_id} -> {self.checkbox}"

    class Meta:
        db_table = "likes"