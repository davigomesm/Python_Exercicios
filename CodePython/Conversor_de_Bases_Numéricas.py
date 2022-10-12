num = int(input("Digite um numero inteiro: "))
print("""[ 1 ] para tranforma-lo em binário"
[ 2 ] para tranforma-lo em óctal"
[ 3 ] para tranforma-lo em hexadecimal""")
opção = int(input("Digite sua opção: "))
if opção == 1:
      print("O número {} em binário fica: {}".format(num, bin(num)[2:]))
elif opção == 2:
      print("O número {} em óctal fica: {}".format(num, oct(num)[2:]))
elif opção == 3:
      print("O número {} em hexdecimal fica: {}".format(num, hex(num)[2:]))
else:
      print("Opção inválida, tente novamente")
