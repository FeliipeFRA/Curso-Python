print("\033[1;31;40m ~= VERIFICADOR DE SEXO =~ \033[m")
print("\033[1;31m-\033[m" * 27)
s = ""
while s != "F" and s != "M":
    s = str(input("\033[1;31m-\033[m Qual seu sexo? \033[1;31m[F/M]\033[m\n\033[1;31m-----> \033[m")).strip().upper()[0]
    if s != "F" and s != "M":
        print("\033[1;31m- Opção inválida! Tente novamente.\033[m")
        print("\033[1;31m-\033[m" * 27)
    else:
        print("\033[1;31m-\033[m" * 27)
        print(f"\033[1;32m- Sexo {s} registrado com sucesso!")
