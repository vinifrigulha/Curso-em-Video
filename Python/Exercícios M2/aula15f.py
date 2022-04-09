print('=================================')
print('            BANCO VFR            ')
print('=================================')
print('''Cédulas disponíveis para saque: 
R$ 50,00
R$ 20,00
R$ 10,00        
R$  1,00''')
valor = int(input('Valor do saque: R$ '))
total = valor
cedula = 50
totalced = 0
while True:
    if total >= cedula:
        total -= cedula
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} cédulas de R$ {cedula:.2f}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalced = 0
        if total == 0:
            break
print('-*-'*16)
print('Volte sempre ao Banco VFR! Tenho um ótimo dia!')
