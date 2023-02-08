from random import randint
from time import sleep

print('-'*40)
print('Vamos jogar Jokenpô!')
print('-'*40)

#Escolhendo a modalidade do jogo.
print('''Modalidades: 
|0| = Humano     X Humano 
|1| = Humano     x Computador 
|2| = Computador x Computador ''')
modalidade = int(input('Qual modalidade você quer jogar? '))
print('-'*40)

placar1 = 0
placar2 = 0

while True:
    itens = ('Pedra', 'Papel', 'Tesoura')


    #HUMANO X HUMANO

    if modalidade == 0:
        print('|Jogador Número 1|')
        print('''Suas opções são: 
        |0| = Pedra
        |1| = Papel
        |2| = Tesoura ''')
        jogador1 = int(input("Qual é a sua jogada? "))
        print('-' * 40)

        print('|Jogador Número 2|')
        print('''Suas opções são: 
        |0| = Pedra
        |1| = Papel
        |2| = Tesoura ''')
        jogador2 = int(input("Qual é a sua jogada? "))
        print('-' * 40)

        print('JO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PÔ!!!')
        print('-' * 40)

        print('Jogador número 1 jogou {}'.format(itens[jogador1]))
        print('Jogador número 2 jogou {}'.format(itens[jogador2]))
        print('-' * 40)

        # Descrevendo as regras do jogo.
        if jogador1 == 0:  # Jogador 1 jogou pedra
            if jogador2 == 0:
                print('Empate!')
            elif jogador2 == 1:
                print('Jogador 2 Vence!')
                placar2 = placar2 + 1
            elif jogador2 == 2:
                print('Jogador 1 Vence!')
                placar1 = placar1 + 1
            else:
                print('Jogada inválida!')
        elif jogador1 == 1:  # Jogador 1 jogou papel
            if jogador2 == 0:
                print('Jogador 1 Vence!')
                placar1 = placar1 + 1
            elif jogador2 == 1:
                print('Empate!')
            elif jogador2 == 2:
                print('Jogador 2 Vence!')
                placar2 = placar2 + 1
            else:
                print('Jogada inválida!')
        elif jogador1 == 2:  # Jogador 1 jogou tesoura
            if jogador2 == 0:
                print('Jogador 2 Vence!')
                placar2 = placar2 + 1
            elif jogador2 == 1:
                print('Jogador 1 Vence!')
                placar1 = placar1 + 1
            elif jogador2 == 2:
                placar2 = placar2 + 1
                print('Empate!')
            else:
                print('Jogada inválida!')

        print('O placar é: ')
        print('Jogador 1: ', placar1)
        print('Jogador 2: ', placar2)


    #HUMANO X COMPUTADOR

    if modalidade == 1:
        computador = randint(0, 2)

        print('''Suas opções são: 
        |0| = Pedra
        |1| = Papel
        |2| = Tesoura ''')
        jogador = int(input("Qual é a sua jogada? "))
        print('-'*40)

        print('JO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PÔ!!!')
        print('-'*40)

        print('O computador jogou {}'.format(itens[computador]))
        print('Jogador jogou {}'.format(itens[jogador]))
        print('-'*40)

        # Descrevendo as regras do jogo.
        if computador == 0: #computador jogou pedra
            if jogador == 0:
                print('Empate!')
            elif jogador == 1:
                print('Jogador Vence!')
                placar1 = placar1 + 1
            elif jogador == 2:
                print('Computador Vence!')
                placar2 = placar2 + 1
            else:
                print('Jogada inválida!')
        elif computador == 1: #computador jogou papel
            if jogador == 0:
                print('Computador Vence!')
                placar2 = placar2 + 1
            elif jogador == 1:
                print('Empate!')
            elif jogador == 2:
                print('Jogador Vence!')
                placar1 = placar1 + 1
            else:
                print('Jogada inválida!')
        elif computador == 2: #computador jogou tesoura
            if jogador == 0:
                print('Jogador Vence!')
                placar1 = placar1 + 1
            elif jogador == 1:
                print('Computador Vence!')
                placar2 = placar2 + 1
            elif jogador == 2:
                print('Empate!')
            else:
                print('Jogada inválida!')

        print('O placar é: ')
        print('Humano: ', placar1)
        print('Computador: ', placar2)


    #COMPUTADOR X COMPUTADOR

    if modalidade == 2:
        computador1 = randint(0, 2)
        computador2 = randint(0, 2)

        print('JO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PÔ!!!')
        print('-'*40)

        print('O computador 1 jogou {}'.format(itens[computador1]))
        print('O computador 2 jogou {}'.format(itens[computador2]))
        print('-' * 40)

        # Descrevendo as regras do jogo.
        if computador1 == 0:  # computador 1 jogou pedra
            if computador2 == 0:
                print('Empate!')
            elif computador2 == 1:
                print('Computador 2 Vence!')
                placar2 = placar2 + 1
            elif computador2 == 2:
                print('Computador 1 Vence!')
                placar1 = placar1 + 1
            else:
                print('Jogada inválida!')
        elif computador1 == 1:  # computador 1 jogou papel
            if computador2 == 0:
                print('Computador 1 Vence!')
                placar1 = placar1 + 1
            elif computador2 == 1:
                print('Empate!')
            elif computador2 == 2:
                print('Computador 2 Vence!')
                placar2 = placar2 + 1
            else:
                print('Jogada inválida!')
        elif computador1 == 2:  # computador 1 jogou tesoura
            if computador2 == 0:
                print('Computador 2 Vence!')
                placar2 = placar2 + 1
            elif computador2 == 1:
                print('Computador 1 Vence!')
                placar1 = placar1 + 1
            elif computador2 == 2:
                print('Empate!')
            else:
                print('Jogada inválida!')

        print('O placar é: ')
        print('Computador 1: ', placar1)
        print('Computador 2: ', placar2)


    # Continuar ou sair.
    print('-' * 40)
    partida = int(input('Deseja continuar(0) ou sair(1)? '))
    print('-'*40)

    # Para sair, exibir placar geral e mostrar mensagem de agradecimento com os nomes dos estudantes.
    if partida == 1:
        print('O placar final foi: ', placar1, 'X', placar2)
        print('Obrigada por jogar meu jogo!')
        print('Feito por Luana Tiemann Halicki Cordeiro')
        break

