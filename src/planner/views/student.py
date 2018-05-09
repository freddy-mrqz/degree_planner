from django.views.generic import DetailView

from planner.models import Student


class CourseList(ListView):

    model = Student
    context_object_name = 'student_list'


class StudentDetail(DetailView):

    model = Student

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the courses
        context['student_*'] = Student.objects.all()
        return context
