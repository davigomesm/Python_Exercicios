print("Gerador de PA")
print("=-" * 18)
primeiro = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print("{} -> ".format(termo), end="")
        termo = termo + razao
        cont = cont + 1
    print("PAUSA")
    mais = int(input("Digite quantos termos vc quer digitar a mais? (Digite 0 para encerrar)"))
print("Progressão finalizou com {} termos.".format(total))
