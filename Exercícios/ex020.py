import random
print('\033[1;31;40m~= TAL DO SORTEIO 2 =~\033[m\n' + '\033[1;31m-\033[m' * 22)
n1 = input('\033[1;31m•\033[m Aluno(a) \033[1;31m1\033[m: ')
n2 = input('\033[1;32m•\033[m Aluno(a) \033[1;32m2\033[m: ')
n3 = input('\033[1;33m•\033[m Aluno(a) \033[1;33m3\033[m: ')
n4 = input('\033[1;34m•\033[m Aluno(a) \033[1;34m4\033[m: ')
alunos = [n1, n2, n3, n4]
random.shuffle(alunos)
print('\033[1;31m-\033[m' * 22)
print(f'\033[1;31m•\033[m A ordem de apresentação será: {alunos}')
