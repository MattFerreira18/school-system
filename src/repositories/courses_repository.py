REPOSITORY = []


def create(data):
    REPOSITORY.append(data)


def findById(id):
    result = None

    for course in REPOSITORY:
        if (course.id == id):
            result = course
            break

    return result


def findAll():
    return REPOSITORY


def updateById(id, data):
    course = None

    for i in range(len(REPOSITORY)):
        if (REPOSITORY[i].id == id):
            course[i] = data
            break


def updateById(id, data):
    course = None

    for i in range(len(REPOSITORY)):
        if (REPOSITORY[i].id == id):
            course[i] = data
            break


def delById(id):
    filtered = filter(lambda course: course.id != id, REPOSITORY)

    REPOSITORY = filtered
