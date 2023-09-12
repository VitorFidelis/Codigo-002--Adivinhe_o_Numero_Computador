import random

def adivinhe(numero_secreto):
    number_random = random.randint(1, numero_secreto)
    adivinhe = 0
    while adivinhe != number_random:
        adivinhe = int(input(f'> Escolha um número de 1 a {numero_secreto}:'))
        if adivinhe < number_random:
            # print("")
            print("Tente novamente! O número escolhido é menor que o número secreto.")
            # print("")
        elif adivinhe > number_random:
            # print("")
            print("Eita! Você escolheu um número muito maior do que o número secreto.")
            # print("")
    # print("")        
    print(f'Hey!! parabéns. Você acerto o número secreto[ {number_random}]!!')
