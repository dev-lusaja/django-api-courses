from ..models.student import Student


class EnrollmentController:

    @staticmethod
    def get_by_student_id(uuid: str):
        try:
            student = Student.objects.get(id=uuid)
            enrollments = student.enrollments.all()
            data = []
            for enrollment in enrollments:
                data.append(enrollment.course)
            return data
        except Exception:
            return []
