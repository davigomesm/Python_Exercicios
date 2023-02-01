from datetime import date
anoatual = date.today().year
nasc = int(input("Digite o ano de nascimento do atleta: "))
idade = anoatual - nasc
if idade < 9:
    print("O atleta faz parte da categoria MIRIM!")
elif idade >= 9 and idade < 14:
    print("O atleta faz parte da categoria INFANTIL!")
elif idade >= 14 and idade < 19:
    print("O atleta faz parte da categoria JUNIOR!")
elif idade >= 19 and idade < 25:
    print("O atleta faz parte da categoria SENIOR!")
elif idade >= 25:
    print("O atleta faz parte da categoria MASTER!")
