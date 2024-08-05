aluno = {}
aluno['Nome'] = str(input("- Nome do aluno: "))
aluno['Média'] = float(input("- Média: "))
if aluno['Média'] >= 7:
    aluno['Situação'] = "Aprovado"
elif aluno['Média'] >= 5:
    aluno['Situação'] = "Recuperação"
else:
    aluno['Situação'] = "Reprovado"
print("=" * 30)
for k, v in aluno.items():
    print(f"- {k}: {v}")