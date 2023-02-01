from random import randint
print("-COMPUTADOR-: Vou pensar em um número!")
computador = randint(0, 10)
jogador = int(input("Digite um numero de 0 a 10 e tente adivinhar qual é: "))
c = 1
while jogador != computador:
    if computador > jogador:
        jogador = int(input("É mais... Digite outro número: "))
        c = c + 1
    if computador < jogador:
        jogador = int(input("É menos... Digite outro número: "))
        c = c + 1
print("Você acertou em {} tentativas! parabéns <3".format(c))
