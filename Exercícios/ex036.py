print('\033[1;31;40m    ~= TAL DO EMPRÉSTIMO =~    \033[m\n' + '\033[1;31m-\033[m' * 31)
print('\033[1mNEGOCIE O EMPRÉSTIMO DA SUA CASA PRÓPRIA!\033[m')
v = int(input('\033[1;31m•\033[m Valor do imóvel:\n\033[1;32m-----> R$\033[m '))
s = int(input('\033[1;31m•\033[m Seu salário atual:\n\033[1;32m-----> R$\033[m '))
a = int(input('\033[1;31m•\033[m Pagará em quantos anos:\n\033[1;31m----->\033[m '))
p = v / (a * 12)
print('\033[1;31m-\033[m' * 31)
if p > (s * 0.3):
    print(f'\033[1;31mEmprestimo negado!\033[m\nA parcela \033[1;31m(R${p:.2f})\033[m ultrapassa 30% do seu salário '
          f'\033[1;31m(R${s * 0.3:.2f})\033[m!')
else:
    print(f'\033[1;32mEmprestimo aprovado!\033[m\nValor da parcela: \033[1;31mR${p:.2f}\033[m')
