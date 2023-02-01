print("Gerador de PA")
print("_-" * 20)
primeiro = int(input("Digite o primeiro termo: "))
razao = int(input("digite a razão: "))
termo = primeiro
cont = 1
while cont <=10:
    print("{} -> ".format(termo), end="")
    termo = termo + razao
    cont = cont + 1
print("FIM")
