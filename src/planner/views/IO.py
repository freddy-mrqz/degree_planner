#IO.py
'''
defines functions for converting a path intoa a string for storage and converting a string into
    path for display
'''

from planner.models import Course
from planner.views.term import Term

def path_to_string(num,path):
    string = str(num) + ";"
    for term in path:
        try:
            string += term.toString()
        except:
            raise Exception("Bad parameters")
    return string

def string_to_path(string):
    parsed = string.split(";")
    num = int(parsed[0])
    term_num = 1
    courses = []
    path = []
    for course in parsed[1:]:
        try:
            courses.append(Course.objects.get(course_id=int(course)))
        except:
            raise Exception("requires a list of correct course numbers")
        if len(courses) == num:
            path.append(Term(1,courses))
            term_num += 1
            courses = []
