print("{:-^40}".format(" LOJAS AMERICANAS "))
preco = float(input("Digite o valor das compras: R$"))
print("""Formas de pagamento:
 [1] à vista dinheiro/cheque
 [2] à vista no cartão
 [3] 2x no cartão
 [4] 3x ou mais no cartão""")
opcao = int(input("Digite sua opção: "))
if opcao == 1:
    print("Você tem um desconto de 10%, total a pagar: R${:.2f}".format(preco - (preco * 0.10)))
elif opcao == 2:
    print("Você tem um desconto de 5%, total a pagar: R${:.2f}".format(preco - (preco * 0.05)))
elif opcao == 3:
    print("Você irá pagar em 2 parcelas de R${:.2f}".format(preco / 2))
elif opcao == 4:
    parcelas = int(input("Em quantas parcelas você deseja pagar? "))
    print("Você irá pagar em {} parcelas de R${:.2f}".format(parcelas, (preco / parcelas) * 1.20))
else:
    print("OPÇÃO INVALIDA!")
