n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2)/2
if m < 5:
    print('Sua média foi {:.2f}! Você está REPROVADO.'.format(m))
elif m < 7:
    print('Sua média foi {:.2f}! Você está em RECUPERAÇÃO.'.format(m))
else:
    print('PARABÉNS! Sua média foi {:.2f}! Você está APROVADO!'.format(m))
