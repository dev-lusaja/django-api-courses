from django.db import models


class Course(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.TextField(null=True, blank=True)
    period = models.IntegerField(null=True, blank=True)
    classes = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.TextField(null=True, blank=True)

    @property
    def period_formatted(self):
        if self.period > 1:
            return "{} meses".format(self.period)
        else:
            return "{} mes".format(self.period)

    @property
    def classes_formatted(self):
        if self.classes > 1:
            return "{} clases".format(self.classes)
        else:
            return "{} clase".format(self.classes)

    def __str__(self):
        return self.id.__str__()
