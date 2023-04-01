from rest_framework.serializers import ModelSerializer
from ...models.course import Course


class CourseEnrollmentSerializer(ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'
