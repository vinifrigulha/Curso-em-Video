print('-*-'*10)
print('   SHOPPING DO FRIGULHINHA   ')
print('-*-'*10)
total = c = menor = p =0
barato = ' '
while True:
    item = input('Nome do produto: ')
    preco = float(input('Preço: R$ '))
    total += preco
    p += 1
    if preco > 1000:
        c += 1
    if p == 1 or preco < menor:
        menor = preco
        barato = item
    cont = ' '
    while cont not in 'SN':
        cont = input('Deseja comprar mais alguma coisa? [S/N]: ').strip().upper()[0]
    if cont == 'N':
        break
    print('^'*40)
print('{:-^30}'.format('FIM DAS COMPRAS'))
print(f'O total gasto na compra foi de R$ {total:.2f}.')
print(f'Você adquiriu {c} produtos acima de R$ 1.000,00.')
print(f'E o item mais barato foi {barato}')
