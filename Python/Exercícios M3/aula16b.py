tabela = 'Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', \
         'Fluminense', 'América-MG', 'Atlético-GO', 'Santos', 'Ceará SC', 'Internacional', \
         'São Paulo', 'Athletico-PR', 'Cuiabá', 'Juventude', 'Grêmio', 'Bahia', 'Sport Recife', 'Chapecoense'
print('=-='*20)
print(f'Os times são {tabela}.')
print('=-='*20)
print(f'Os 5 primeiros colocados foram: {tabela[0:5]}')
print('=-='*20)
print(f'Os quatro últimos colocados foram: {tabela[-4:]}')
print('=-='*20)
print(f'Em ordem alfabética temos os times organizados em: \n{sorted(tabela)}')
print('=-='*20)
print(f'A Chapecoense está na {tabela.index("Chapecoense")+1}ª colocação.')
print('=-='*20)
