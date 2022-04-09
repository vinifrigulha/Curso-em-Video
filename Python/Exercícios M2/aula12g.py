l1 = float(input('Primeiro segmento: '))
l2 = float(input('Segundo segmento: '))
l3 = float(input('Terceiro segmento: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os segmentos PODEM FORMAR um triângulo!')
    if l1 == l2 == l3:
        print('Ele será EQUILÁTERO.')
    elif l1 != l2 != l3 != l1:
        print('Ele será ESCALENO.')
    else:
        print('Ele será ISÓSCELES.')
else:
    print('Os lados NÃO PODEM FORMAR um triângulo com essas medidas.')
