nome = input("digite o seu nome completo: ")
mais = nome.upper()
minus = nome.lower()
print("O nome com todas as letras maiusculas {} e com todas a letras minusculas {}".format(mais, minus))
nomev = nome.split()
nomec = "".join(nomev)
print("O nome sem espaços tem {} letras".format(len(nomec)))
l1nome = len(nomev[0])
print("o primeiro nome tem {} letras".format(l1nome))
