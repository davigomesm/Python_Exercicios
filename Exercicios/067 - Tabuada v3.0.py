while True:
    n = int(input("Digite um numero para ver sua tabuada: "))
    if n < 0:
        break
    for c in range(1, 11):
        print("{} x {} = {}".format(n, c, n*c))
