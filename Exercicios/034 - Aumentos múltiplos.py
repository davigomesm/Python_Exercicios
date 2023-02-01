salario = float(input("Digite o valor do salario do funcionario: R$"))
if salario > 1250.00:
    print("O salario do funcionario com aumento de 10% ficará: R${:.2f}".format(salario + (salario * 0.10)))
if salario <= 1250.00:
    print("O salario do funcionario com aumento de 15% ficará: R${:.2f}".format(salario + (salario * 0.15)))
