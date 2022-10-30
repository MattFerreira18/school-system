from entities.lesson import Lesson
from utils.string import isIdValid


def create(lessons_repository):
    def execute(name, course_id):
        if (len(name) < 4):
            return 'invalid name length'

        if (not (isIdValid(course_id))):
            return 'course id invalid'

        lesson = Lesson(name, course_id=course_id)

        lessons_repository.create(lesson)

    return execute


def find(lessons_repository):
    def execute(id):
        if (not (isIdValid(id))):
            return 'lesson id invalid'

        lesson = lessons_repository.findById(id)

        return lesson

    return execute


def getAll(lessons_repository):
    def execute():
        lessons = lessons_repository.findAll()

        return lessons

    return execute


def delete(lessons_repository):
    def execute(id):
        if (not (isIdValid(id))):
            return 'lesson id invalid'

        lessons_repository.delById(id)

    return execute
