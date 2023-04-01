from ..models.student import Student


class StudentController:

    @staticmethod
    def get_all() -> list[dict]:
        try:
            response: list[dict] = Student.objects.all()
            return response
        except Exception:
            return []

    @staticmethod
    def get_by_id(uuid: str) -> dict:
        try:
            response: dict = Student.objects.get(id=uuid)
            return response
        except Exception:
            return {}
