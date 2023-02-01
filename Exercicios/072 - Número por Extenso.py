tupla = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoio", "dezenove", "vinte")
valor = int(input("digite um valor de 0 a 20: "))
while valor > 20 or valor < 0:
    valor = int(input("Valor incorreto, digite um valor de 0 a 20: "))
print(f"Você digitou o valor: {tupla[valor]}")
