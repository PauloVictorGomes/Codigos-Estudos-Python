listnum = []  # Criando lista
op = ' '  # Criando string vazia
print('-=' * 15)
while op not in 'N':    
    num = int(input('Digite um código: '))
    if num not in listnum:
        listnum.append(num)
        print('Código adicionado\n')
    else:
        print('Tente novamente.Já existe esse código!')

    op = input('Deseja continuar?[S/N] ').strip().upper()[0]

print('-=' * 15)
listnum.sort(reverse = True)
print(f'Códigos inseridos {listnum}')
print('-=' * 15)