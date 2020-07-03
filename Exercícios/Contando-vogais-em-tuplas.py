words = ('pessoa', 'joga', 'computador', 'corrida', 'comida','gratis', 'futuro', 'programar')
vogais = 'aeiou'

for w in words:     #W será cada palavra da TUPLA words
    print(f'\nNa palavra {w.upper()} temos ', end='')
    for l in w:     #L será cada letra da palavra na variável W
        if l.lower() in vogais:  #Se em L tivermos alguma vogal
            print(l, end=' ')   # será exibido na tela a vogal