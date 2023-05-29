import time

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
opcao = 0

while opcao != 5:
    print('''[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa''')
    opcao = int(input('Qual a sua opção? '))
    if opcao == 1:
        print('A soma de {} e {} é {}'.format(n1, n2, n1 + n2))
    elif opcao == 2:
        print('{} multiplicado por {} é {}'.format(n1, n2, n1 * n2))
    elif opcao == 3:
        if n1 > n2:
            print('{} é maior que {}'.format(n1, n2))
        else:
            print('{} é maior que {}'.format(n2, n1))
    elif opcao == 4:
        print('Informe os números novamente.')
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
    elif opcao == 5:
        print('Finalizando...')
        time.sleep(3)
    else:
        print('Opção invalida! Tente novamente.')
    print('=-=' * 10)

print('Fim do programa, volte sempre!')
