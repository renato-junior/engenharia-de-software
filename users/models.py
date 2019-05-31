from django.db import models
from django.contrib.auth.models import User

class ForumUser(User):
    description = models.CharField(max_length=300)
    photo = models.ImageField(upload_to='images/', default='images/user.ico')