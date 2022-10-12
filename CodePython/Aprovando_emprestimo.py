print("\033[0;32mAPROVAÇÃO DE EMPRESTIMO PARA IMOVEIS: \033[m")

salario = float(input("Digite o seu salario mensal: R$"))
imovel = float(input("Digite o valor do imovel: R$"))
anos = float(input("Em quantos anos vc deseja parcelar o imovel: "))
prestacao = imovel / (anos * 12)
aceitacao = salario * 0.3

print("O valor da prestação será de: R${:.2f}".format(prestacao))

if aceitacao >= prestacao:
    print("\033[0;32mO EMPRESTIMO FOI ACEITO, ESTÁ TUDO DENTRO DAS NORMAS.\033[m")
else:
    print("\033[0;31mO EMPRESTIMO FOI NEGADO\033[m, O VALOR DA PRESTAÇÃO PRESCISA SER 30% DO SEU SALARIO OU MENOS.")
