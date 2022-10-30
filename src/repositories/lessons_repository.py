REPOSITORY = []


def create(data):
    REPOSITORY.append(data)


def findById(id):
    result = None

    for lesson in REPOSITORY:
        if (lesson.id == id):
            result = lesson
            break

    return result


def findAll():
    return REPOSITORY


def updateById(id, data):
    lesson = None

    for i in range(len(REPOSITORY)):
        if (REPOSITORY[i].id == id):
            lesson[i] = data
            break


def delById(id):
    filtered = filter(lambda lesson: lesson.id != id, REPOSITORY)

    REPOSITORY = filtered
