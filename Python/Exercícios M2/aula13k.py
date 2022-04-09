soma = 0
maior = 0
velho = ''
cont = 0
for p in range(1, 5):
    print(f'==== {p}ª PESSOA ====')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').upper()
    soma += idade
    if sexo == 'M':
        if p == 1:
            maior = idade
            velho = nome
        else:
            if idade > maior:
                maior = idade
                velho = nome
    if sexo == 'F':
        if idade < 20:
            cont += 1
media = soma/4
print(f'A média da idade do grupo é {media} anos.')
print(f'O homem mais velho se chama {velho} e ele tem {maior} anos.')
print(f'Temos {cont} mulheres com menos de 20 anos.')
