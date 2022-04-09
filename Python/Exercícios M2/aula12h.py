peso = float(input('Seu peso (kg): '))
altura = float(input('Sua altura (m): '))
imc = peso/(altura**2)
print(f'Seu IMC é \033[1;30;107m{imc:.1f}\033[m!')
if imc < 18.5:
    print('Você está \033[1;33mABAIXO DO PESO\033[m.')
elif imc < 25:
    print('Você está com o \033[1;33mPESO IDEAL\033[m.')
elif imc < 30:
    print('Você está com \033[1;33mSOBREPESO\033[m.')
elif imc < 40:
    print('Você está com \033[1;33mOBESIDADE\033[m.')
else:
    print('Você está com \033[1;33mOBESIDADE MÓRBIDA\033[m.')
