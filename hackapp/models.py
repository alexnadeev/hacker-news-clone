from django.db import models
from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=15)
    e-mail = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField
    upvote_count = models.IntegerField(default=0)
    