num = soma = cont = maior = menor = 0
r = 'S'
while r == 'S':
    num = int(input('Digite um número: '))
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = menor
        if num < menor:
            menor = num
    soma += num
    cont += 1
    r = input('Quer continuar? [S/N]: ').upper()
print(f'Você digitou {cont} números e a média entre eles é {soma/cont:.2f}.')
print(f'O maior número é {maior} e o menor número {menor}.')