from unidecode import unidecode
frase = input('Digite um frase: ').strip().upper()
frasej = unidecode(frase.replace(' ', ''))
inverso = ''
for letras in range(len(frasej)-1, -1, -1):
    inverso += frasej[letras]
print(f'A frase {frase} ao contrário é {inverso}.')
if frasej == inverso:
    print('A frase digitada é um palíndromo.')
else:
    print('A frase digitada não é um palíndromo.')