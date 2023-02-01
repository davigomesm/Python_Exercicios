def terreno(l, c):
    area = l * c
    print(f'A área de um terreno com {l} x {c} é de {area}m²')


print("CALCULO DA AREA DO TERRENO")
print('-'*20)

largura = float(input('Largura: (m) '))
comprimento = float(input('Comprimento: (m) '))

terreno(largura, comprimento)
