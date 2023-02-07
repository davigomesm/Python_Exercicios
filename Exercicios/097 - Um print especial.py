#   Exercício Python 097 - Um print especial
#    Faça um programa que tenha uma função chamada escreva(),
#    que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

def escreva(msg):
    t = len(msg)
    print("-" * (t + 2))
    print(f" {msg}")
    print("-" * (t + 2))


escreva("Davi Gomes")
escreva("Curso em video")
escreva("Aula python")
