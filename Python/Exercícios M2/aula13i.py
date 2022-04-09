from datetime import date
maior = 0
menor = 0
for a in range(1, 8):
    ano = int(input(f'Ano de nascimento da {a}ª pessoa: '))
    if date.today().year - ano < 21:
        menor += 1
    else:
        maior += 1
print(f'A quantidade de menores de idade é {menor}.')
print(f'E a quantidade de maiores de idade é {maior}.')
