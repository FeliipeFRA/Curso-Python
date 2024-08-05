exp = str(input("- Digite uma expressão: "))
p = []
for l in exp:
    if l in "()":
        p.append(l)
if p.count("(") != p.count(")") or p[0] == ")" or p[len(p) - 1] == "(":
    print("\033[1;31mA EXPRESSÃO ESTÁ INCORRETA!")
else:
    print("\033[1;32mA EXPRESSÃO ESTÁ CORRETA!")
