import controllers
import use_cases
from repositories import lessons_repository


def create():
    return controllers.create(use_case=use_cases.create(lessons_repository))


def find():
    return controllers.find(use_case=use_cases.find(lessons_repository))


def getAll():
    return controllers.getAll(use_case=use_cases.getAll(lessons_repository))


def delete():
    return controllers.delete(use_case=use_cases.delete(lessons_repository))
