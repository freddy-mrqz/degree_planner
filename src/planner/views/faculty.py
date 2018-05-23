from django.views.generic import TemplateView

from planner.views import term
from planner.views import test

class FacultyForm(TemplateView):
    template_name = 'planner/faculty_path_form.html'


class FacultyLookup(TemplateView):
    template_name = 'planner/faculty_lookup.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        term1 = term.Term("Winter1")
        term1.add_course(test.Test('CSC','Algorithms',221,'Description Temp','None','Spring'))
        term1.add_course(test.Test('CSC','Cryptology',333,'Cryptology Description','CSC 407','Winter'))
        term1.add_course(test.Test('CSC','Object-Oriented Software Development',349,'OO Development','CSC 330 or CSC 310','Spring')) 
        path = [term1]
        context['path'] = path
        return context



class FacultyStep2(TemplateView):
    template_name = 'planner/faculty_step_2.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        course = [
            test.Test('CSC','Algorithms',221,'Description Temp','None','Spring'),
            test.Test('CSC','Cryptology',333,'Cryptology Description','CSC 407','Winter'),
            test.Test('CSC','Object-Oriented Software Development',349,'OO Development','CSC 330 or CSC 310','Spring')
                ]
        context['courses'] = course
        return context


class FacultyFinish(TemplateView):
    template_name = 'planner/faculty_finish.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        term1 = term.Term("Winter1")
        term1.add_course(test.Test('CSC','Algorithms',221,'Description Temp','None','Spring'))
        term1.add_course(test.Test('CSC','Cryptology',333,'Cryptology Description','CSC 407','Winter'))
        term1.add_course(test.Test('CSC','Object-Oriented Software Development',349,'OO Development','CSC 330 or CSC 310','Spring')) 
        path = [term1]
        context['path'] = path
        return context


