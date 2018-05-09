from django.views.generic import ListView, DetailView

from planner.models import Course


class CourseList(ListView):

    model = Course
    context_object_name = 'course_list'


class CourseDetail(DetailView):

    model = Course

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the courses
        context['course_list'] = Course.objects.all()
        return context
