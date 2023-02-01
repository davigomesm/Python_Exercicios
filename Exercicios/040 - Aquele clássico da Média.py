print("\033[32mCalculo da media de um aluno:\033[m")
nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))
media = (nota1 + nota2) / 2
print("A media do aluno é {:.2f}".format(media))
if media < 5:
    print("\033[31mO aluno está reprovado!\033[m")
elif media >= 5 and media < 7:
    print("\033[33mO aluno está de recuperação.\033[m")
elif media >= 7:
    print("\033[32mO aluno está APROVADO!!!\033[m")
