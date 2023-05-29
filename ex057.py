s = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]

while s != 'M' and s != 'F':
    print('Erro! Tente novamente.')
    s = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
print('sexo {} registrado com sucesso'.format(s))
