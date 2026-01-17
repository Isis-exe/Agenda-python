def menu():
    voltarMenuPrincipal = 's'
    while voltarMenuPrincipal == 's':
        opcao = input('''
    ===============================================
            Projeto Agenda em Python
    MENU:

    [1] Cadastrar contato
    [2] Listar contato
    [3] Deletar contato
    [4] Buscar contato pelo nome
    [5] Atualizar contato
    [6] Sair
    ===============================================
    Escolha uma opção acima:''')
        if opcao == "1":
            cadastrarContato()
        elif opcao == "2":
            listarContato()
        elif opcao == "3":
            deletarContato()
        elif opcao == "4":
            buscarContatoPeloNome()
        elif opcao == "5":
            atualizarContato()
        else:
            sair()
        voltarMenuPrincipal = input(
            'Deseja voltar ao menu principal? (s/n) ').lower()


def atualizarContato():
    nomeAtualizar = input(
        f'Digite o nome do contato que deseja atualizar: ').lower()
    agenda = open("agenda.txt", "r")
    aux = []
    aux2 = []
    for i in agenda:
        aux.append(i)
    for i in range(0, len(aux)):
        if nomeAtualizar not in aux[i].lower():
            aux2.append(aux[i])
        else:
            print('Contato encontrado. Insira os novos dados:')
            idContato = input('Escolha o ID do seu contato: ')
            nome = input("Escreva o nome do seu contato: ")
            telefone = input("Escreva o telefone do contato: ")
            email = input("Escreva o e-mail do contato: ")
            dadosAtualizados = f'{idContato};{nome};{telefone};{email} \n'
            aux2.append(dadosAtualizados)
    agenda = open("agenda.txt", "w")
    for i in aux2:
        agenda.write(i)
    print(f'Contato atualizado com sucesso.')
    listarContato()


def cadastrarContato():
    idContato = input('Escolha o ID do seu contato: ')
    nome = input("Escreva o nome do seu contato: ")
    telefone = input("Escreva o telefone do contato: ")
    email = input("Escreva o e-mail do contato: ")
    try:
        agenda = open("agenda.txt", "a")
        dados = f'{idContato};{nome};{telefone};{email} \n'
        agenda.write(dados)
        agenda.close()
        print(f'Contato inserido com sucesso !')
    except:
        print("ERRO na gravação do contato")


def listarContato():
    print(f'Listar contato')
    agenda = open("agenda.txt", "r")
    for contato in agenda:
        print(contato)
    agenda.close


def deletarContato():
    nomeDeletado = input(f'Digite o nome para ser deletado: ').lower()
    agenda = open("agenda.txt", "r")
    aux = []
    aux2 = []
    for i in agenda:
        aux.append(i)
    for i in range(0, len(aux)):
        if nomeDeletado not in aux[i].lower():
            aux2.append(aux[i])
    agenda = open("agenda.txt", "w")
    for i in aux2:
        agenda.write(i)
    print(f'Contato deletado com sucesso.')
    listarContato()


def buscarContatoPeloNome():
    nome = input(f'Digite um nome a ser procurado: ').upper()
    print(f'Buscar contato')
    agenda = open("agenda.txt", "r")
    for contato in agenda:
        if nome in contato.split(";")[1].upper():
            print(contato)
    agenda.close


def sair():
    exit()


def main():

    menu()


main()
