import math
a = int(input("Digite um angulo para descobrir: seno, cosseno e tangente: "))
seno = math.sin(math.radians(a))
cosseno = math.cos(math.radians(a))
tangente = math.tan(math.radians(a))
print("O seno desse angulo vale: {:.2f}, o cosseno vale: {:.2f} e a tangente vale: {:.2f}".format(seno, cosseno, tangente))
