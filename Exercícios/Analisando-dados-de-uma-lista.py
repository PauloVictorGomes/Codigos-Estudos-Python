galera = list()
dado = list()
print('=-' * 20)
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    if len(galera) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        elif dado[1] < menor:
            menor = dado[1]
    galera.append(dado[:])
    dado.clear()
    op = str(input('Deseja continuar?[S/N] ')).strip()
    if op in 'Nn':
        break
print('=-' * 20)
print(f'\nForam cadastradas {len(galera)} pessoas')
print(f'O maior peso foi de {maior}Kg. Peso de ', end=' ')
for p in galera:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print(f'\nO menor peso foi de {menor}Kg. Peso de ', end=' ')
for p in galera:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')