t = 0
s = 1
cal = t * s

while t >= 0:
    t = int(input('Quer ver a tabuada de qual valor? '))
    if t < 0:
        break
    if t == -0:
        t:.1
    for c in range(1, 11):
        print(f'{t} x {s} = {t * s}')
        s += 1
    s = 1
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
