#   Exercício Python 094 - Unindo dicionários e listas
#   Crie um programa que leia nome, sexo e idade de várias pessoas,
#   guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
#       A) Quantas pessoas foram cadastradas
#       B) A média de idade
#       C) Uma lista com as mulheres
#       D) Uma lista de pessoas com idade acima da média

pessoas = dict()
chavenomes = list()
chaveidades = list()
chavesexo = list()
mulheres = list()
continuar = ' '


while True:
    nome = str(input('Nome: '))
    chavenomes.append(nome)
    pessoas['nome'] = chavenomes




    sexo = str(input('Sexo: M/F: ')).upper()
    if sexo not in 'MF':
        print('erro')
        chavenomes.pop()
        continue


    elif sexo in 'FM':
        chavesexo.append(sexo)
        pessoas['sexo'] = chavesexo


    idade = int(input('Idade: '))
    chaveidades.append(idade)
    pessoas['idade'] = chaveidades
    media = sum(chaveidades) / len(chaveidades)


    continuar = str(input('Continuar? S/N: '))
    if continuar in 'nN':
        break


for nome, sexo, idade in zip(chavenomes, chavesexo, chaveidades):
    if sexo in 'F':
        mulheres.append(nome)


print('-=' * 20)
print(f'A) Ao todo temos {len(chavenomes)} pessoas cadastradas.')
print(f'B) A média de idade é de {media:.2f} anos.')
print(f'C) As mulheres cadastradas foram {mulheres}.')
print(f'D) Lista das pessoas que estão acima da média:')
for n, s, i in zip(chavenomes, chavesexo, chaveidades):
    if i > media:
        print(f'Nome: = {n}; sexo = {s}; idade = {i};')
