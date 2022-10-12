print("\033[1;32mComparando números:\033[m")

num1 = int(input("Digite um numero inteiro: "))
num2 = int(input("Digite outro numero inteiro: "))

print("\033[1;32mCOMPARANDO ...\033[m")

if num1 > num2:
    print("O primeiro número é maior que o segundo número.")
elif num1 < num2:
    print("O segundo número é maior que o primeiro número.")
elif num1 == num2:
    print("O primeiro número e o segundo número são iguais.")
