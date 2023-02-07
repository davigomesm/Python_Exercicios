#   Exercício Python 080 - Lista ordenada sem repetições
#   Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
#   já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista = []
for c in range (0, 5):
    n = int(input("Digite um valor: "))
    if c == 0 or n > lista[len(lista)-1]:
        lista.append(n)
        print("Valor adicionado ao final da lista.")
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f"Valor adicionado na posição {pos}.")
                break
            pos = pos + 1
print(f"Valores adicionados na lista em ordem (sem usar sort) é: {lista}")
