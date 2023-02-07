def voto(ano):
    from datetime import date
    anoatual = date.today().year
    idade = anoatual - ano
    print(f"Esta pessoa nasceu no ano {ano}")
    if idade < 16:
        return "Voto negado"
    elif idade >= 18:
        return "Voto obrigatorio"
    elif idade > 65:
        return "Voto opcional"


nascimento = int(input("Digite o ano de nascimento: "))
print(voto(nascimento))
