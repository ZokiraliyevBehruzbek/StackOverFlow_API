from rest_framework import serializers
# from django.db import models

from posts.models import Post,Answer,Comment,Like


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "title", "content", "owner", "created_at"]
        read_only_fields = ["id", "owner", "created_at"]  # owner foydalanuvchidan kirmaydi


class AnswerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ["id", "post_id", "content", "owner", "created_at"]
        read_only_fields = ["id", "owner","created_at"]

class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "answer_id","content", "owner", "created_at"]
        read_only_fields = ["id", "owner","created_at"]

# class MyPostSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = GetMyPostAnswers
#         fields= ["id","post_id", "answer_id", "checkbox", "owner", "created_at"]
#         read_only_fields = ["id", "owner","created_at"]
    
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ["post_id", "answer_id", "checkbox"]

    def validate(self, attrs):
        post_id = attrs["post_id"]
        answer_id = attrs["answer_id"]

        # Javob shu postga tegishliligini tekshirish
        if answer_id.post_id != post_id:
            raise serializers.ValidationError("Answer bu postga tegishli emas.")

        return attrs
