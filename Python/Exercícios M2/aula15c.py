from random import randint
cont = 0
while True:
    print('='*20)
    print('   PAR OU ÍMPAR??     ')
    print('='*20)
    jogador = int(input('Escolha um número de 0 a 10: '))
    computador = randint(0, 11)
    s = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = input('Escolha PAR ou ÍMPAR [P/I]: ').strip().upper()[0]
    print(f'O jogador jogou {jogador} e o computador {computador}. O total foi {s}.')
    print('Deu PAR' if s % 2 == 0 else 'Deu ÍMPAR')
    if tipo == 'P':
        if s % 2 == 0:
            print('Você VENCEU!')
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if s % 2 == 1:
            print('Você VENCEU!')
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
    cont += 1
print(f'GAME OVER! Você me venceu {cont} vezes!')