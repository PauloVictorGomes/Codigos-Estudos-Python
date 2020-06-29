from random import randint
v = 0 #contador de número de partidas ganhas
while True:
    computador = randint(0,10) #número aleatório de 0 a 10
    print('~' * 30)
    jogador = int(input('Digite um valor: ')) #número escolhido pelo jogador
    total = jogador + computador
    resp = total % 2    #resposta usada para saber se é par ou impar
    op = ' '
    while op not in 'PI': #Laço usado para só aceitar P(par) ou I(impar) como OPção de escolha
        op = str(input('PAR ou ÍMPAR?[P|I]  ')).strip().upper()[0] # retirando espaços e pegando somente a primeira letra
    print(f'Você jogou {jogador} e o computador {computador}. Total de  {total} ',end='') # exibir escolha dos números

    print('\n\nDEU PAR\n' if resp == 0 else '\n\nDEU ÍMPAR\n')#se o RESP estiver com 0, a soma dos valores deu par senão deu ímpar
    if op == 'P': #se P em OP, deu par
        if resp == 0: #Se o resto da divisão  por 2 dos números escolhidos for 0, deu par
            print('Você ganhou\n')
            v += 1  #contador de vitórias
        else:
            print('GAME OVER!')
            break
    elif op == 'I': #se I em OP, deu impar
        if resp == 1:#Se o resto da divisão por 2 dos números escolhidos for 1 , deu impar
            print('Você ganhou!\n')
            v += 1  #contador de vitórias
        else:
            print('GAME OVER!')
            break
print(f'\nVocê ganhou {v} vezes seguidas.')
