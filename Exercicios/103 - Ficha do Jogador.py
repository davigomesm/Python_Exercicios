def ficha(jogador='Não informado', gols=-1):
    print('-'*40)
    print(f'{"Jogador":<20}{"Gols":<20}')
    if gols == -1:
        print(f'{jogador:<20}{"Não informado":<20}')
    else:
        print(f'{jogador:<20}{gols:<20}')

ficha()
ficha('ana')
ficha(gols=5)
ficha('marta', 3)
