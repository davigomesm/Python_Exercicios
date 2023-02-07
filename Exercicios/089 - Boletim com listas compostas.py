#   Exercício Python 089 - Boletim com listas compostas
#   Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
#   No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar
#   as notas de cada aluno individualmente.

ficha = []
while True:
    nome = str(input("Digite o nome do aluno: "))
    nota1 = float(input("Digite a primeira nota do aluno: "))
    nota2 = float(input("digite a segunda nota do aluno: "))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input("Quer continuar? [S/N] "))
    if resp in "Nn":
        break
print("=-" * 30)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print("-" * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print("-" * 35)
    opc = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    if opc == 999:
        print("finalizando...")
        break
    if opc <= len(ficha) - 1:
        print(f"Notas de {ficha[opc][0]} são {ficha[opc][1]}")
print("volte sempre")
