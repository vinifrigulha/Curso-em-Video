print('=-='*6)
print('TABUADA INFINITA')
print('=-='*6)
while True:
    print('Insira um número \033[32mPOSITIVO\033[m para saber a tabuada \nou um número \033[31mNEGATIVO\033[m para encerrar')
    print('*' * 50)
    n = int(input('Número: '))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('*'*50)
print('\033[33mPROGRAMA ENCERRADO')