from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.ViewAllCourses.as_view(), name='view_all_courses'),
    path('courses/<str:uuid>', views.ViewCourseDetail.as_view(), name='view_course_detail'),
    path('students/', views.ViewAllStudents.as_view(), name='view_all_students'),
    path('students/<str:uuid>', views.ViewStudentProfile.as_view(), name='view_student_profile'),
    path('students/<str:uuid>/enrollments', views.ViewEnrollmentByStudent.as_view(), name='view_enrollment_by_student')
]
