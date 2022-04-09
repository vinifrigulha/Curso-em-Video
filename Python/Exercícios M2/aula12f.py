from datetime import date
ano = int(input('Ano de nascimento: '))
idade = date.today().year - ano
print(f'O atleta tem {idade} anos.')
if idade <=9:
    print('Cassificação: MIRIM.')
elif idade <= 14:
    print('Cassificação: INFANTIL.')
elif idade <= 19:
    print('Cassificação: JÚNIOR')
elif idade <= 25:
    print('Cassificação: SÊNIOR.')
else:
    print('Cassificação: MASTER.')
