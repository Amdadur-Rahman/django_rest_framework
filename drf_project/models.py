from django.db import models

# Create your models here.


class Course(models.Model):
    teacher_name = models.CharField(max_length=50)
    course_name = models.CharField(max_length=50)
    student = models.IntegerField(default=0)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']


    def __str__(self):
        return self.course_name