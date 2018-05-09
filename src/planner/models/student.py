from django.contrib.auth.models import User
from django.db import models


class Student(models.Model):
    # Studies
    INFORMATION_SERVICES = 'IS'
    COMPUTER_SCIENCE = 'CS'

    DEGREE_CHOICES = (
        (INFORMATION_SERVICES, 'Information Services'),
        (COMPUTER_SCIENCE, 'Computer Science'),
    )
    degree = models.CharField(max_length=2,choices=DEGREE_CHOICES)

    first_name = models.CharField(max_length=128, blank=True)
    last_name = models.CharField(max_length=128, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    credits = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.first_name)

    def full_name(self):
        if self.first_name != "" & self.last_name != "":
            return self.first_name + self.last_name
        else:
            print("Lacking required field (first_name, last_name)")

    def current_degree(self):
        return self.degree

    def required_credits(self):
        CREDIT_REQUIREMENT = 192
        rc = CREDIT_REQUIREMENT - self.credits
        return rc

    class Meta:
        app_label = "planner"
