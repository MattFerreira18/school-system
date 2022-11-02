import string
import uuid
from random import randint, choice


def genId():
    return uuid.uuid4()


def genRa():
    return f'{choice(string.ascii_letters)}{choice(string.ascii_letters)}{randint(10_000, 99_999)}'
