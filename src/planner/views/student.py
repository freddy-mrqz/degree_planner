from django.views.generic import DetailView, ListView, TemplateView
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from planner.models import Student, Course
from planner.views import test, term, pathform, variables, step2form, lookup_form, pathbuilder


subject = None
start = None
num_per = None
con = None
final_path = None

class StudentForm(TemplateView):
    template_name = 'planner/student_path_form.html'
    form_class = pathform.PathForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        global subject
        global start
        global num_per
        global con
        global final_path
        subject = None
        start = None
        num_per = None
        con = None
        final_path = None
        return render(request, self.template_name, {'form' : form})


class StudentLoad(TemplateView):
    template_name = 'planner/student_load.html'
    path = None

    def get(self, request, *args, **kwargs):
        path_string = User.student.saved_path
        start_season = User.student.start_term
        if path_string:
            self.path = IO.string_to_path(start_season,path_string)
        return render(request, self.template_name, {'path' : path})


class StudentStep2(TemplateView):
    template_name = 'planner/student_step_2.html'
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
        global subject
        global start
        global num_per
        global con
        if form.is_valid():
            form_subject = form.cleaned_data['subject']
            subject = form_subject
            form_start = form.cleaned_data['start']
            start = form_start
            form_num = form.cleaned_data['num']
            if form_num == '1':
                num_per = 1
            elif form_num =='2':
                num_per = 2
            else:
                num_per = 3
            if form_subject == "CS":
                concentration = form.cleaned_data['cs_con']
                con = concentration
                self.course = Course.objects.filter(cs_concentration=concentration)
            else:
                concentration = form.cleaned_data['is_con']
                con = concentration
                self.reqnum = variables.is_elective_requirements[concentration]
                if concentration == 'Standard':
                    self.course = Course.objects.exclude(is_concentration__contains='CORE').exclude(is_concentration='None')
                else:
                    self.course = Course.objects.filter(is_concentration=concentration)
            if self.reqnum > 2: self.ge2 = True
            if self.reqnum > 3: self.ge3 = True
            if self.reqnum > 4: self.ge4 = True
        dic =  {    'courses' : self.course,
                    'form' : form,
                    'reqnum' : self.reqnum, 
                    'step2' : step2,
                    'ge2' : self.ge2,
                    'ge3' : self.ge3,
                    'ge4' : self.ge4}
        return render(request, self.template_name,dic) 


class StudentFinish(TemplateView):
    template_name = 'planner/student_finish.html'
    form2_class = step2form.Step2Form
    path = None
    local_sub = None
    local_start = None
    local_num_per = None
    local_con = None

    def post(self,request,*args,**kwargs):
        global subject
        global start
        global num_per
        global con
        global final_path
        self.local_sub = subject
        if start == '1':
            self.local_start = "Fall"
        elif start == '2':
            self.local_start = "Winter"
        else:
            self.local_start = "Spring"
        self.local_num_per = num_per
        self.local_con = con
        step2 = self.form2_class(request.POST)
        if step2.is_valid():
            electives = []
            electives.append(Course.objects.get(course_id=int(step2.cleaned_data['elec1'])))
            electives.append(Course.objects.get(course_id=int(step2.cleaned_data['elec2'])))
            if step2.cleaned_data['elec3']:
                electives.append(Course.objects.get(course_id=int(step2.cleaned_data['elec3'])))
            if step2.cleaned_data['elec4']:
                electives.append(Course.objects.get(course_id=int(step2.cleaned_data['elec4'])))
            if step2.cleaned_data['elec5']:
                electives.append(Course.objects.get(course_id=int(step2.cleaned_data['elec5'])))
            if step2.cleaned_data['elec6']:
                electives.append(Course.objects.get(course_id=int(step2.cleaned_data['elec6'])))
            if step2.cleaned_data['elec7']:
                electives.append(Course.objects.get(course_id=int(step2.cleaned_data['elec7'])))
            if self.local_sub == 'CS':
                self.path = pathbuilder.cs_path_build(self.local_con,self.local_start,self.local_num_per,electives)
            else:
                self.path = pathbuilder.is_path_build(self.local_con,self.local_start,self.local_num_per,electives)
        return render(request,self.template_name,{'path' : self.path})


class StudentSave(TemplateView):
    template_name = 'planner/student_save.html'

    def post(self,request,*args,**kwargs):
        global final_path
        path = final_path
        path_string = path_to_string(path)
        User.student.saved_path = path_string
        User.save()
        return redirect('student-form/')
