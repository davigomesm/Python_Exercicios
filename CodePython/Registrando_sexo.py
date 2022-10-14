sexo = "H"
while sexo != "F" and "M":
    sexo = str(input("Registre seu sexo, digite [M ou F]: ")).upper().strip()[0]
    if sexo != "F" and "M":
        print("Dado invalido!")
    else:
        print("Sexo {} registrado com sucesso!".format(sexo))
