def leiaInt(n):
    while not n.isnumeric():
        print(f'{n} não é um número')
        n = input('Digite um número: ')
    return n


aux = leiaInt(input('Digite um número: '))
print(f'Você digitou o número {aux}')
