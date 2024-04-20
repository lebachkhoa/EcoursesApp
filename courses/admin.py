from django.contrib import admin
from .models import Category, Course, Lesson, Tag, User
from django.contrib.auth.admin import UserAdmin

class CourseInline(admin.TabularInline):
    model = Course
    extra = 0


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 0


class LessonTagInline(admin.TabularInline):
    model = Lesson.tag.through
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ("id", "category",)
    list_display_links = ("category",)
    inlines = (CourseInline,)


class CourseAdmin(admin.ModelAdmin):
    model = Course
    list_display = ("id", "subject", "actived", "image", "description", "category")
    list_display_links = ("subject",)
    inlines = (LessonInline,)


class LessonAdmin(admin.ModelAdmin):
    model = Lesson
    list_display = ("id", "subject", "actived", "image", "content", "course")
    list_display_links = ("subject",)
    inlines = (LessonTagInline,)


admin.site.register(User)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Tag)
