from ..models.course import Course


class CoursesController:

    @staticmethod
    def get_all() -> list[dict]:
        try:
            response: list[dict] = Course.objects.all()
            return response
        except Exception:
            return []

    @staticmethod
    def get_by_id(course_id: str) -> dict:
        try:
            response: dict = Course.objects.get(id=course_id)
            return response
        except Exception:
            return {}
