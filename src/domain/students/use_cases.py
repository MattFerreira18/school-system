from presentations.student_presentation import student_presentation
from entities.student import Student
from utils.string import isIdValid, isCpfValid, isRaValid


def create(students_repository, courses_repository):
    def execute(name, cpf, course_id):

        if (len(name) < 4):
            return 'invalid name length'

        if (not (isCpfValid(cpf))):
            return 'invalid cpf'

        if (not (isIdValid(course_id))):
            return 'course id invalid'

        cpf_already_exists = students_repository.findByCpf(cpf)

        if (cpf_already_exists):
            return 'cpf already registered'

        course_exists = courses_repository.findById(course_id)

        if (not (course_exists)):
            return 'couse not found'

        student = Student(name, cpf, course_id)

        students_repository.create(student)

    return execute


def find(students_repository):
    def execute(ra):
        if (not (isRaValid(ra))):
            return 'student RA invalid'

        student = students_repository.findByRa(ra)

        if (not (student)):
            return None

        return student_presentation(student)

    return execute


def getAll(students_repository):
    def execute():
        students = students_repository.findAll()

        return map(student_presentation, students)

    return execute


def delete(students_repository):
    def execute(id):
        if (not (isIdValid(id))):
            return 'student id invalid'

        students_repository.delById(id)

    return execute
