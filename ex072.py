extenso = 'zero', 'um', 'dois', 'três', 'quatro', 'cinto', 'seis', 'sete', 'oito', \
          'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', '' \
           'dezessete', 'dezoito', 'dezenove', 'vinte'

while True:
    ler = int(input('Digite APENAS UM número entre 0 e 20: '))
    if 0 <= ler <= 20:
        print(extenso[ler])
        break
    else:
        print('O número deve estar entre 0 e 20. Tente Novamente.')