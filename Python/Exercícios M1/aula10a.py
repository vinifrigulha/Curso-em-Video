from random import randint
from time import sleep
comp = randint(0, 5)
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
num = int(input('Em qual número estou pensando? '))
print('PROCESSANDO...')
sleep(2.5)
if num == comp:
    print('PARABÉNS! Você adivinhou o número que estou pensando!!')
else:
    print('Eu pensei no número {} e não no número {}! Você PERDEU!!'.format(comp, num))
