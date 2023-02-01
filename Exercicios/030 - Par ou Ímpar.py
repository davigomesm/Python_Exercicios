numero = int(input("Digite um numero para descobrir se ele é impar ou par: "))
resto = numero % 2
if resto == 0:
    print("Esse número é par")
else:
    print("Esse número é impar")
