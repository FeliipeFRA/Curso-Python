again = sex = ""
contf20 = cont18 = contm = 0
print("    ~= CADASTRO =~    ")
print("-" * 22)
while True:
    idade = int(input("- Idade: "))
    if idade > 18:
        cont18 += 1
    while True:
        sex = str(input("- Sexo [M/F]: ")).strip().upper()[0]
        if sex not in ("M", "F"):
            print("Opção inválida!")
        if sex == "M":
            contm += 1
            break
        if sex == "F":
            if idade < 20:
                contf20 += 1
            break
    print("-" * 22)
    print("CADASTRADO COM SUCESSO")
    print("-" * 22)
    again = str(input("Deseja cadastrar outra pessoa? [S/N]\n-----> ")).strip().upper()[0]
    while again not in ("S", "N"):
        print("Opção inválida!")
        again = str(input("Deseja cadastrar outra pessoa? [S/N]\n-----> ")).strip().upper()[0]
    print("-" * 22)
    if again == "N":
        print(f"- MAIORES DE 18 ANOS: {cont18}")
        print(f"- HOMENS CADASTRADOS: {contm}")
        print(f"- MULHERES MENORES DE 20 ANOS: {contf20}")
        break
