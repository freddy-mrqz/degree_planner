from django.views.generic import TemplateView
from django.shortcuts import render

from planner.views import term
from planner.views import test, pathform, step2form, variables

from planner.models import Course

class FacultyForm(TemplateView):
    template_name = 'planner/faculty_path_form.html'
    form_class = pathform.PathForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form' : form})


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
    form_class = pathform.PathForm
    form2_class = step2form.Step2Form
    course = None
    reqnum = 4
    ge4 = False
    ge3 = False
    ge2 = False

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        step2 = self.form2_class()
        if form.is_valid():
            subject = form.cleaned_data['subject']
            if subject == "CS":
                concentration = form.cleaned_data['cs_con']
                self.course = Course.objects.filter(cs_concentration=concentration)
            else:
                concentration = form.cleaned_data['is_con']
                self.reqnum = variables.is_elective_requirements[concentration]
                if concentration == 'Standard':
                    self.course = Course.objects.exclude(is_concentration__contains='CORE').exclude(is_concentration='None')
                else:
                    self.course = Course.objects.filter(is_concentration=concentration)
            if self.reqnum > 2: self.ge2 = True
            if self.reqnum > 3: self.ge3 = True
            if self.reqnum > 4: self.ge4 = True
        dic =  {'courses' : self.course, 
                    'reqnum' : self.reqnum, 
                    'step2' : step2,
                    'ge2' : self.ge2,
                    'ge3' : self.ge3,
                    'ge4' : self.ge4}
        return render(request, self.template_name,dic)


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


