times = (
    "Flamengo",
    "Santos",
    "Palmeiras",
    "Grêmio",
    "Athletico Paranaense",
    "São Paulo",
    "Internacional",
    "Corinthians",
    "Fortaleza",
    "Goiás",
    "Bahia",
    "Vasco da Gama",
    "Atlético Mineiro",
    "Fluminense",
    "Botafogo",
    "Ceará",
    "Cruzeiro",
    "CSA",
    "Chapecoense",
    "Avaí"
)
print("\033[1;42m ~= BRASILEIRÃO SÉRIE A 2019 =~ \033[m")
for pos in range(0, len(times)):
    if pos == 0:
        print(f"\033[1;34m{pos + 1}º - {times[pos]}\033[m")
    elif 0 < pos < 6:
        print(f"\033[34m{pos + 1}º - {times[pos]}\033[m")
    elif 6 <= pos < 8:
        print(f"\033[33m{pos + 1}º - {times[pos]}\033[m")
    elif 6 <= pos < 14:
        print(f"\033[32m{pos + 1}º - {times[pos]}\033[m")
    elif 15 < pos < 20:
        print(f"\033[31m{pos + 1}º - {times[pos]}\033[m")
    else:
        print(f"{pos+1}º - {times[pos]}")
print("\033[1;42m           ~= DADOS =~          \033[m")
print(f"- G4: ")
for pos in range(0, 4):
    print(f"{times[pos]}", end=" ")
print("\n- Z4: ")
for pos in range(16, 20):
    print(f"{times[pos]}", end=" ")
print("\n- TIMES EM ORDEM ALFABÉTICA:")
print(f"{sorted(times)}")
print("- POSIÇÃO DO VASCO DA GAMA:")
for pos in range(0, len(times)):
    if times[pos] == "Vasco da Gama":
        print(f"{pos + 1}º LUGAR")