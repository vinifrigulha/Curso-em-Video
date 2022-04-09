v = float(input('Qual a sua velocidade? '))
if v > 80:
    print('Você foi multado! Pague já R$ {:.2f}!'.format((v-80)*7))
else:
    print('Muito bem! Continue dentro do limite de velocidade!')
