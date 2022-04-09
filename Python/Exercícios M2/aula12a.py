casa = float(input('Valor da casa: R$ '))
salario = float(input('Valor do salário: R$ '))
anos = int(input('Em quantos anos: '))
parcela = (casa) / (anos * 12)
if parcela > 0.3 * salario:
    print('Infelizmente será inviável realizar um empréstimo, pois cada parcela custará \033[31mR$ {:.2f}\033[m ao mês.'.format(parcela))
else:
    print('Tudo bem! O seu empréstimo foi aprovado! A sua prestação será de \033[1;32;107mR$ {:.2f}\033[m por mês.'.format(parcela))
