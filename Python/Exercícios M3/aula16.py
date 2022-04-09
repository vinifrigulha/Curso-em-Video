lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
for comida in lanche:
      print(f'Eu vou comer {comida}')

for cont in range(0, len(lanche)):
      print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
      print(f'Eu vou comer {comida} na posição {pos}')

print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c1 = a + b
c2 = b + a
print(c1)
print(c2)
print(len(c1))
print(c1.count(5))
print(c2.index(8))

pessoa = ('Vinicius', 22, 'M', 78.5)
del(pessoa)