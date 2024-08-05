alunos = []
aluno = []
notas = []
print("\033[1;31m=" * 35)
print("SISTEMA ESCOLA DE NOTAS".center(35, " "))
print("\033[1;31m=\033[m" * 35)
while True:
    nome = str(input("\033[1;31m-\033[m Nome do Aluno: "))
    n1 = float(input("\033[1;31m-\033[m Nota 1: "))
    n2 = float(input("\033[1;31m-\033[m Nota 2: "))
    m = (n1 + n2) / 2
    notas.append(n1)
    notas.append(n2)
    aluno.append(nome)
    aluno.append(notas[:])
    notas.clear()
    aluno.append(m)
    alunos.append(aluno[:])
    aluno.clear()
    print("\033[1;32mALUNO CADASTRADO COM SUCESSO!\033[m")
    print("\033[1;31m=\033[m" * 35)
    cont = str(input("\033[1;31m-\033[m Deseja continuar? \033[1;31m[S/N]\033[m ")).upper().strip()[0]
    print("\033[1;31m=\033[m" * 35)
    if cont == "N":
        break
print("\033[1;41m              BOLETIM              \033[m")
print("\033[1;31mNº: ".ljust(4, " "), end=" ")
print("NOME:".ljust(23, " "), end=" ")
print("MÉDIA:\033[m".ljust(6, " "))
for a in range(0, len(alunos)):
    print(f"{a}".ljust(4, " "), end=" ")
    print(f"{alunos[a][0]}".ljust(23, " "), end=" ")
    print(f"{alunos[a][2]}".ljust(6, " "))
while True:
    print("\033[1;31m=\033[m" * 35)
    n = int(input("\033[1;31m-\033[m Deseja ver as notas de qual aluno? \033[1;31m[999]\033[m "))
    if n == 999:
        break
    if n >= len(alunos):
        print(f"\033[1;31mALUNO NÃO ENCONTRADO! Tente novamente")
    else:
        for a in range(0, len(alunos)):
            if a == n:
                print(f"\033[1;31m-\033[m As notas de \033[1;31m{alunos[a][0]}\033[m são: "
                      f"\033[1;31m{alunos[a][1][0]}\033[m e \033[1;31m{alunos[a][1][1]}\033[m")
print("\033[1;31m=\033[m" * 35)
print("\033[1;31mFINALIZANDO SISTEMA...\033[m")
