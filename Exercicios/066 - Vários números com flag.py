soma = 0
quant = 0
while True:
    n = int(input("Digite um numero: "))
    if n == 999:
        break
    soma = soma + n
    quant = quant + 1
print("A quantidade de numero digitados foi {} e a soma deles foi {}".format(quant, soma))
