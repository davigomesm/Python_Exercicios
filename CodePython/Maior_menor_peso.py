pesomaior = 0
pesomenor = 0
for pessoa in range(1, 6):
    peso = float(input("Digite o peso da {}ª pessoa: kg".format(pessoa)))
    if pesomaior < peso:
        pesomaior = peso
    elif pesomaior > peso:
        pesomenor = peso
print("O maior peso é: {:.2f}kg".format(pesomaior))
print("O menor peso é: {:.2f}kg".format(pesomenor))
