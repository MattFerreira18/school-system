from utils.string import genId, genRa


class Student:
    def __init__(self, id, name, cpf, ra, course_id) -> None:
        if (not (id)):
            id = genId()

        if (not (ra)):
            ra = genRa()

        self.id = id
        self.name = name
        self.cpf = cpf
        self.ra = ra
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
    def ra(self):
        return self.ra

    @property
    def course_id(self):
        return self.course_id
