#   Exercício Python 090 - Dicionário
#   Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
#   No final, mostre o conteúdo da estrutura na tela.

aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Media de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'De recuperação'
else:
    aluno['situação'] = 'Reprovado'
print()
print(f'O(a) Aluno(a): {aluno["nome"]} teve media: {aluno["media"]} e está {aluno["situação"]}')
