from datetime import date
ano = date.today().year
print('\033[1;31;40m ~= É A TAL DA MAIORIDADE =~ \033[m\n' + '\033[1;31m-\033[m' * 29)
idades = []
for i in range(1, 8):
    print(f'\033[1;31m- Pessoa {i}:\033[m')
    nasc = int(input('\033[1;31m•\033[m \033[1mAno de nascimento:\033[m '))
    idade = ano - nasc
    idades.append((idade))
total = 0
for i in range (0, 7):
    if idades[i] > 21:
        total += 1
print(f'Das 7 pessoas, {total} já alcançaram a maioridade e {7 - total} ainda não.')
