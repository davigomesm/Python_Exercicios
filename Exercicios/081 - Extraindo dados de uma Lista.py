#   Exercício Python 081 - Extraindo dados de uma Lista
#   Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
#       A) Quantos números foram digitados.
#       B) A lista de valores, ordenada de forma decrescente.
#       C) Se o valor 5 foi digitado e está ou não na lista.


lista = []
while True:
    n = int(input("Digite um numero: "))
    lista.append(n)
    r = str(input("Deseja continuar? [S/N]"))
    if r in "Nn":
        break
print("-=-=-" * 15)
print(f"Foram digitados {len(lista)} numeros;")
print(f"A lista em ordem decrescente : ", end="")
lista.sort(reverse=True)
print(lista)
if 5 in lista:
    print("O valor 5 foi digitado e esta na lista: ")
else:
    print("O valor 5 não foi digitado e n esta na lista")
