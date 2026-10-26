from rest_framework import serializers
from .models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['teacher_name','course_name','student','description','price','created']

    def create(self, validate_data):
        return Course.objects.create(**validate_data)