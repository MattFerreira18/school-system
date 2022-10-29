from utils.string import genId


class Student:
    def __init__(self, id, name, cpf, course_id) -> None:
        if (not (id)):
            id = genId()

        self.id = id
        self.name = name
        self.cpf = cpf
        self.course_id = course_id
        pass

    @property
    def id(self):
        return self.id

    @property
    def name(self):
        return self.name

    @property
    def cpf(self):
        return self.cpf

    @property
    def course_id(self):
        return self.course_id
