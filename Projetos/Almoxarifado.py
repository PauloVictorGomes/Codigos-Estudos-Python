from time import sleep

#Funções usadas no manoseio do arquivo


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')    #read / ler arquivo
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') #criando arquivo caso nao exista
        a.close()
    except:
        print('Erro ao criar o arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso')


def lerArquivo(arq):
    try:
        a = open(arq, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabeçalho('LISTA DE PRODUTOS')
        print(f'{"Cód.":<5}{"Nome".center(15)}{"Valor(R$)":>10}')
        print('-' * 40)
        for linha in a:
            dado = linha.split(';')#Dado aqui é uma lista, onde eu dividi/separei onde tem ;
            print(f'{dado[0]:<5}|{dado[1].center(15)}|{dado[2]:>8}', end='')
            print('-' * 4,'+', '-' *13, '+', '-' * 10)

    sleep(1.5)
    print()

def cadastrar(arq, cod, nome='vazio', val=0):
    try:
        a = open(arq, 'at') #a = append, ou seja acrescentar
    except:
        print('Ocorrce um erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{cod};{nome};{val}\n')
        except:
            print('Ocorreu um ERRO na hora de escrever os dados.')
        else:
            print('...gravando dados...')
            sleep(1.5)
            print(f'\nItem "{nome.upper()}" cadastrado com sucesso !!!')

#Funções usadas no programa principal


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


def leiaFloat(msg):
    while True:
        try:
            num = float(input(msg))
        except (TypeError, ValueError):
            print('\033[0;31mErro! Digite um número Real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mO usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return num


def cabeçalho(txt):
    print('~' * 40)
    print(f'{txt.center(40)}')
    print('~' * 40)


def menu(lista):
    cabeçalho('MENU PRINCIAPAL')
    for c, v in enumerate(lista):
        print(f'{c+1}- {v}')
    #sleep(1)
    opc = leiaInt('\nOpção escolhida: ')
    return opc



arq = 'cadastroAlmoxarifado.txt'

if arquivoExiste(arq):
    print(f'Arquivo {arq} encontrado com sucesso!')
    print('Arquivo aberto\n\n')
else:
    print('Arquivo não encontrado, criando arquivo...\n')
    criarArquivo(arq)

#PROGRMA PRINCIPAL
while True:    #Só sai do loop se digitar alguma string com 'n' no inicio
    opc = menu(['Cadastrar Produto', 'Lista de cadastro','Sair do programa'])
    if opc == 1:
        #Opção para cadastrar novo produto
        cabeçalho('NOVO CADASTRO')
        cod = leiaInt('Digite o código do produto: ')
        nome = str(input('Digite o nome do produto: '))
        val = leiaFloat('Digite o valor do produto: ')
        cadastrar(arq, cod, nome, val)
        #implementar opção para nao cadastrar produto repetidos
          #else:
          #  print('Tente novamente.Já existe esse código!')
    elif opc == 2:
        #implementar meto de organização do produtos
        lerArquivo(arq)
    elif opc == 3:
        cabeçalho('Saindo do sistema')
        print('Ate logo...')
        break
    else:
        print('\nErro, opção inválida!!!\n')
