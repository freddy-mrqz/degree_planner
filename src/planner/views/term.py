#term.py
'''
defines a class to hold course objects for use in a path
contains a name and a list of courses
'''
from planner.models import Course
import logging

logger = logging.getLogger(__name__)

class Term():

    def __init__(self,string,lst=[]):
        self.name = string
        self.courses = lst

    def __repr__(self):
        return self.courses

    def to_string(self):
        to_return = ""
        for course in self.courses:

            try:
                to_return += course.course_id + ";"
            except:
                to_return += "empty;"
        return to_return

    def fill_empty(self,num):
        for x in range(num):
            self.courses.append("empty")

    def add_course(self,course):
        self.courses.append(course)

    def contains(self,course_string):
        #condition = course_string.split(" ")
        for course in self.courses:
            #if course.subject == condition[0] and course.number == condition[1]:
            if course == 'empty':
                continue
            if course == '':
                continue
            if course.course_id == course_string:
                return True
        return False
