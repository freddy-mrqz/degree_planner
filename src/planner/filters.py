from planner.models.course import Course
import django_filters

class CourseFilter(django_filters.FilterSet):
  class Meta:
    model = Course
    fields = ['subject', 'number', 'name']