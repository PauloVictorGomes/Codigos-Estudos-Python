from random import randint
def maior(* num):
    print('-=' * 30)
    print('Analisando valores recebidos...')
    maior = 0
    for valor in num:
        print(valor, end=' ')
        # Condicional para pegar o maior número
        if valor > maior:
            maior = valor
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


#Programa Principal
maior(randint(0, 10), randint(0,10), randint(0, 10), randint(0,10), randint(0, 10), randint(0,10))
maior(randint(0, 10), randint(0,10), randint(0, 10))
maior(randint(0, 10), randint(0,10))
maior(randint(0, 10))
maior()
