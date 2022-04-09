from time import sleep
num = int(input('Digite o seu número: '))
print('\033[33mPROCESSANDO...\033[m')
sleep(2)
print('''Escolha a base numérica:
 [ \033[34m1\033[m ] para \033[34mBINÁRIO\033[m;
 [ \033[31m2\033[m ] para \033[31mOCTAL\033[m; ou
 [ \033[97m3\033[m ] para \033[97mHEXADECIMAL\033[m.''')
opt = int(input('Digite aqui: '))
print('\033[33mPROCESSANDO...\033[m')
sleep(2)
if opt == 1:
    print(f'O número {num} na base binária é {num:b}.')
elif opt == 2:
    print(f'O número {num} na base octagonal é {num:o}.')
elif opt == 3:
    print(f'O número {num} na base hexadecimal é {num:x}.')
else:
    print('Opção inválida. Favor reiniciar o processo.')
