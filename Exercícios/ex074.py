from random import randint
numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print("- Números gerados: ")
for num in range(0, (len(numeros))):
    print(f"\033[1;31m{numeros[num]}\033[m", end=" ")
print(f"\n- Maior número: {max(numeros)}")
print(f"- Menor número: {min(numeros)}")
