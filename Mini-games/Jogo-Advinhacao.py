from random import randint
from time import sleep
resp = randint(0, 10) #número que devemos adivinhar, de 0 a 10
tent = 1 #variavel para contar as tentaivas, já começa em um pois só é contado novamente depois de o usuário errar

print('\n----- JOGO DE ADIVINHAÇÃO v2.0 -----')
print('\nPensei em um número inteiro, tente adivinha-lo.')
print('Aqui vai uma dica, é de 0 a 10. Pense bem!')
sleep(2)
num = int(input('Qual número você acha que é? '))#usuário entrar com um número para ver se é o mesmo que foi randomizado

while num != resp: #Laço para ver se 'adivinhamos' o número
    if num < resp:  #Dando dica que a resposta é um Nº maior 
        print('\nMais...')  
    if num > resp:  #Dando dica que a resposta é um Nº menor
        print('\nMenos...')
    num = int(input('Tente Novamente. Qual você acha que é? '))
    tent += 1 #aumentando a variável de Nº de tentativas

print(f'\nParabéns, VOCÊ ACERTOU eu escolhi o número {resp}')
print(f'Você acertou na {tent}ª tentativa!')
