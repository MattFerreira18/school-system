import time
import random
from utils import os
from domain.courses import factory as courses_factory
from domain.lessons import factory as lessons_factory
from domain.students import factory as students_factory

ENTITIES = ['Alunos', 'Cursos', 'Aulas']
CRUD_ACTIONS = ['criar', 'listar todos',
                'listar somente um', 'atualizar', 'remover']


def showLoadingInterface():
    print('=' * 28)
    print('\n\n')
    print('Iniciando Sistema Escolar')
    print('         aguarde...')
    print('\n\n')
    print('=' * 28)

    time.sleep(random.randint(1, 5))
    os.clear()


def loadEntitiesInterface():
    print('=' * 28)
    print('\nSelecione uma entidade: \n\n')

    for i, entity in enumerate(ENTITIES):
        print(f'{i + 1} - {entity}')

    print('\n')
    selected_entity = int(input())

    if (selected_entity < 1 or selected_entity > len(ENTITIES)):
        print('Você digitou uma opção inexistente, tente novamente:')
        return loadEntitiesInterface()

    print('=' * 28)
    os.clear()

    return selected_entity - 1


def getSelectedEntityFactory(selected_entity):
    match(selected_entity):
        case 0:
            return students_factory
        case 1:
            return courses_factory
        case 2:
            return lessons_factory


def callSelectedEntityAction(selected_factory, selected_action):
    match(selected_action):
        case 0:
            return selected_factory.create()
        case 1:
            return selected_factory.find()
        case 2:
            return selected_factory.getAll()
        case 3:
            return selected_factory.update()
        case 4:
            return selected_factory.delete()


def loadCrudActionsInterface():
    print('=' * 28)
    print('\nSelecione uma das ações: \n\n')

    for i, action in enumerate(CRUD_ACTIONS):
        print(f'{i + 1} - {action}')

    print('\n')
    selected_action = int(input())

    if (selected_action < 1 or selected_action > len(ENTITIES)):
        print('Você digitou uma opção inexistente, tente novamente:')
        return loadCrudActionsInterface()

    print('=' * 28)
    os.clear()

    return selected_action - 1


def main():
    showLoadingInterface()
    selected_entity = loadEntitiesInterface()
    selected_action = loadCrudActionsInterface()
    selected_factory = getSelectedEntityFactory(selected_entity)
    callSelectedEntityAction(selected_action, selected_factory)


main()
