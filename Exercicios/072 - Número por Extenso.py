#   Exercício Python 072 - Número por Extenso
#   Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
#   Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

tupla = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoio", "dezenove", "vinte")
valor = int(input("digite um valor de 0 a 20: "))
while valor > 20 or valor < 0:
    valor = int(input("Valor incorreto, digite um valor de 0 a 20: "))
print(f"Você digitou o valor: {tupla[valor]}")
