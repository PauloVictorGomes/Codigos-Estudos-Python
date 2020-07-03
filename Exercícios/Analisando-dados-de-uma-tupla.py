num = (int(input('Digite um número: ')),
        int(input('Digite outro número: ')),
        int(input('Digite mais um número: ')),
        int(input('Digite o ultimo número: ')))
print(num)
print(f'\nO valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O primeiro 3 está na {num.index(3)+1}ª posição')
else:
    print('Não tem nenhum número 3')
print('Números pares : ', end=' ')
for n in num:
    if n % 2 == 0:
        print(f'{n}  ', end='')