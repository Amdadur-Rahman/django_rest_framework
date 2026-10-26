from django.urls import path
from .import views


urlpatterns = [
    path('data/',views.course_list, name='course_list'),
    path('data/<int:id>/',views.course_detail, name='course_detail'),
    path('create/',views.create_course, name='create'),

]
