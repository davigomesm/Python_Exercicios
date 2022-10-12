numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))
numero3 = int(input("Digite o terceiro numero: "))
maior = 0
menor = 0

#Calculando o maior numero:

if numero1 > numero2 and numero1 > numero3:
    maior = numero1
if numero2 > numero1 and numero2 > numero3:
    maior = numero2
if numero3 > numero1 and numero3 > numero2:
    maior = numero3

#Calculando o menor numero:

if numero1 < numero2 and numero1 < numero3:
    menor = numero1
if numero2 < numero1 and numero2 < numero3:
    menor = numero2
if numero3 < numero1 and numero3 < numero2:
    menor = numero3

print("O maior numero é o {}".format(maior))
print("o menor numero é o {}".format(menor))
