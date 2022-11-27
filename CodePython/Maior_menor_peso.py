pesomaior = 0
pesomenor = 0
for pessoa in range(0, 5):
    peso = float(input("Digite o peso da {}ª pessoa: kg".format(pessoa)))
    if pessoa == 0:
        pesomaior = pesomenor = peso
    else:
        if peso > pesomaior:
            pesomaior = peso
        if peso < pesomenor:
            pesomenor = peso
print("O maior peso é: {:.2f}kg".format(pesomaior))
print("O menor peso é: {:.2f}kg".format(pesomenor))
