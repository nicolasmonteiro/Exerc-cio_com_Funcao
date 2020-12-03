import random


def jogadores():
    print('-'*15, '-Bem vindo ao Jokenpo', '-'*15)
    print('           0- Pedra 1- Papel 2- Tesoura\n')
    jogador1 = int(input('Jogador 1, escolha o número correspondente: '))
    jogador_comp = random.randint(0, 2)
    return jogador1, jogador_comp


def jogo():
    jog1, jog_comp = jogadores()
    opcoes = ['pedra', 'papel', 'tesoura']
    if(jog1 == jog_comp):
        return 'Empate, Jogador1: ' + opcoes[jog1] + ' computador: ' + opcoes[jog_comp]
    if((jog1 == 0 and jog_comp == 1) or
       (jog_comp == 0 and jog1 == 1)):
        return 'O papel Venceu!' + 'Jogador 1: ' + opcoes[jog1] + ' computador: ' + opcoes[jog_comp]
    elif((jog1 == 0 and jog_comp == 2) or
         (jog_comp == 0 and jog1 == 2)):
        return 'A Pedra Venceu!' + 'Jogador 1: ' + opcoes[jog1] + ' computador: ' + opcoes[jog_comp]
    elif((jog1 == 2 and jog_comp == 1) or
         (jog_comp == 2 and jog1 == 1)):
        return 'A Tesoura Venceu!' + 'Jogador 1: ' + opcoes[jog1] + ' computador: ' + opcoes[jog_comp]


print(jogo())
print('-'*15, 'Fim de jogo', '-'*15)
