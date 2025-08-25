from django.contrib import admin
from .models import Post, Answer, Comment, Like

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1
    fields = ("content", "owner")  # faqat editable fieldlar
    readonly_fields = ("created_at",)  # faqat ko‘rsatish uchun
    show_change_link = True


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "created_at")
    inlines = [AnswerInline]

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ("post_id",  "content", "owner","created_at")

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id","answer_id",  "content","owner", "created_at")

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("post_id","answer_id","user","checkbox")
