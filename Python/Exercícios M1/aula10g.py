sal = float(input('Qual o seu salário? '))
if sal > 1250:
    print('Você receberá um reajuste de 10%, logo seu novo salário será de R$ {:.2f}'.format(sal*1.1))
else:
    print('Você receberá um reajuste de 15%, logo seu novo salário será de R$ {:.2f}'.format(sal*1.15))
