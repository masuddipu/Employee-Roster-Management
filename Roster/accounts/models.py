from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_emp = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)

    phone = models.CharField(max_length=50)
    location = models.CharField(max_length=264)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.username
