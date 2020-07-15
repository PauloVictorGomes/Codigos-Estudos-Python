turma = []
pessoa = {}
mediaIdade = somaIdade = 0
while True:
    print('-' * 30)
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
    while pessoa['sexo'] not in 'MF':
        print('\nERRO! Por favor digite somente M ou F\n ')
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
    pessoa['idade'] = int(input('Idade: '))
    #variável com soma das idades
    somaIdade += pessoa['idade']
    #copiando o dicionário na lista
    turma.append(pessoa.copy())
    op = str(input('Deseja continuar? [S/N] ')).upper()[0]
    while op not in 'SN':
        op = str(input('\nERRO! Por favor, digite S ou N: ')).upper()[0]
    if op in 'N':
        break
print(f'\n {turma}')
print(f'\nA - Foram cadastradas {len(turma)} pessoa(s).')
mediaIdade = somaIdade / len(turma)
print(f'B - Média de idade: {mediaIdade:5.2f} anos.')
print(f'C - As mulheres cadastradas foram: ', end= ' ')
for p in turma:
    for k, v in p.items():
        if v == 'F':
            print(f'{p["nome"]} ', end= ' ')
print(f'\nD - Lista com pessoas a cima da média: ')
for p in turma:
    if p['idade'] >= mediaIdade:
        print('    ')
        for k, v in p.items():
            print(f'    {k} = {v};', end= ' ')
print('\n>>>>ENCERRADO<<<<')
