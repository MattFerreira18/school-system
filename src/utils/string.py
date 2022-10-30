import uuid


def genId():
    return uuid.uuid4()


def isIdValid(string):
    try:
        uuid.UUID(str(string))
        return True
    except:
        return False


def isCpfValid(string):
    return True
