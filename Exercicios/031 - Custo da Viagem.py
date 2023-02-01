distancia = float(input("Digite em km, qual a distancia da sua viagem? "))
if distancia < 200:
    print("Será cobrado R${:.2f} pelo transporte da viagem".format(distancia * 0.50))
else:
    print("Será cobrado R${:.2f} pelo transporte da viagem".format(distancia * 0.45))
