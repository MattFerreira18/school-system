from utils.string import genId


class Course:
    def __init__(self, id, name, duration) -> None:
        if (not (id)):
            id = genId()

        self.id = id
        self.name = name
        self.duration = duration
        pass

    @property
    def id(self):
        return self.id

    @property
    def name(self):
        return self.name

    @property
    def duration(self):
        return self.duration
