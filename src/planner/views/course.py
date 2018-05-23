from django.views.generic import ListView

from planner.models import Course


class CourseList(ListView):
    model = Course



