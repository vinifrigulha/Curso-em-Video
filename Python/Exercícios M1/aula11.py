nome = 'Vinícius'
cores = {'limpa':'\033[m',
         'vermelho':'\033[31m',
         'preto e branco':'\033[30;107m', 'fundopreto':'\033[40m'}
print('Olá, prazer em te conhecer {}{}{}!!'.format(cores['vermelho'], nome, cores['limpa']))
