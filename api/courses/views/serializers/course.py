from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from ...models.course import Course


class CourseSerializer(ModelSerializer):
    period_formatted = serializers.ReadOnlyField()
    classes_formatted = serializers.ReadOnlyField()

    class Meta:
        model = Course
        fields = '__all__'
