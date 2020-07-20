def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    fat = 1
    for c in range(n, 0, -1):
        fat *= c
        if show == True:
            if c >= 2:
                print(c, end=' x ')
            else:
                print(c, end=' = ')
    return fat


#Programa principal
print(fatorial(5, True))
print('-=' * 20)
help(fatorial)
