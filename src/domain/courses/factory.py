import controllers
import use_cases
from repositories import courses_repository


def create():
    return controllers.create(use_case=use_cases.create(courses_repository))


def find():
    return controllers.find(use_case=use_cases.find(courses_repository))


def getAll():
    return controllers.getAll(use_case=use_cases.getAll(courses_repository))


def delete():
    return controllers.delete(use_case=use_cases.delete(courses_repository))
