
banco_de_dados =[]
matricula_atual = 0

def criarAluno(nome, idade, curso):
    global matricula_atual
    matricula_atual +=1
    aluno = {
        'matricula': matricula_atual,
        'nome': nome,
        'idade': idade,
        'curso': curso
    }
    return aluno
def adicionarAluno (nome, idade, curso):
    aluno = criarAluno(nome, idade, curso)
    banco_de_dados.append(aluno)
    print('Aluno adicionado com sucesso!')

def listarTodosAlunos():
    print(f'-----Alunos matriculados----')
    for aluno in banco_de_dados:
        print(f"matricula: {aluno['matricula']}")
        print(f"nome: {aluno['nome']}")
        print(f"idade: {aluno['idade']}")
        print(f"curso: {aluno['curso']}")
        print('---------------------\n')

def editarAluno(matricula, nome, idade, curso):
    aluno = alunoExiste(matricula)
    if aluno:
        aluno['nome'] = nome
        aluno['idade'] = idade
        aluno['curso'] = curso
        print('Dados alterados com suscesso!')
    else:
        print('Matricula informada não encontrada')

def alunoExiste(matricula):
    for aluno in banco_de_dados:
        if aluno['matricula'] == matricula:
            return aluno
    return False
def removerAluno(matricula):
    aluno = alunoExiste(matricula)
    if aluno:
        banco_de_dados.remove(aluno)
        print('Aluno removido com sucesso!')
    else:
        print('Matricula não encontrada.')

def consultarAluno(matricula):
    aluno = alunoExiste(matricula)
    if aluno:
         print('-----Dados do aluno-----')
         print(f"nome: {aluno['nome']}")
         print(f"idade: {aluno['idade']}")
         print(f"curso: {aluno['curso']}")
    else:
         print('Matricula não encontrada!')

def menu():
    while True:
        print('----Bem vindo ao menu escolar.----')
        print('1 - Adicionar Aluno')
        print('2 - Editar aluno')
        print('3 - Remover aluno')
        print('4 - Buscar aluno')
        print('5 - Listar aluno')
        print('6 - Sair do sistema')
        opcao = input('Selecione uma opção: ')
        if opcao == '1':
            nome = input("Digite o nome: ")
            idade = int(input('Digite a idade: '))
            curso = input('Digite o curso: ')
            adicionarAluno(nome, idade, curso)
        elif opcao == '2':
            matricula = int(input("Digite a matricula: "))
            nome = input("Digite o nome: ")
            idade = int(input('Digite a idade: '))
            curso = input('Digite o curso: ')
            editarAluno(matricula, nome, idade, curso)
        elif opcao == '3':
            matricula = int(input("Digite a matricula: "))
            removerAluno(matricula)
        elif opcao == '4':
            matricula = input("Digite a matricula: ")
            consultarAluno(matricula)
        elif opcao == '5':
            listarTodosAlunos()
        elif opcao == '6':
            break
        else:
            print('Opção inválida')
menu()

