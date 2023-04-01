from django.db import models

from . import Student
from ..models.course import Course


class Enrollment(models.Model):
    id = models.UUIDField(primary_key=True)
    course = models.ForeignKey(Course, related_name='students', on_delete=models.CASCADE)
    student = models.ForeignKey(Student, related_name='enrollments', on_delete=models.CASCADE)

    def __str__(self):
        return self.id.__str__()
