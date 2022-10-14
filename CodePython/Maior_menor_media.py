resp = "s"
soma = n = quant = maior = menor = 0
while resp in "Ss":
    n = int(input("Digite um numero: "))
    soma = soma + n
    quant = quant + 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = input("Você quer continuar? [Sim/Não]").upper().strip()[0]
media = soma / quant
print("A soma dos valores foi de {}, a media foi de {:.2f}, o maior numero é {} e o menor numero é {}".format(soma, media, maior, menor))
print("fim")
