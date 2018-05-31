from django.views.generic import DetailView, ListView, TemplateView

from planner.models import Student
from planner.views import test, term

class StudentList(ListView):

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



class StudentForm(TemplateView):
    template_name = 'planner/student_path_form.html'


class CourseBrowser(TemplateView):
    template_name = 'planner/course_browser.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        course = [test.Test('CS','Algorithms',221,'Description Temp','None','Spring')]
        context['courses'] = course
        return context


class StudentStep2(TemplateView):
    template_name = 'planner/student_step_2.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        course = [
            test.Test('CSC','Algorithms',221,'Description Temp','None','Spring'),
            test.Test('CSC','Cryptology',333,'Cryptology Description','CSC 407','Winter'),
            test.Test('CSC','Object-Oriented Software Development',349,'OO Development','CSC 330 or CSC 310','Spring')
                ]
        context['courses'] = course
        return context


class StudentFinish(TemplateView):
    template_name = 'planner/student_finish.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        term1 = term.Term("Winter1")
        term1.add_course(test.Test('CSC','Algorithms',221,'Description Temp','None','Spring'))
        term1.add_course(test.Test('CSC','Cryptology',333,'Cryptology Description','CSC 407','Winter'))
        term1.add_course(test.Test('CSC','Object-Oriented Software Development',349,'OO Development','CSC 330 or CSC 310','Spring')) 
        path = [term1]
        context['path'] = path
        return context


