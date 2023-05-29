from random import randint
numeros = randint(1, 10), randint(1, 10), randint(1, 10), \
randint(1, 10), randint(1, 10)

for e in numeros:
    print(f'{e} ', end='')

print(f'\n{min(numeros)}')
print(max(numeros))