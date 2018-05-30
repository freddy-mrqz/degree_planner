#term.py
'''
defines a class to hold course objects for use in a path
contains a name and a list of courses
'''

class Term():

    def __init__(self,string,lst=[]):
        self.name = string
        self.courses = lst

    def to_string(self):
        to_return = ""
        for course in self.courses:
            to_return += course.id + ";"
        return to_return

    def fill_empty(self,num):
        for x in range(num):
            self.courses.append("empty")

    def add_course(self,course):
        self.courses.append(course)

    def contains(self,course_string):
        condition = course_string.split(" ")
        for course in self.courses:
            if course.subject == condition[0] and course.coursename == condition[1]:
                return True
        return False
