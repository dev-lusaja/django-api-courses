from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers.course import CourseSerializer
from ..controllers.course import CoursesController as controller


class ViewAllCourses(APIView):

    @staticmethod
    def get(*args, **kwargs):
        course = controller.get_all()
        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data)


class ViewCourseDetail(APIView):

    @staticmethod
    def get(*args, **kwargs):
        uuid = kwargs['uuid']
        course = controller.get_by_id(uuid)
        serializer = CourseSerializer(course)
        return Response(serializer.data)
