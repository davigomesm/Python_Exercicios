import math
co = float(input("Digite o comprimento do cateto oposto: "))
ca = float(input("Digite o comprimento do cateto adjacente: "))
hip = math.hypot(ca, co)
print("A hipotenusa do triangulo retangulo é {:.2f}".format(hip))
