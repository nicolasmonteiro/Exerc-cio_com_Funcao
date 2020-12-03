'''
2-Faça o código que tenha a função que recebe três parâmetros inicio,
fim e passo e faz a contagens Seu programa realiza três contagens
através da função criada
a-De 1 até 10 de 1 em 1
b-De 10 até 0 de 2 em 2
c-Um contagem personalizada
'''


def cont(inicio, fim, passo):
    print(f'Contagem de {inicio} até {fim} passo {passo}')
    for n in range(inicio, fim, passo):
        print(n)
    print('-'*30)


cont(1, 10, 1)
cont(10, 0, -2)


print('Contagem particularizada')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
cont(i, f, p)
