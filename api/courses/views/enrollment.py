from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers.enrollment import CourseEnrollmentSerializer
from ..controllers.enrollment import EnrollmentController as controller


class ViewEnrollmentByStudent(APIView):

    @staticmethod
    def get(*args, **kwargs):
        uuid = kwargs['uuid']
        enrollments = controller.get_by_student_id(uuid)
        serializer = CourseEnrollmentSerializer(enrollments, many=True)
        return Response(serializer.data)
