from django.contrib import admin
from .models import Course, Parent, StudentParent, Student, Enrollment

admin.site.register(Course)
admin.site.register(Parent)
admin.site.register(Student)
admin.site.register(StudentParent)
admin.site.register(Enrollment)
