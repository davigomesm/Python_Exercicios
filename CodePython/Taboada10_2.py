n = int(input("Escolha um numero para ver sua taboada: "))
for t in range(1, 11):
    resultado = n * t
    print("{} * {} = {}".format(n, t, resultado))
