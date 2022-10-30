from entities.course import Course
from utils.string import isIdValid


def create(courses_repository):
    def execute(name, duration):
        if (not (duration.is_numeric())):
            return 'invalid duration value type'

        if (len(name) < 4):
            return 'invalid name length'

        course = Course(name, duration=int(duration))

        courses_repository.create(course)

    return execute


def find(courses_repository):
    def execute(id):
        if (not (isIdValid(id))):
            return 'course id invalid'

        course = courses_repository.findById(id)

        return course

    return execute


def getAll(courses_repository):
    def execute():
        courses = courses_repository.findAll()

        return courses

    return execute


def delete(courses_repository):
    def execute(id):
        if (not (isIdValid(id))):
            return 'course id invalid'

        courses_repository.delById(id)

    return execute
