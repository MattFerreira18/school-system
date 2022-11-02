def create(use_case):
    print('Qual é o nome do aluno?\n')
    name = input()
    print('Qual é o CPF do aluno?\n')
    cpf = input()
    print('Esse aluno faz parte de qual curso?\n')
    course_id = input()

    result = use_case(name, cpf, course_id)

    if (isinstance(result, str)):
        print('Você digitou alguma informação inválida, tente novamente.')
        print(f'mensagem de erro: {result}')
        print('Digite:')
        print('1 - tentar novamente')
        print('0 - voltar para o menu anterior')
        option = int(input())

        if (option):
            return create(use_case)

        return False

    print('Aluno criado com sucesso!\n\n')

    return True


def find(use_case):
    print('Qual é o RA do aluno?\n')
    ra = input()

    result = use_case(ra)

    if (isinstance(result, str)):
        print('Você digitou alguma informação inválida, tente novamente.')
        print(f'mensagem de erro: {result}')
        print('Digite:')
        print('1 - tentar novamente')
        print('0 - voltar para o menu anterior')
        option = int(input())

        if (option):
            return find(use_case)

        return False

    print('=' * 20)
    print(f'aluno: {result.name}')
    print(f'possui o CPF: {result.cpf}')
    print(f'faz parte do curso: {result.course_id}')
    print('=' * 20)

    return True


def getAll(use_case):
    result = use_case()

    for student in result:
        print('=' * 20)
        print(f'Identificador: {student.id}')
        print(f'aluno: {student.name}')
        print(f'possui o CPF: {student.cpf}')
        print(f'faz parte do curso: {student.course_id}')

    return True


def update(use_case):
    print('Qual é o RA do aluno?\n')
    ra = input()
    print('Qual é o nome do aluno?\n')
    name = input()
    print('Qual é o CPF do aluno?\n')
    cpf = input()
    print('Esse aluno faz parte de qual curso?\n')
    course_id = input()

    result = use_case(ra, name, cpf, course_id)

    if (isinstance(result, str)):
        print('Você digitou alguma informação inválida, tente novamente.')
        print(f'mensagem de erro: {result}')
        print('Digite:')
        print('1 - tentar novamente')
        print('0 - voltar para o menu anterior')
        option = int(input())

        if (option):
            return create(use_case)

        return False

    print('Aluno atualizado com sucesso!\n\n')

    return True


def delete(use_case):
    print('Qual é o identificador do aula?\n')
    id = input()

    print(f'Você digitou o identificador: {id}')
    print(f'Esta informação está correta? Lembrando que uma vez feita a remoção, você não poderá voltar atrás')
    option = int(input())

    if (not (option)):
        print('Parece que você digitou o identificador do aula errado.')
        print('Digite:')
        print('1 - tentar novamente')
        print('0 - voltar para o menu anterior')
        option = int(input())

        if (option):
            return delete(use_case)

        return False

    result = use_case(id)

    if (isinstance(result, str)):
        print('Você digitou alguma informação inválida, tente novamente.')
        print(f'mensagem de erro: {result}')
        print('Digite:')
        print('1 - tentar novamente')
        print('0 - voltar para o menu anterior')
        option = int(input())

        if (option):
            return find(use_case)

        return False

    print('aula deletada com sucesso!\n\n')

    return True
