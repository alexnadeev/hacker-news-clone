from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

<<<<<<< HEAD
# class Users(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     # user_name = models.CharField(max_length=15)
#     # email = models.CharField(max_length=50)
#     # password = models.CharField(max_length=50)
#     # created_at = models.DateTimeField(auto_now_add=True)
#     # vote_count = models.IntegerField(default=0)

class Post(models.Model):
=======
"""
class Users(models.Model):
    user_name = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    vote_count = models.IntegerField(default=0)
"""

class Posts(models.Model):
>>>>>>> f09a9c5a0cfd5c02ef7cb70fbe2bb9a75fa4090e
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    url = models.CharField(max_length=50, default="null")
    body = models.TextField(max_length=5000)
    vote_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

<<<<<<< HEAD
class Comment(models.Model):
=======
class Comments(models.Model):
>>>>>>> f09a9c5a0cfd5c02ef7cb70fbe2bb9a75fa4090e
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=5000)
    vote_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Posts', on_delete=models.DO_NOTHING)
