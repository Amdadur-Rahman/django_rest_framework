from django.contrib import admin
from . models import Course

# Register your models here.

@admin.register(Course)
class CourceAdmin(admin.ModelAdmin):
    list_display = ['course_name','teacher_name','student','price','created']
