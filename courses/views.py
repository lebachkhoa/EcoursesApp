from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CourseSerializer, LessonSerializer, UserSerializer
from .models import Course, Lesson, User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CourserViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.filter(actived=True)
    serializer_class = CourseSerializer


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.filter(actived=True)
    serializer_class = LessonSerializer