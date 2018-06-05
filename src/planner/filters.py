from planner.models.course import Course
import django_filters

class CourseFilter(django_filters.FilterSet):
  name = django_filters.CharFilter(lookup_expr='icontains')
  class Meta:
    model = Course
    fields = ['subject', 'number', 'name']