from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourserViewSet, LessonViewSet, UserViewSet

router = DefaultRouter()
router.register("api/courses", CourserViewSet)
router.register("api/lessons", LessonViewSet)
router.register("api/users", UserViewSet)

urlpatterns = [
    path("",include(router.urls)),
]
