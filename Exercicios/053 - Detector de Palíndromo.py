frase = str(input("Digite uma frase: ")).upper().strip()
palavras = frase.split()
junto = "".join(palavras)
invertido = ""

for letras in range(len(junto) -1, -1, -1):
    invertido = invertido + junto[letras]
if invertido == junto:
    print("A frase é um palíndromo! ")
else:
    print("A frase não é palídromo. ")
