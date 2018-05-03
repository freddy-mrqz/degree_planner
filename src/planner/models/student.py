from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


@python_2_unicode_compatible
class Student(models.Model):
    # Grades 
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    # Studies
    INFORMATION_TECHNOLOGY = 'IT'
    COMPUTER_SCIENCE = 'CS'
    UNDECIDED = 'NA'

    DEGREE_CHOICES = (
        (INFORMATION_TECHNOLOGY, 'Information Technology'),
        (COMPUTER_SCIENCE, 'Computer Science'),
    ) 

    YEAR_IN_SCHOOL_CHOICES = (
        (FRESHMAN, 'Freshman'),
        (SOPHMORE, 'Sophmore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
    ) 

    degree_in_school = models.CharField(
        max_length=2,
        choices=DEGREE_CHOICES,
    )
    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMAN,
    )
   

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=128, blank=True)
    last_name = models.CharField(max_length=128, blank=True)
   
    credits = models.IntField(null=True, blank=True)
 
    def __str__(self): 
        return '{}'.format(first_name)

    def full_name(self):
        if self.first_name != "" && self.last_name != "":
            return self.first_name + self.last_name
        else:
            print("Lacking required field (first_name, last_name)")

    def is_upperclass(self):
        return self.year_in_school in (self.JUNIOR, self.SENIOR)

    def current_degree(self):
        return self.degree_in_school
