from random import randint
print('Topa um desafio? Eu estou pensando em um número de 0 a 10. \nConsegue adivinhar?')
jogador = int(input('Digite um número de 0 a 10: '))
computador = randint(0, 10)
cont = 0
while not jogador == computador:
    if jogador > computador:
        print('MENOS... Tente novamente!')
    elif jogador < computador:
        print('MAIS... Tente novamente!')
    jogador = int(input('Digite outro número: '))
    cont += 1
print(f'Parabéns! Você me venceu!! Eu estava pensando no número {computador} mesmo!')
print(f'Você tentou {cont} vezes esse desafio!!')
