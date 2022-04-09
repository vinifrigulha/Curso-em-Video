from datetime import date
ano = int(input('O ano que você nasceu: '))
idade = date.today().year - ano
if idade < 18:
    print(f'A sua idade é {idade} anos.')
    print('Ainda não é hora de você se alistar.')
    print(f'O seu alistamento será em {18+ano}')
    if 18 - idade == 1:
        print(f'Ainda falta 1 ano para o seu alistamento!')
    else:
        print(f'Ainda faltam {18-idade} anos para o seu alistamento!')
elif idade == 18:
    print('A sua idade é 18 anos!')
    print('Chegou o momento! Aliste-se IMEDIATAMENTE!')
else:
    print(f'A sua idade é {idade} anos.')
    print(f'Seu alistamento foi em {ano+18}')
