#   Exercício Python 073 - Tuplas com Times de Futebol
#   Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
#   na ordem de colocação. Depois mostre:
#       a) Os 5 primeiros times.
#       b) Os últimos 4 colocados.
#       c) Times em ordem alfabética.
#       d) Em que posição está o time da Chapecoense.


times = ("palmeiras", "internacional", "flamengo", "corinthians", "fluminense", "atletico-pr", "atletico-mg",
         "são paulo", "america-mg", "fortaleza", "botafogo", "santos", "bragantino", "goias",
         "coritiba", "ceara", "atletico-go", "cuiaba", "avai", "juventude")

print("=-" * 30)
print(f"Os 5 primeiros colocados são : {times[0:5]}")
print("=-" * 30)
print(f"Os 4 ultimos colocados são: {times[16:19]}")
print("=-" * 30)
print(f"Os times em ordem alfabetica: {sorted(times)}")
print("=-" * 30)
print(f"O fortaleza está na {times.index('fortaleza')} posição")
