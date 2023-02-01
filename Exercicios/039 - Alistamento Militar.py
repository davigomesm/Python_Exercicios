from datetime import date
sex = input("Qual o seu sexo ou genero ?")
if sex in "Feminino Mulher feminino mulher":
    print("Mulheres são isentas ao serviço militar.")
elif sex in "homem masculino Homem Masculino":
    anoatual = date.today().year
    nasc = int(input("Qual o ano do seu nascimento? "))
    idade = anoatual - nasc
    print("Quem nasceu em {} tem {} anos em {}.".format(nasc, idade, anoatual))
    if idade == 18:
        print("Está no ano de seu alistamento.")
    elif idade > 18:
        print("O tempo do seu alistamento ja passou há {} anos.".format(idade - 18))
    elif idade < 18:
        print("O ano de seu alistamento será em {}, ainda falta {} anos.".format(anoatual + 18 - idade, 18 - idade))
