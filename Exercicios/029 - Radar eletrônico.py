vel = float(input("Qual a velocidade em km/h o carro passou no foto-sensor: "))
multa = (vel - 80) * 7
if vel > 80:
    print("MULTA! POR PASSAR DO LIMITE DE VELOCIDADE!")
    print("Valor da multa por excesso de velocidade: R${:.2f}".format(multa))
else:
    print("SEM REGISTRO DE MULTA, MOTORISTA CONDUZINDO NA VELOCIDADE REGULAR")
