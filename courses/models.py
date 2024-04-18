from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(upload_to="upload/%Y/%M")



class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)


