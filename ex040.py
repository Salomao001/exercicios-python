n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print('Sua média é de {}'.format(media))
if media > 4.9 and media < 7:
    print('RECUPERAÇÃO')
elif media < 5:
    print('REPROVADO')
else:
    print('APROVADO')
