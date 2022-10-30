REPOSITORY = []


def create(data):
    REPOSITORY.append(data)


def findById(id):
    result = None

    for student in REPOSITORY:
        if (student.id == id):
            result = student
            break

    return result


def findByCpf(cpf):
    result = None

    for student in REPOSITORY:
        if (student.cpf == cpf):
            result = student
            break

    return result


def findAll():
    return REPOSITORY


def updateById(id, data):
    student = None

    for i in range(len(REPOSITORY)):
        if (REPOSITORY[i].id == id):
            student[i] = data
            break


def delById(id):
    filtered = filter(lambda student: student.id != id, REPOSITORY)

    REPOSITORY = filtered
