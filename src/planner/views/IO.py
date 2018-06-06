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
            string += term.to_string()
        except:
            raise Exception("Bad parameters")
    return string

def string_to_path(start,string):
    seasons = ['Fall','Winter','Spring']
    index = seasons.index(start)
    parsed = string.split(";")
    num = int(parsed[0])
    term_num = 1
    course_num_list = parsed[1:]
    courses = []
    path = []
    for course in course_num_list:
        try:
            course_num = int(course)
            to_add = Course.objects.get(course_id=course_num)
            courses.append(to_add)
            #courses.append(Course.objects.get(course_id=int(course)))
        except:
            courses.append("empty")
        if len(courses) == num:
            path.append(Term(seasons[index],courses))
            term_num += 1
            index = (index + 1) % 3
            courses = []
    if courses != []:
        path.append(Term(seasons[index],courses))
    return path
