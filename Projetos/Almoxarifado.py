from time import sleep


def leiaInt(msg):
    """
    ->Função semelhante o print, porém com tratamento de erro. Lê um número inteiro, caso o usuário não entre com
     um númeor inteiro irá aparecer um erro, e será pedido novamente um número válido.
    :param msg: mensagem que será exibida, por exemplo:"Sua escolha: "
    :return: retorna ao numero da opção
    """
    while True:
        try:
            num = int(input(msg))
            break
        except (TypeError, ValueError):
            print('\033[0;31mErro! Digite um número Inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            num = 0
            print('\033[0;31mUsuário preferiu não digitar esse número.\033[m')
            return 0
    return num


def cabeçalho(txt):
    print('-' * 30)
    print(f'{txt.center(30)}')
    print('-' * 30)


def menu(lista):
    cabeçalho('MENU PRINCIAPAL')
    for c, v in enumerate(lista):
        print(f'{c+1}- {v}')
    #sleep(1)
    opc = leiaInt('\nOpção escolhida: ')
    return opc


#PROGRMA PRINCIPAL
listnum = []  # Criando lista
op = ' '  # Criando string vazia

while True:    #Só sai do loop se digitar alguma string com 'n' no inicio
    opc = menu(['Cadastrar Produto', 'Lista de cadastro','Sair do programa'])
    if opc == 1:
        cod = leiaInt('Digite o código do produto: ')
        if cod not in listnum:
            listnum.append(cod)
            print('Código adicionado\n')
        else:
            print('Tente novamente.Já existe esse código!')
    elif opc == 2:
        cabeçalho('Exibindo lista de produtos')
        listnum.sort
        print(f'Códigos inseridos {listnum}')
    elif opc == 3:
        cabeçalho('Saindo do sistema')
        sleep(0.5)
        print('Ate logo...')
        break
    else:
        print('\nErro, opção inválida!!!\n')
