from django.db import models


class Parent(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.TextField()

    def __str__(self):
        return self.id.__str__()


class StudentParent(models.Model):
    id = models.UUIDField(primary_key=True)
    student_id = models.UUIDField()
    parent_id = models.UUIDField()

    def __str__(self):
        return self.id.__str__()
