nome = input('Qual o seu nome? ').strip()
n = nome.split()
print('O seu primeiro nome é {}'.format(n[0]))
print('e o seu último nome é {}'.format(n[len(n)-1]))
