from django.contrib import admin
from .models import Users, Posts, Comments 
# Register your models here.
admin.site.register(Users)
admin.site.register(Posts)
admin.site.register(Comments)

class UsersAdmin(admin.ModelAdmin):
    list_display = ("user_name", "email", "password", "created_at", "vote_count")
    
class PostsAdmin(admin.ModelAdmin):
    list_display = ("author", "title", "url", "body", "vote_count", "created_at")
    
class CommentsAdmin(admin.ModelAdmin):
    list_display = ("author", "body", "vote_count", "created_at", "post")