def fatorial(num, show=False):
    fat = 1
    for i in range(num, 0, -1):
        fat *= i
    if show:
        for i in range(num, 0, -1):
            if i == 1:
                print('1', end='')
            else:
                print(i, end=' x ')
        print(f' = {fat}')
    else:
        print(f'Fatorial de {num}! é {fat}')


n = int(input('Informe um número para calcular o fatorial: '))
mostrar = int(input('Mostrar na tela? [0-Não/1-Sim]'))
fatorial(n, mostrar)
