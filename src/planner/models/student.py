from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Student(models.Model):
    # Studies
    INFORMATION_SERVICES = 'IS'
    COMPUTER_SCIENCE = 'CS'

    DEGREE_CHOICES = (
        (INFORMATION_SERVICES, 'Information Services'),
        (COMPUTER_SCIENCE, 'Computer Science'),
    )

    FALL = 'Fall'
    WINTER = 'Winter'
    SPRING = 'Spring'

    TERM_CHOICES = (
            (FALL, 'Fall'),
            (WINTER, 'Winter'),
            (SPRING, 'Spring')
                )

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    degree = models.CharField(max_length=2,choices=DEGREE_CHOICES)

    first_name = models.CharField(max_length=128, blank=True)
    last_name = models.CharField(max_length=128, blank=True)
    saved_path = models.CharField(max_length=500,blank=True)
    start_term = models.CharField(max_length=10,choices=TERM_CHOICES,default=FALL)

    def __str__(self):
        return '{}'.format(self.first_name)

    def full_name(self):
        if self.first_name != "" & self.last_name != "":
            return self.first_name + self.last_name
        else:
            print("Lacking required field (first_name, last_name)")

    def current_degree(self):
        return self.degree

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance,first_name=sender.first_name,last_name=sender.last_name)

    @receiver(post_save,sender=User)
    def save_user_profile(sender,instance,**kwargs):
        instance.profile.save()

    class Meta:
        app_label = "planner"
