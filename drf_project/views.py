from django.shortcuts import render, get_object_or_404
from .models import Course
from .serializers import CourseSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Create your views here.

def course_list(request):
    all_course = Course.objects.all()
    serializer = CourseSerializer(all_course, many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse (json_data, content_type = 'application/json')


def course_detail(request, id):
    course = get_object_or_404(Course, id=id)
    serializer = CourseSerializer(course)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse (json_data, content_type = 'application/json')

