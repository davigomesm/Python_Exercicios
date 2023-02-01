n = 0
cont = 0
soma = 0
n = int(input("Digite um numero (999 para parar)"))
while n != 999:
    soma = soma + n
    cont = cont + 1
    n = int(input("Digite um numero (999 para parar)"))
print("Voçê digitou {} numeros e a soma entre eles foi {}".format(cont, soma))
