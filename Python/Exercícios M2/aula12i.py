print('{:=^40}'.format(' LOJAS FRIGULHINHA '))
preco = float(input('Preço do produto: R$ '))
print('''Forma de pagamento:
[ 1 ] para à vista no dinheiro;
[ 2 ] para cartão à vista;
[ 3 ] para parcelar em 2x;
[ 4 ] para parcelar em 3x ou mais.''')
pagamento = int(input('Digite: '))
if pagamento == 1:
    print(f'O seu produto de R$ {preco:.2f} custará R$ {preco*0.9:.2f} com essa opção.')
elif pagamento == 2:
    print(f'O seu produto de R$ {preco:.2f} custará R$ {preco*0.95:.2f} com essa opção.')
elif pagamento == 3:
    print(f'O seu produto de R$ {preco:.2f} custará R$ {preco:.2f} com essa opção.')
elif pagamento == 4:
    parcela = int(input('Digite a quantidade de parcelas: '))
    print(f'Sua compra de R$ {preco:.2f} será parcelada em {parcela}x de R$ {(preco*1.2)/parcela:.2f}')
    print(f'Custará, então, R$ {preco*1.2:.2f} com essa opção.')
else:
    print('\033[31mOpção inválida de pagamento. Tente novamente.\033[m')
