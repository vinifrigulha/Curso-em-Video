sexo = input('Informe o seu sexo [M/F]: ').strip().upper()
while sexo not in 'MmFf':
    sexo = input('Dados inválidos. Por favor, informe o seu sexo [M/F]: ').upper()
print(f'Sexo {sexo} registrado com sucesso.')
