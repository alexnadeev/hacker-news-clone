from django.contrib import admin
<<<<<<< HEAD
from . models import Post, Comment

#admin.site.register(Users)
admin.site.register(Post)
admin.site.register(Comment)


=======
from .models import Posts, Comments 
>>>>>>> f09a9c5a0cfd5c02ef7cb70fbe2bb9a75fa4090e
# Register your models here.
#admin.site.register(Users)
admin.site.register(Posts)
admin.site.register(Comments)

  
class PostsAdmin(admin.ModelAdmin):
    list_display = ("author", "title", "url", "body", "vote_count", "created_at")
    
class CommentsAdmin(admin.ModelAdmin):
    list_display = ("author", "body", "vote_count", "created_at", "post")