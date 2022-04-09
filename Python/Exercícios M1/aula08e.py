from random import shuffle
p1 = str(input('Primeira pessoa: '))
p2 = str(input('Segunda pessoa: '))
p3 = str(input('Terceira pessoa: '))
p4 = str(input('Quarta pessoa: '))
lista = [p1, p2, p3, p4]
shuffle(lista)
print('A ordem de apresentação dos trabalhos será: {}'.format(lista))
