import random
a1 = input("Digite o nome da primeira pessoa: ")
a2 = input("digite o nome da segunda pessoa: ")
a3 = input("digite o nome da terceira pessoa: ")
a4 = input("digite o nome da quarta pessoa: ")
lista = [a1, a2, a3, a4]
alunosort = random.choice(lista)
print("A pessoa sorteada é {}".format(alunosort))
