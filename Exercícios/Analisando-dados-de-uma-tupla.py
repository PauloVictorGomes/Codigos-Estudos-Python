#Entrada dos dados
num = (int(input('Digite um número: ')),
        int(input('Digite outro número: ')),
        int(input('Digite mais um número: ')),
        int(input('Digite o ultimo número: ')))
print(num)
print(f'\nO valor 9 apareceu {num.count(9)} vezes') #número de vezes que o algarismo 9 apareceu
if 3 in num:    #Se tivermos o algarismo 3 na tupla num, será exibido a posição
    print(f'O primeiro 3 está na {num.index(3)+1}ª posição')
else:   #Senão tiver o algarismo 3, será exibido uma mensagem informando 
    print('Não tem nenhum número 3')
print('Números pares : ', end=' ')
for n in num: #Laço para varrer a tupla
    if n % 2 == 0:      #Só será exibido os números com o resto 0 da divisão por 2, ou seja, números pares
        print(f'{n}  ', end='')
