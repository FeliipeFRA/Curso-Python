jogador = {}
g = []
tot = 0
print(f"\033[1;32m{'SOFASCORE':^50}\033[m")
print("\033[1;32m=\033[m" * 50)
jogador['Nome'] = str(input("\033[1;32m-\033[m Nome do jogador: "))
jogador['Camisa'] = int(input("\033[1;32m-\033[m Nº da camisa: "))
jogador['Time'] = str(input("\033[1;32m-\033[m Time do jogador: "))
p = int(input(f"\033[1;32m-\033[m Quantas partidas \033[1;32m{jogador['Nome'].title()}\033[m jogou nessa temporada? "))
print("\033[1;32m=\033[m" * 50)
for i in range(0, p):
    gol = (int(input(f"\033[1;32m-\033[m Gols feitos na {i+1}ª partida: ")))
    tot += gol
    g.append(gol)
jogador['Gols'] = g
jogador['Total'] = tot
print("\033[1;32m=\033[m" * 50)
print(f"\033[1;32m{'DADOS DO JOGADOR':^50}\033[m")
print(f"\033[1;32m-\033[m {jogador['Nome']} camisa {jogador['Camisa']} "
      f"pelo \033[1;32m{jogador['Time']}\033[m nessa temporada:")
for i in range(0, p):
    print(f"\033[1;32m {i+1}ª partida: {jogador['Gols'][i]}\033[m")
print("\033[1;32m=\033[m" * 50)
print(f"\033[1;32m-\033[m Total de gols: {jogador['Total']}")
print(f"\033[1;32m-\033[m Média de gols: {jogador['Total'] / p:.2f}")