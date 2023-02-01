from random import randint
sort = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), )
print("Valores sorteados: ")
for n in sort:
    print(f"{n} ", end=" ")
print(f"\nO maoir numero é {max(sort)}")
print(f"O menor numero é {min(sort)}")
