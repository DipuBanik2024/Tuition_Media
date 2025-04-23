from django.contrib import admin
from .models import Course
# Register your models here.



@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'course_type', 'teacher', 'created_at']
    search_fields = ['title', 'teacher__username']
    list_filter = ['course_type', 'created_at']
