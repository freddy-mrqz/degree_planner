# defines two functions that build paths based on the user's field of study, electives, and starting term
from itertools import cycle, islice
from variables import is_elective_requirements
from planner.models import Course
from term import *


def term_order(starting_term):
    terms = ['Fall', 'Winter', 'Spring']
    for i, semester in enumerate(terms):
        if starting_term in semester:
            order_of_terms = list(islice(cycle(terms), i, i+20))
            return order_of_terms


def check_path(prerequisite):
    split_prerequisite = prerequisite.split(" and ")
    count = 0
    for item in split_prerequisite:
        or_split = item.split(" or ")
        for or_item in or_split:
            if term.contains(or_item):
                count += 1
                break
    if count >= len(split_prerequisite):
        return True
    else:
        return False


def can_take(course):
    if term.contains(course.subject + " " + course.number):
        return False
    prerequisite = course.prereqs
    if prerequisite == "None" or prerequisite == "Instructor Consent":
        return True
    if check_path(prerequisite):
            return True
    else:
        return False


def add_choice(count, limit, choice, electives):
    if count < limit:
        for course in choice:
            for check_course in electives:
                if course.course_id == check_course.course_id:
                    if can_take(course):
                        term.add_course(course)
                        return True
    return False


def add_class(count, limit, electives):
    if count < limit:
        for course in electives:
            if can_take(course):
                term.add_course(course)
                return True
    return False


def add_core(core):
    for course in core:
        if can_take(course):
            term.add_course(course)
            return True
    return False


def cs_path_build(concentration, starting_term, number_of_courses, choice):
    concentration_count = 0
    elective_count = 0
    course_count = 0
    core = Course.objects.filter(cs_concentration='CORE')
    concentration = Course.objects.filter(cs_concentration=concentration)
    electives = Course.objects.exclude(cs_concentration='None').exclude(cs_concentration=concentration)
    concentration_fall = concentration.objects.filter(term='Fall')
    concentration_winter = concentration.objects.filter(term='Winter')
    concentration_spring = concentration.objects.filter(term='Spring')
    elective_fall = electives.objects.filter(term='Fall')
    elective_winter = electives.objects.filter(term='Winter')
    elective_spring = electives.objects.filter(term='Spring')
    order = term_order(starting_term)
    while True:
        for semester in order:
            if course_count >= 13:
                break
            if semester == "Fall":
                term_count = 0
                cycle_count = 0
                while term_count < number_of_courses:
                    if add_choice(concentration_count, 4, choice, concentration_fall):
                        concentration_count += 1
                        term_count += 1
                        course_count += 1
                    if add_core(core):
                        term_count += 1
                        course_count += 1
                    if add_class(elective_count, 4, elective_fall):
                        elective_count += 1
                        term_count += 1
                        course_count += 1
                    if cycle_count >= 5:
                        term.fill_empty(number_of_courses-term_count)
                        break
                    cycle_count += 1
            elif semester == "Winter":
                term_count = 0
                cycle_count = 0
                while term_count < number_of_courses:
                    if add_choice(concentration_count, 4, choice, concentration_winter):
                        concentration_count += 1
                        term_count += 1
                        course_count += 1
                    if add_core(core):
                        term_count += 1
                        course_count += 1
                    if add_class(elective_count, 4, elective_winter):
                        elective_count += 1
                        term_count += 1
                        course_count += 1
                    if cycle_count >= 5:
                        term.fill_empty(number_of_courses - term_count)
                        break
                    cycle_count += 1
            elif semester == "Spring":
                term_count = 0
                cycle_count = 0
                while term_count < number_of_courses:
                    if add_choice(concentration_count, 4, choice, concentration_spring):
                        concentration_count += 1
                        term_count += 1
                        course_count += 1
                    if add_core(core):
                        term_count += 1
                        course_count += 1
                    if add_class(elective_count, 4, elective_spring):
                        elective_count += 1
                        term_count += 1
                        course_count += 1
                    if cycle_count >= 5:
                        term.fill_empty(number_of_courses - term_count)
                        break
                    cycle_count += 1
        break


def is_limits(concentration):
    for key, value in is_elective_requirements.items():
        if key == concentration:
            return value


def add_capstone(course_count):
    capstone = Course.objects.get(course_id=30440)
    if course_count >= 10:
        if can_take(capstone):
            term.add_course(capstone)
            return True
    return False


def is_path_build(concentration, starting_term, number_of_courses, choice):
    concentration_count = 0
    elective_count = 0
    course_count = 0
    extra_count = 0
    core = Course.objects.filter(is_concentration='CORE')
    concentration = Course.objects.filter(is_concentration=concentration)
    electives = Course.objects.exclude(is_concentration='None').exclude(is_concentration=concentration)
    concentration_fall = concentration.objects.filter(term='Fall')
    concentration_winter = concentration.objects.filter(term='Winter')
    concentration_spring = concentration.objects.filter(term='Spring')
    elective_fall = electives.objects.filter(term='Fall')
    elective_winter = electives.objects.filter(term='Winter')
    elective_spring = electives.objects.filter(term='Spring')
    order = term_order(starting_term)
    elective_limit = is_limits(concentration)
    concentration_limit = (len(concentration_fall) + len(concentration_winter) + len(concentration_spring))
    while True:
        for semester in order:
            if course_count >= 13:
                break
            if semester == "Fall":
                term_count = 0
                cycle_count = 0
                while term_count < number_of_courses:
                    if add_choice(elective_count, elective_limit, choice, elective_fall):
                        elective_count += 1
                        term_count += 1
                        course_count += 1
                    if add_core(core):
                        term_count += 1
                        course_count += 1
                    if add_class(concentration_count, concentration_limit, concentration_fall):
                        concentration_count += 1
                        term_count += 1
                        course_count += 1
                    if add_class(extra_count, 1, elective_fall):
                        extra_count += 1
                        term_count += 1
                        course_count += 1
                    if add_capstone(course_count):
                        term_count += 1
                        course_count += 1
                    if cycle_count >= 5:
                        term.fill_empty(number_of_courses - term_count)
                        break
                    cycle_count += 1
            elif semester == "Winter":
                term_count = 0
                cycle_count = 0
                while term_count < number_of_courses:
                    if add_choice(elective_count, elective_limit, choice, elective_winter):
                        elective_count += 1
                        term_count += 1
                        course_count += 1
                    if add_core(core):
                        term_count += 1
                        course_count += 1
                    if add_class(concentration_count, concentration_limit, concentration_winter):
                        concentration_count += 1
                        term_count += 1
                        course_count += 1
                    if add_class(extra_count, 1, elective_winter):
                        extra_count += 1
                        term_count += 1
                        course_count += 1
                    if add_capstone(course_count):
                        term_count += 1
                        course_count += 1
                    if cycle_count >= 5:
                        term.fill_empty(number_of_courses - term_count)
                        break
                    cycle_count += 1
            elif semester == "Spring":
                term_count = 0
                cycle_count = 0
                while term_count < number_of_courses:
                    if add_choice(elective_count, elective_limit, choice, elective_spring):
                        elective_count += 1
                        term_count += 1
                        course_count += 1
                    if add_core(core):
                        term_count += 1
                        course_count += 1
                    if add_class(concentration_count, concentration_limit, concentration_spring):
                        concentration_count += 1
                        term_count += 1
                        course_count += 1
                    if add_class(extra_count, 1, elective_spring):
                        extra_count += 1
                        term_count += 1
                        course_count += 1
                    if add_capstone(course_count):
                        term_count += 1
                        course_count += 1
                    if cycle_count >= 5:
                        term.fill_empty(number_of_courses - term_count)
                        break
                    cycle_count += 1
        break