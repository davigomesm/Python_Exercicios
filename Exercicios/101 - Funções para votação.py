#   Exercício Python 101 - Funções para votação
#    Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma
#    pessoa retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

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
