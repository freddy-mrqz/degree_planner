from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.shortcuts import render

class HomePage(TemplateView):
    template_name="planner/student_home"
    
    def get(self, request, *args, **kwargs):
        user=request.user
        return render(request, self.template_name, {"user" : user})