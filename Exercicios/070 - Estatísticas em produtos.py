#   Exercício Python 070 - Estatísticas em produtos
# #   Crie um programa que leia o nome e o preço de vários produtos.
# #   O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# #       A) qual é o total gasto na compra.
# #       B) quantos produtos custam mais de R$1000.
# #       C) qual é o nome do produto mais barato.


total = 0
totalmil = 0
menor = 0
cont = 0
barato = " "
while True:
    produto = str(input("Digite o nome do produto: "))
    preco = float(input("preço: R$"))
    cont = cont + 1
    total = total + preco
    if preco > 1000:
        totalmil = totalmil + 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resposta = " "
    while resposta not in "SN":
        resposta = str(input("Quer continuar? [Sim/Não]")).upper().strip()[0]
    if resposta == "N":
        break
print("O total da compra foi de R${:.2f}".format(total))
print("total de {} produtos custando mais de R$1000.00".format(totalmil))
print("O produto mais barato é {} que custa R${:.2f}".format(barato, menor))
