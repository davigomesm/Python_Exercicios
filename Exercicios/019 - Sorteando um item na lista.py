import random
a1 = input("Digite o nome do primeiro aluno: ")
a2 = input("digite o nome do segundo aluno: ")
a3 = input("digite o nome do terceiro aluno: ")
a4 = input("digite o nome do quarto aluno: ")
lista = [a1, a2, a3, a4]
alunosort = random.choice(lista)
print("o aluno sorteado é {}".format(alunosort))
