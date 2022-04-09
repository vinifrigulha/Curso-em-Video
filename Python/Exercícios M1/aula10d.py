dist = float(input('Qual a distância até o nosso destino? '))
if dist <=200:
    print('É uma viagem relativamente curta! O preço da passagem será R$ {}!'.format(dist*0.5))
else:
    print('É uma viagem longa! O preço da passagem será R$ {}!'.format(dist*0.45))
