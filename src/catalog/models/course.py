from django.db import models

class Course(models.Model):
    subject = models.CharField(max_length=4)
    course_number = models.IntegerField()
    class Meta:
        app_label = "catalog"