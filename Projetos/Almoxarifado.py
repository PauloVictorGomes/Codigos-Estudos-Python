listnum = []  # Criando lista
op = ' '  # Criando string vazia
print('-=' * 15)
while op not in 'N':    #Só sai do loop se digitar alguma string com 'n' no inicio
    num = int(input('Digite um código: '))
    if num not in listnum:
        listnum.append(num)
        print('Código adicionado\n')
    else:
        print('Tente novamente.Já existe esse código!')

    op = input('Deseja continuar?[S/N] ').strip().upper()[0]#tirando espaços e pegando a 1º letra tornado-a em maiúscula

print('-=' * 15)
listnum.sort
print(f'Códigos inseridos {listnum}')
print('-=' * 15)