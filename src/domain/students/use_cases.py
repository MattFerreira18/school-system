from entities.student import Student
from utils.string import isIdValid, isCpfValid


def create(students_repository):
    def execute(name, cpf, course_id):

        if (len(name) < 4):
            return 'invalid name length'

        if (not (isCpfValid(cpf))):
            return 'invalid cpf'

        if (not (isIdValid(course_id))):
            return 'course id invalid'

        student = Student(name, cpf, course_id)

        students_repository.create(student)

    return execute


def find(students_repository):
    def execute(id):
        if (not (isIdValid(id))):
            return 'student id invalid'

        student = students_repository.findById(id)

        return student

    return execute


def getAll(students_repository):
    def execute():
        students = students_repository.findAll()

        return students

    return execute


def delete(students_repository):
    def execute(id):
        if (not (isIdValid(id))):
            return 'student id invalid'

        students_repository.delById(id)

    return execute
