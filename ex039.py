from datetime import datetime
nasc = int(input('Digite seu ano de nascimento: '))
now = datetime.now()
idade = now.year - nasc
if idade == 18:
    print('Esta na hora de se alistar.')
elif idade > 18:
    print('ja passou o prazo de alistamento.')
    print('se passaram {} anos desde o alistamento.'.format(idade - 18))
else:
    print('ainda vai chegar a hora do alistamento')
    print('faltam {} anos para o alistamento'.format(18 - idade))
