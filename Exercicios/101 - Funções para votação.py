def voto(ano):
    from datetime import date
    anoatual = date.today().year
    idade = anoatual - ano
    print(f"Esta pessoa nasceu no ano {ano}")
    if idade < 16:
        return "Voto negado"
    elif 16 <= idade < 18 or idade >= 65:
        return "Voto opcional"
    else:
        return "Voto obrigatorio"


nascimento = int(input("Digite o ano de nascimento: "))
print(voto(nascimento))
