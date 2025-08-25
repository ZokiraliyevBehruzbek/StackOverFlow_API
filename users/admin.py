from django.contrib import admin

# Register your models here.
from users.models import User
from posts.models import Post


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "ball", "ban", "is_active")
    search_fields = ('email', 'first_name', 'last_name')
    
    


