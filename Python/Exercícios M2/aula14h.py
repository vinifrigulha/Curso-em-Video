num = int(input('Digite um número [999 para parar]: '))
cont = soma = 0
while num != 999:
    cont += 1
    soma += num
    num = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {cont} números e a soma entre eles é {soma}.')