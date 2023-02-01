kmr = float(input("Quantos kilometros foram rodados? "))
d = float(input("E por quantos dias foi alugado? "))
print("total a pagar pelo aluguel: R${:.2f}".format((kmr * 0.15) + (d * 60)))
