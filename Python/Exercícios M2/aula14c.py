from time import sleep
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
p = 0
while p != 5:
    print('[ 1 ] somar \n[ 2 ] multiplicar \n[ 3 ] maior \n[ 4 ] novos números \n[ 5 ] sair do programa')
    p = int(input('Digite a operação desejada: '))
    if p == 1:
        print(f'A soma {n1} + {n2} = {n1+n2}.')
    elif p == 2:
        print(f'O produto {n1} * {n2} = {n1*n2}.')
    elif p == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}.')
        elif n1 < n2:
            print(f'{n2} é maior que {n1}.')
        else:
            print('Os dois números digitados são iguais.')
    elif p == 4:
        n1 = int(input('Digite um novo número: '))
        n2 = int(input('Digite um outro numero: '))
        print('Computando os novos dados...')
    elif p == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
    sleep(2)
    print('=-='*17)
print('Obrigado por usar o nosso programa! :)')
