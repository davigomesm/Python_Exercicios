soma = 0
for c in range(1, 7):
    num = int(input("Digite o {}º valor: ".format(c)))
    if num % 2 == 0:
        soma = soma + num
print("A soma vale: {}".format(soma))
