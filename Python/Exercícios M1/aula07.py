d = int(input('Digite quantos dias o carro foi alugado: '))
q = float(input('Digite a distância em quilômetros percorrida nesse período: '))
pd = d*60
pq = q*0.15
print('Logo, o total a se pagar pelo carro alugado é de R$ {:.2f}.'.format(pd+pq))
