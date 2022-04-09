frase = input('Escreva uma palavra/frase: ').lower().replace('à', 'a').replace('á', 'a').replace(' ', '').strip()
print('A sua palavra/frase tem {} letras "A"!!'.format(frase.count('a')))
print('A letra "A" apareceu pela primeira vez na posição {}'.format(frase.find('a')+1))
print('e pela última vez na posição {}!'.format(frase.rfind('a')+1))
