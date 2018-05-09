from django.views.generic import ListView
from models.course import Course


class CourseList(ListView):
    model = Course
    context_object_name = 'course_list'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all courses
        context['courses'] = Course.objects.all()
        return context
