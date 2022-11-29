lista = list()
while True:
    n = int(input("Digite um numero: "))
    if n not in lista:
        lista.append(n)
        print("Valor adicionado! ")
    else:
        print("numero duplicado!")
    r = str(input("Deseja continuar ? [S/N] "))
    if r in "Nn":
        break
lista.sort()
print(f"Lista em ordem crescente: {lista}")
