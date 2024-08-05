pessoas = []
dados = {}
media = 0
print(f"\033[1;31m{'CADASTRO':^30}\033[m")
print("\033[1;31m=\033[m" * 30)
while True:
    dados.clear()
    dados['Nome'] = str(input("- Nome: ")).strip().title()
    dados['Sexo'] = str(input("- Sexo [M/F]: ")).strip().upper()[0]
    while dados['Sexo'] not in "FM":
        print("\033[1;31mOpção inválida! Digite apenas M ou F.\033[m")
        dados['Sexo'] = str(input("- Sexo [M/F]: ")).strip().upper()[0]
    dados['Idade'] = int(input("- Idade: "))
    media += dados['Idade']
    pessoas.append(dados.copy())
    print("\033[1;31m=\033[m" * 30)
    cont = str(input("- Deseja continuar? [S/N] ")).strip().upper()[0]
    while cont not in "SN":
        print("\033[1;31mOpção inválida! Digite apenas S ou N.\033[m")
        print("\033[1;31m=\033[m" * 30)
        cont = str(input("- Deseja continuar? [S/N] ")).strip().upper()[0]
    print("\033[1;31m=\033[m" * 30)
    if cont == "N":
        break
media = media / len(pessoas)
print(f"- Total de pessoas cadastradas: {len(pessoas)}")
print(f"- Média de idade do grupo: {media:.2f}")
print(f"- Mulheres cadastradas: ", end='')
quantm = 0
for i in range(0, len(pessoas)):
    if pessoas[i]['Sexo'] == "F":
        quantm += 1
        if quantm == 1:
            print(f"{pessoas[i]['Nome']}", end='')
        else:
            print(f", {pessoas[i]['Nome']}", end='')
if quantm == 0:
    print("Nenhuma! ")
print(f"\n- Pessoas com a idade acima da média: ")
acima = 0
for pessoa in pessoas:
    if pessoa['Idade'] > media:
        acima += 1
        if pessoa['Sexo'] == "F":
            print(f"\033[1;31m{pessoa['Nome']}, Sexo Feminino, {pessoa['Idade']} anos.")
        else:
            print(f"\033[1;31m{pessoa['Nome']}, Sexo Masculino, {pessoa['Idade']} anos.")
if acima == 0:
    print("Nenhuma!")
