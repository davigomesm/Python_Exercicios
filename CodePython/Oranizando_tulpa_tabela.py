lista = ("ak-47", 2700,
         "awp", 4750,
         "m4a1", 2900,
         "mp9", 1250,
         "ump", 1200,
         "famas", 2050,
         "galil", 1800,
         "desert", 700)
print("=" * 41)
print(f"{'LOJA VALVE':^40}")
print("=" * 41)
for p in range(len(lista)):
    if p % 2 == 0:
        print("{:.<30""}".format(lista[p]), end=" ")
    else:
        print("R$ {:>7.2f}".format(lista[p]))
print("=" * 41)
