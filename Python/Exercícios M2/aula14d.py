from math import factorial
num = int(input('Informe um número: '))
fat = factorial(num)
p = num
print(f'{num}! = ', end ='')
while p > 0:
    print(f'{p}', end = '')
    print(' x ' if p > 1 else ' = ', end = '')
    p -= 1
print(fat)
