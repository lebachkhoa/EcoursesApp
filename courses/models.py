from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(upload_to="upload/avatar/%Y/%M")


class Base(models.Model):
    class Meta:
        abstract = True

    subject = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    actived = models.BooleanField(default=True)
    image = models.ImageField(upload_to="upload/courses/%Y/%M")

    def __str__(self):
        return self.subject
    


class Category(models.Model):
    category = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.category


class Course(Base):
    class Meta:
        unique_together = ("subject", "category")
    
    description = models.CharField(max_length=1000, null=True, blank= True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)


class Lesson(Base):
    content = models.TextField()
    course = models.ForeignKey(Course, models.SET_NULL, null=True)
    tag = models.ManyToManyField("Tag")



class Tag(models.Model):
    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.tag
    

    