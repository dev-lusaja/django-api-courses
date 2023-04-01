from django.db import models


class Student(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.TextField()

    def __str__(self):
        return self.id.__str__()
