#   Exercício Python 084 - Lista composta e análise de dados
#   Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#       A) Quantas pessoas foram cadastradas.
#       B) Uma listagem com as pessoas mais pesadas.
#       C) Uma listagem com as pessoas mais leves.


pessoas = list()
dados = list()
pesados = list()
leves = list()
resp = 0
while True:
    dados.append(str(input("Digite o nome da pessoa: ")))
    dados.append(float(input("Digite o peso desta pessoa: ")))
    pessoas.append(dados[:])
    if dados[1] >= 80:
        pesados.append(dados[:])
    else:
        leves.append(dados[:])
    dados.clear()
    resp = str(input("Voce deseja continuar ? [S/N] "))
    if resp in "Nn":
        break
print(f"O total de pessoas cadastradas foi de {len(pessoas)}")
print(f"As pessoas a cima de 80kgs são: {pesados}")
print(f"As pessoas a baixo de 80kgs são: {leves}")
