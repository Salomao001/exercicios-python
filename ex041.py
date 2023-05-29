from datetime import datetime
now = datetime.now()
nasc = int(input('Digite seu ano de nascimento: '))
idade = now.year - nasc
if idade <= 9:
    print('Categoria MIRIM')
elif idade > 9 and idade <= 14:
    print('Categoria INFANTIL')
elif idade > 14 and idade <= 19:
    print('Categoria JUNIOR')
elif idade > 19 and idade <= 20:
    print('Categoria SÊNIOR')
else:
    print('Categoria MASTER')
