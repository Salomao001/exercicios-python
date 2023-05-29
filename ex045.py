from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
jogador = (input('Qual é a sua jogada? '))
print('O computador escolheu {}'.format(itens[computador]))
if computador == 0 and jogador == 'Papel':
    print('Jogador venceu!')
elif computador == 0 and jogador == 'Tesoura':
    print('Computador venceu!')
elif computador == 0 and jogador == 'Pedra':
    print('Empate!')
elif computador == 1 and jogador == 'Tesoura':
    print('Jogador venceu!')
elif computador == 1 and jogador == 'Pedra':
    print('Computador venceu!')
elif computador == 1 and jogador == 'Papel':
    print('Empate!')
elif computador == 2 and jogador == 'Pedra':
    print('Jogador venceu!')
elif computador == 2 and jogador == 'Papel':
    print('Computador venceu!')
elif computador == 2 and jogador == 'Tesoura':
    print('Empate!')
else:
    print('Jogada inválida. Tente novamente')
