print("\033[1;32;40m ~= TAL DO FATORIAL DNV =~ \033[m")
num = int(input("- Número a ser fatorado: "))
numi = num
fat = num
while num != 1:
    fat = fat * (num - 1)
    num -= 1
print("\033[1;32;40m         RESULTADO:        \033[m ")
print(f"\033[1;32m{numi}! = {fat}\033[m")
