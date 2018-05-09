from django.db import models


class Course(models.Model):
    id = models.IntegerField(blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    subject = models.CharField(max_length=4, blank=True, null=True)
    class_section = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=128, blank=True, null=True)
    credit_hours = models.IntegerField(max_length=1, blank=True, null=True)

    def __string__(self):
        return "{}".format(self.number)

    class Meta:
        app_label = "catalog"
