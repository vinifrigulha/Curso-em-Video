import math
ang = float(input('Digite o valor do ângulo em graus: '))
s = math.sin(math.radians(ang))
c = math.cos(math.radians(ang))
t = math.tan(math.radians(ang))
print('''O ângulo {} tem as seguintes medidas trignométricas:
seno = {:.2f},
cosseno = {:.2f}, e
tangente = {:.2f}'''.format(ang, s, c, t))

