s1 = float(input("Digite o primeiro seguimento: "))
s2 = float(input("Digite o segundo seguimento: "))
s3 = float(input("Digite o terceiro seguimento: "))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print("Os seguimentos acima podem formar um triangulo ", end="")
    if s1 == s2 and s2 == s3:
        print("EQUILATERO!")
    elif s1 != s2 and s2 != s3 and s1 != s3:
        print("ESCALENO!")
    else:
        print("ISOSCELES!")
else:
    print("Os seguimentos acima NAO podem formar um triangulo")
