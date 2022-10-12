num = int(input("digite um numero de 0 a 9999: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print("A unidade desse numero é: {}".format(u))
print("A dezena desse numero é: {}".format(d))
print("A centena desse numero é: {}".format(c))
print("A milhar desse numero é: {}".format(m))
