idadetotal = 0
maioridadehomem = 0
homemvelho = ""
totalmulheres20 = 0
for pessoas in range(1, 5):
    print("Pessoa numero {}, digite os dados: ".format(pessoas))
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M]/[F]: ")).upper()
    idadetotal = idadetotal + idade
    if sexo == "M" and idade > maioridadehomem:
        maioridadehomem = idade
        homemvelho = nome
    if sexo == "F" and idade < 20:
        totalmulheres20 = totalmulheres20 + 1

print("\nA idade média das pessoas é: {}".format(idadetotal/4))
print("A pessoa mais velha tem {} anos e se chama: {}".format(maioridadehomem, homemvelho))
print("O total de mulheres com menos de 20 anos são: {}".format(totalmulheres20))
