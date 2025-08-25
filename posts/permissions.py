from rest_framework import permissions
from .models import Post, Answer

class IsPostOwnerToLike(permissions.BasePermission):
    """
    Faqatgina post egasiga o'z postidagi answerlarga like qo'yishga ruxsat beradi
    """

    def has_permission(self, request, view):
        # Faqat authenticated userlar uchun
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        post_id = request.data.get("post_id")
        answer_id = request.data.get("answer_id")

        if not post_id or not answer_id:
            return False

        try:
            post = Post.objects.get(id=post_id)
            answer = Answer.objects.get(id=answer_id)
        except (Post.DoesNotExist, Answer.DoesNotExist):
            return False

        # Faqat post egasi like bosishi mumkin
        return post.owner == request.user
