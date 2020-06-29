from random import randint
from time import sleep

num_a = randint(0, 5)      # Numero aleatório

print('\nPensei em um número entre 0 e 5!\nDuvido adivinhar.')
num_e = int(input('\nQual número você acha que é? '))         # Numero escolhido
print('Processando...')
sleep(2)
if num_a == num_e:
    print('\nVocê acertou!')
else:
    print('\nVocê errou!')
    print('Eu ecolhi o número {} e você {}'.format(num_a, num_e))