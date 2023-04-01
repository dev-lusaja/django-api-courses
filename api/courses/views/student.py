from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers.student import StudentSerializer
from ..controllers.student import StudentController as controller


class ViewAllStudents(APIView):

    @staticmethod
    def get(*args, **kwargs):
        course = controller.get_all()
        serializer = StudentSerializer(course, many=True)
        return Response(serializer.data)


class ViewStudentProfile(APIView):

    @staticmethod
    def get(*args, **kwargs):
        uuid = kwargs['uuid']
        course = controller.get_by_id(uuid)
        serializer = StudentSerializer(course)
        return Response(serializer.data)
