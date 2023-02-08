#   Exercício Python 077 - Contando vogais em Tupla
#   Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
#   Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.


palavras = ("aprender", "python", "programar", "curso", "em", "video", "estudar")
for p in palavras:
    print(f"\nNa palavra {p.upper()} temos ", end="")
    for letra in p:
        if letra.lower() in "aeiou":
            print(letra, end="")
