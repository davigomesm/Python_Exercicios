ano = int(input("Digite um ano para descobrir se ele é um ano bissexto "))
resto4 = ano % 4
resto400 = ano % 400
resto100 = ano % 100
if resto4 == 0:
    if resto100 == 0:
        print("O ano {} não é um ano bissexto".format(ano))
    else:
        print("O ano {} é um ano bissexto".format(ano))
else:
    if resto400 == 0:
        print("O ano {} é um ano bissexto".format(ano))
    else:
        print("O ano {} não é um ano bissexto".format(ano))

#modo mais facil de entender kkkk

ano2 = int(input("Digite um ano para descobrir se ele é um ano bissexto "))
if ano2 % 4 == 0 and ano2 % 100 != 0 or ano2 % 400 == 0:
    print("O ano {} é um ano bissexto".format(ano2))
else:
    print("O ano {} não é um ano bissexto".format(ano2))
