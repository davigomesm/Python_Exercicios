#   Exercício Python 075 - Análise de dados em uma Tupla
#   Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#       A) Quantas vezes apareceu o valor 9.
#       B) Em que posição foi digitado o primeiro valor 3.
#       C) Quais foram os números pares.

num = (int(input("Digite um numero: ")), int(input("Digite mais um numero: ")), int(input("Digite outro um numero: ")), int(input("Digite o ultimo numero: ")))
print("Voce digitou os numeros: {}".format(num))
print(f"O numero 9 apareceu {num.count(9)} vezes")
if 3 in num:
    print(f"O primeiro numero 3 apareceu na posição {num.index(3)+1}")
else:
    print("Não tem numero 3 na tupla")
print("Os numero pares digitados foram:", end=" ")
for n in num:
    if n % 2 == 0:
        print(n, end=" ")
