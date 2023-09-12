import random
from game import adivinhe

nome = ""

print("********************************")
print("Adivinhe o número secreto!!")
print("********************************")


while nome == "":
    # print("")
    nome = input("informe seu nome para jogar: ")


# print("")
print(f"Olá {nome}, vamos iniciar a partida do game [adivinhe o número]!!")
# print("")
print(adivinhe(10))