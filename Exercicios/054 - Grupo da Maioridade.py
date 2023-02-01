from datetime import date
anoatual = date.today().year
totalmaiores = 0
totalmenores = 0
for pessoa in range(1, 8):
    nasc = int(input("Digite o ano de nascimento da {}ª pessoa: ".format(pessoa)))
    idade = anoatual - nasc
    if idade < 18:
        totalmenores = totalmenores + 1
    else:
        totalmaiores = totalmaiores + 1
print("O total de pessoas de maiores: {}".format(totalmaiores))
print("E o total de pessoas de menores: {}".format(totalmenores))
