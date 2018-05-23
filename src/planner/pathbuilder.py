# defines two functions that build paths based on the user's field of study, electives, and starting term
import json
from itertools import cycle, islice


def get_data():
    with open('courses.json') as data_file:
        data = json.load(data_file)
    return data


def term_order(starting_term):
    terms = ['Fall', 'Winter', 'Spring']
    for i, term in enumerate(terms):
        if starting_term in term:
            order_of_terms = list(islice(cycle(terms), i, i+20))
            return order_of_terms


def prerequisite_check(course):
    course_subject = course.split()[0]
    course_number = course.split()[1]
    data = get_data()
    for item in data:
        if item.get("subject") == course_subject:
            if item.get("number") == course_number:
                return item.get("prereqs")


def check_path(path, prerequisite):
    split_prerequisite = prerequisite.split(" and ")
    count = 0
    for item in split_prerequisite:
        or_split = item.split(" or ")
        for term in path:
            for or_item in or_split:
                if or_item in term:
                    count += 1
                    break
    if count >= len(split_prerequisite):
        return True
    else:
        return False


def add_course(course, path):
    for term in path:
        if course in term:
            return False
    prerequisite = prerequisite_check(course)
    if prerequisite == "None" or prerequisite == "Instructor Consent":
        return True
    prerequisite_fulfilled = check_path(path, prerequisite)
    if prerequisite_fulfilled:
            return True
    else:
        return False


def is_limits(concentration):
    if concentration == 'Business Intelligence':
        return 3
    elif concentration == 'Database Administration':
        return 3
    elif concentration == 'Systems Analysis':
        return 2
    elif concentration == 'Enterprise Infrastructure':
        return 3


def cs_path_build(concentration, starting_term, number_of_courses):
    concentration_fall = []
    concentration_winter = []
    concentration_spring = []
    core = []
    elective_fall = []
    elective_winter = []
    elective_spring = []
    path = []
    concentration_count = 0
    elective_count = 0
    course_count = 0
    data = get_data()
    for item in data:
        if item.get("cs_concentration") == concentration:
            if item.get("term") == 'Fall':
                concentration_fall.append(item.get("subject")+" "+item.get("number"))
            elif item.get("term") == 'Winter':
                concentration_winter.append(item.get("subject")+" "+item.get("number"))
            elif item.get("term") == 'Spring':
                concentration_spring.append(item.get("subject")+" "+item.get("number"))
        elif item.get("cs_concentration") == "CORE":
            core.append(item.get("subject")+" "+item.get("number"))
        elif item.get("cs_concentration") != "None":
            if item.get("term") == 'Fall':
                elective_fall.append(item.get("subject") + " " + item.get("number"))
            elif item.get("term") == 'Winter':
                elective_winter.append(item.get("subject") + " " + item.get("number"))
            elif item.get("term") == 'Spring':
                elective_spring.append(item.get("subject") + " " + item.get("number"))
    order = term_order(starting_term)
    while True:
        for term in order:
            if course_count >= 13:
                break
            term_object = []
            term_object.append(term)
            if term == "Fall":
                term_count = 0
                for course in core:
                    if term_count < number_of_courses:
                        if add_course(course, path):
                            term_object.append(course)
                            term_count += 1
                            course_count += 1
                    else:
                        break
                for course in concentration_fall:
                    if concentration_count < 4:
                        if term_count < number_of_courses:
                            if add_course(course, path):
                                term_object.append(course)
                                concentration_count += 1
                                term_count += 1
                                course_count += 1
                        else:
                            break
                    else:
                        break
                for course in elective_fall:
                    if term_count < number_of_courses:
                        if elective_count < 4:
                            if add_course(course, path):
                                term_object.append(course)
                                elective_count += 1
                                term_count += 1
                                course_count += 1
                        else:
                            break
                    else:
                        break
            elif term == "Winter":
                term_count = 0
                for course in core:
                    if term_count < number_of_courses:
                        if add_course(course, path):
                            term_object.append(course)
                            term_count += 1
                            course_count += 1
                    else:
                        break
                for course in concentration_winter:
                    if concentration_count < 4:
                        if term_count < number_of_courses:
                            if add_course(course, path):
                                term_object.append(course)
                                concentration_count += 1
                                term_count += 1
                                course_count += 1
                        else:
                            break
                    else:
                        break
                for course in elective_winter:
                    if term_count < number_of_courses:
                        if elective_count < 4:
                            if add_course(course, path):
                                term_object.append(course)
                                elective_count += 1
                                term_count += 1
                                course_count += 1
                        else:
                            break
                    else:
                        break
            elif term == "Spring":
                term_count = 0
                for course in core:
                    if term_count < number_of_courses:
                        if add_course(course, path):
                            term_object.append(course)
                            term_count += 1
                            course_count += 1
                    else:
                        break
                for course in concentration_spring:
                    if concentration_count < 4:
                        if term_count < number_of_courses:
                            if add_course(course, path):
                                term_object.append(course)
                                concentration_count += 1
                                term_count += 1
                                course_count += 1
                        else:
                            break
                    else:
                        break
                for course in elective_spring:
                    if term_count < number_of_courses:
                        if elective_count < 4:
                            if add_course(course, path):
                                term_object.append(course)
                                elective_count += 1
                                term_count += 1
                                course_count += 1
                        else:
                            break
                    else:
                        break
            path.append(term_object)
        break
    print(path)


def is_path_build(concentration, starting_term, number_of_courses):
    concentration_fall = []
    concentration_winter = []
    concentration_spring = []
    core = []
    elective_fall = []
    elective_winter = []
    elective_spring = []
    path = []
    concentration_count = 0
    elective_count = 0
    course_count = 0
    elective_limit = is_limits(concentration)
    data = get_data()
    for item in data:
        if item.get("is_concentration") == "CORE " + concentration:
            if item.get("term") == 'Fall':
                concentration_fall.append(item.get("subject") + " " + item.get("number"))
            elif item.get("term") == 'Winter':
                concentration_winter.append(item.get("subject") + " " + item.get("number"))
            elif item.get("term") == 'Spring':
                concentration_spring.append(item.get("subject") + " " + item.get("number"))
        elif item.get("is_concentration") == "CORE":
            core.append(item.get("subject") + " " + item.get("number"))
        elif item.get("is_concentration") == concentration:
            if item.get("term") == 'Fall':
                elective_fall.append(item.get("subject") + " " + item.get("number"))
            elif item.get("term") == 'Winter':
                elective_winter.append(item.get("subject") + " " + item.get("number"))
            elif item.get("term") == 'Spring':
                elective_spring.append(item.get("subject") + " " + item.get("number"))
    order = term_order(starting_term)
    concentration_limit = (len(concentration_fall) + len(concentration_winter) + len(concentration_spring))
    while True:
        for term in order:
            if course_count >= 12:
                break
            term_object = []
            term_object.append(term)
            if term == "Fall":
                term_count = 0
                for course in core:
                    if term_count < number_of_courses:
                        if add_course(course, path):
                            term_object.append(course)
                            term_count += 1
                            course_count += 1
                    else:
                        break
                for course in concentration_fall:
                    if term_count < number_of_courses:
                        if concentration_count < concentration_limit:
                            if add_course(course, path):
                                term_object.append(course)
                                concentration_count += 1
                                term_count += 1
                                course_count += 1
                        else:
                            break
                    else:
                        break
                for course in elective_fall:
                    if term_count < number_of_courses:
                        if elective_count < elective_limit:
                            if add_course(course, path):
                                term_object.append(course)
                                elective_count += 1
                                term_count += 1
                                course_count += 1
                        else:
                            break
                    else:
                        break
            elif term == "Winter":
                term_count = 0
                for course in core:
                    if term_count < number_of_courses:
                        if add_course(course, path):
                            term_object.append(course)
                            term_count += 1
                            course_count += 1
                    else:
                        break
                for course in concentration_winter:
                    if term_count < number_of_courses:
                        if concentration_count < concentration_limit:
                            if add_course(course, path):
                                term_object.append(course)
                                concentration_count += 1
                                term_count += 1
                                course_count += 1
                        else:
                            break
                    else:
                        break
                for course in elective_winter:
                    if term_count < number_of_courses:
                        if elective_count < elective_limit:
                            if add_course(course, path):
                                term_object.append(course)
                                elective_count += 1
                                term_count += 1
                                course_count += 1
                        else:
                            break
                    else:
                        break
            elif term == "Spring":
                term_count = 0
                for course in core:
                    if term_count < number_of_courses:
                        if add_course(course, path):
                            term_object.append(course)
                            term_count += 1
                            course_count += 1
                    else:
                        break
                for course in concentration_spring:
                    if term_count < number_of_courses:
                        if concentration_count < concentration_limit:
                            if add_course(course, path):
                                term_object.append(course)
                                concentration_count += 1
                                term_count += 1
                                course_count += 1
                        else:
                            break
                    else:
                        break
                for course in elective_spring:
                    if term_count < number_of_courses:
                        if elective_count < elective_limit:
                            if add_course(course, path):
                                term_object.append(course)
                                elective_count += 1
                                term_count += 1
                                course_count += 1
                        else:
                            break
                    else:
                        break
            if term_count < number_of_courses:
                if course_count >= 10:
                    if add_course('IS 577', path):
                        term_object.append('IS 577')
                        term_count += 1
                        course_count += 1
            path.append(term_object)
        break
    print(path)


print("CS test Runs: ")
cs_path_build("Software and Systems Development", "Fall", 3)
cs_path_build("Theory", "Winter", 3)
cs_path_build("Data Science", "Spring", 3)
cs_path_build("Database Systems", "Winter", 3)
cs_path_build("Artificial Intelligence", "Fall", 3)
cs_path_build("Software Engineering", "Spring", 3)
cs_path_build("Game and Real-Time Systems", "Winter", 3)
cs_path_build("Human-Computer Interaction", "Fall", 3)


print("IS test Runs: ")
is_path_build("Database Administration", "Fall", 2)
is_path_build("Enterprise Infrastructure", "Spring", 2)
is_path_build("Business Intelligence", "Winter", 2)
is_path_build("Systems Analysis", "Fall", 2)
