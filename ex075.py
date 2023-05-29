n1 = int(input('Digite um valor: '))
n2 = int(input('Outro valor:'))
n3 = int(input('Outro: '))
n4 = int(input('Só mais um: '))
t = n1, n2, n3, n4
print(t)
print(f'O valor 9 apareceu {t.count(9)} vezes')
if 3 in t:
    print(f'O valor 3 apareceu na {t.index(3)} posição pela primeira vez')
print(f'Os valores pares digitados foram ', end='')
for n in t:
    if n % 2 == 0:
        print(n, end=' ')