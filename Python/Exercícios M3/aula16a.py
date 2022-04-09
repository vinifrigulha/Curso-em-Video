# Resolução finita
tupla = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', \
        'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', \
        'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
num = int(input('Digite um número de 0 a 20: '))
while num < 0 or num > 20:
    num = int(input('Tente novamente. Digite um número entre 0 e 20: '))
print(f'Você digitou o número {tupla[num]}.')

# Resolução com repetição
tupla = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', \
        'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', \
        'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        print(f'Você digitou o número {tupla[num]}.')
        c = input('Quer continuar? [S/N]: ').strip().upper()
        while c not in 'SN':
            print('Opção inválida. ', end = '')
            c = input('Quer continuar? [S/N]: ').strip().upper()
        if c == 'N':
            break
    else:
        print('Tente novamente. ', end = '')
print('Fim da apresentação!')
