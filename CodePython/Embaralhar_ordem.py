import random
a1 = input("Digite o nome da primeira pessoa: ")
a2 = input("digite o nome da segunda pessoa: ")
a3 = input("digite o nome da terceira pessoa: ")
a4 = input("digite o nome da quarta pessoa: ")
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print("A nova ordem é: ")
print(lista)
