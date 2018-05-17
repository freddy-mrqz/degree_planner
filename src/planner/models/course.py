from django.db import models


class Course(models.Model):
    course_id = models.IntegerField(primary_key=True, default=0)
    subject = models.CharField(max_length=4, blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    term = models.CharField(max_length=16, blank=True, null=True)
    prereqs = models.CharField(max_length=64, blank=True, null=True)
    cs_concentration = models.CharField(max_length=64, blank=True, null=True)
    is_concentration = models.CharField(max_length=64, blank=True, null=True)

    def __string__(self):
        return "{}".format(self.number)

    class Meta:
        app_label = "planner"
