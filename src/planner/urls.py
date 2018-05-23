"""degree_planner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from planner.views.course import CourseList
from planner.views import (
    IndexView,
    CourseList,
    StudentList,
    LoginView,
    StudentForm,
    FacultyForm,
    CourseBrowser,
    StudentStep2,
    StudentFinish,
    FacultyStep2,
    FacultyFinish,
    FacultyLookup
)

urlpatterns = [
    path('planner/', IndexView.as_view()),
    path('courses/', CourseList.as_view()),
    path('students/', StudentList.as_view(), name='student-list'),
    path('login/', LoginView.as_view(), name='login-page'),
    path('student-form', StudentForm.as_view(), name='student-form'),
    path('faculty-form', FacultyForm.as_view(), name='faculty-form'),
    path('student-form/browse-courses', CourseBrowser.as_view(), name='browser'),
    path('student-form/path-step-2', StudentStep2.as_view()),
    path('student-form/path-display', StudentFinish.as_view()),
    path('faculty-form/student-path', FacultyLookup.as_view()),
    path('faculty-form/path-step-2', FacultyStep2.as_view()),
    path('faculty-form/path-display', FacultyFinish.as_view())
]
