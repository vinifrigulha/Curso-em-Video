print('*'*20)
print('{:^20}'.format('CADASTRO DE CLIENTES'))
print('*'*20)
c1 = c2 = c3 = 0
while True:
    idade = int(input('Qual a sua idade? R: '))
    if idade > 18:
        c1 += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Qual o seu sexo? [\033[34mM\033[m/\033[35mF\033[m]: ').strip().upper()[0]
        if sexo == 'M':
            c2 += 1
        elif sexo == 'F' and idade < 20:
            c3 += 1
    cont = ' '
    while cont not in 'SN':
        cont = input('Quer continuar? [\033[32mS\033[m/\033[31mN\033[m]: ').strip().upper()[0]
    if cont == 'N':
        break
    print('=-='*10)
print('*'*50)
print(f'Maiores de 18 anos: {c1}.')
print(f'Total de homens: {c2}. \nTotal de mulheres com menos de 20 anos: {c3}.')
print('*'*50)
