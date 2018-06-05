from django.shortcuts import render
from planner.filters import CourseFilter
from planner.models import Course

def search(request):
    course_list = Course.objects.all()
    course_filter = CourseFilter(request.GET, queryset=course_list)
    return render(request, 'planner/course_list.html', {'filter': course_filter})






