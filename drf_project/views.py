from django.shortcuts import render, get_object_or_404
from .models import Course
from .serializers import CourseSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
import io
from rest_framework.parsers import JSONParser

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

def create_course(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        sirializer = CourseSerializer(data=python_data)
        if sirializer.is_valid:
            sirializer.save()
            message = {'msg':'succesfully create your course'}
            json_data = JSONRenderer().render(message)
            return HttpResponse (json_data, content_type = 'application/json')
        json_data = JSONRenderer().render(sirializer.errors)
        return HttpResponse (json_data, content_type = 'application/json')

        

