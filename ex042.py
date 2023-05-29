s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos acima podem formar um triângulo ', end='')
    if s1 == s2 == s3:
        print('equilátero.')
    if s1 != s2 != s3 != s1:
        print('escaleno')
    else:
        print('isósceles')
else:
    print('Os segmentos acima não podem formar um triângulo')