from entities.course import Course
from presentations.course_presentation import course_presentation
from utils.validate import isIdValid


def create(courses_repository):
    def execute(name, duration):
        if (not (duration.isnumeric())):
            return 'invalid duration value type'

        if (len(name) < 4):
            return 'invalid name length'

        course_already_exists = courses_repository.findByName(name)

        if (course_already_exists):
            return 'course name already exists'

        course = Course(id=None, name=name, duration=int(duration))

        courses_repository.create(course)

    return execute


def find(courses_repository):
    def execute(id):
        if (not (isIdValid(id))):
            return 'course id invalid'

        course = courses_repository.findById(id)

        if (not (course)):
            return 'course not found'

        return course_presentation(course)

    return execute


def getAll(courses_repository):
    def execute():
        courses = courses_repository.findAll()

        return map(course_presentation, courses)

    return execute


def edit(courses_repository):
    def execute(id, name, duration):
        if (not (isIdValid(id))):
            return 'course id invalid'

        course = courses_repository.findById(id)

        if (not (course)):
            return 'course not found'

        if (len(name) < 4):
            return 'invalid name length'

        course = Course(id=course.id, name=name, duration=int(duration))

        courses_repository.updateById(id, course)

    return execute


def delete(courses_repository):
    def execute(id):
        if (not (isIdValid(id))):
            return 'course id invalid'

        courses_repository.delById(id)

    return execute
