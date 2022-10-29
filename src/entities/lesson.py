from utils.string import genId


class Lesson:
    def __init__(self, id, name, course_id) -> None:
        if (not (id)):
            id = genId()

        self.id = id
        self.name = name
        self.course_id = course_id
        pass

    @property
    def id(self):
        return self.id

    @property
    def name(self):
        return self.name

    @property
    def course_id(self):
        return self.course_id
