valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
resultado = 0
opcao = 0
print("""Opções:
[1] somar
[2] multiplicar
[3] maior numero
[4] novos valores
[5] sair""")
while opcao != 5:
    opcao = int(input("Digite uma opção: "))
    if opcao == 1:
        resultado = valor1 + valor2
        print("O resultado da soma foi {}".format(resultado))
    if opcao == 2:
        resultado = valor1 * valor2
        print("O resultado da multiplicação foi {}".format(resultado))
    if opcao == 3:
        if valor1 == valor2:
            print("Os valores são iguais")
        if valor1 > valor2:
            print("O valor {} é maior que o valor {}".format(valor1, valor2))
        if valor2 > valor1:
            print("O valor {} é maior que o valor {}".format(valor2, valor1))
    if opcao == 4:
        valor1 = int(input("Digite o primeiro valor novamente: "))
        valor2 = int(input("Digite o segundo valor novamente: "))
print("Operação finalizada")
