from django.shortcuts import render
from planner.filters import CourseFilter
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from planner.models import Course

def search(request):
    course_list = Course.objects.all()
    course_filter = CourseFilter(request.GET, queryset=course_list)
    return render(request, 'planner/course_list.html', {'filter': course_filter})

@method_decorator(login_required)
def dispatch(self,*args, **kwargs):
    return super().dispatch(*args, **kwargs)
