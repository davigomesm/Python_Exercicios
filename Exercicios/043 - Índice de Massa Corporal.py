peso = float(input("Digite o seu peso: (kg) "))
altura = float(input("Digite a sua altura: (m) "))
imc = peso / (altura ** 2)
print("O seu IMC vale: {:.1f}".format(imc))
if imc < 18.5:
    print("Você está abaixo do peso normal!")
elif imc < 25:
    print("Você está no peso ideal")
elif imc < 30:
    print("Você está acima do peso ideal!")
elif imc < 40:
    print("Você está obeso!")
else:
    print("Você está com OBESIDADE MÓRBIDA! se cuide!")
