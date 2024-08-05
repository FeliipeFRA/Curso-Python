print('\033[1;31;40m-~ DISSECADOR DE VARIÁVEIS ~-\033[m\n' + '\033[1;31m-\033[m' * 29)
x = input('\033[1;31m•\033[m Escreva algo, dissecaremos a variável:\n\033[1;31m----->\033[m ')
print(f'\n\033[1;31m•\033[m A variável é do tipo: \033[1;32mstr\033[m')
print('\033[1;31m•\033[m É alfanumérico:', '\033[1;32mSim\033[m' if x.isalnum() else '\033[1;31mNão\033[m')
print('\033[1;31m•\033[m É numérico:', '\033[1;32mSim\033[m' if x.isnumeric() else '\033[1;31mNão\033[m')
print('\033[1;31m•\033[m É alfabético:', '\033[1;32mSim\033[m' if x.isalpha() else '\033[1;31mNão\033[m')
print('\033[1;31m•\033[m Seus caracteres estão na Tabela ASCII:', '\033[1;32mSim\033[m' if x.isascii() else '\033[1;31m'
                                                                                                            'Não\033[m')
print('\033[1;31m•\033[m Começa com letra maiúscula:', '\033[1;32mSim\033[m' if x.istitle() else '\033[1;31mNão\033[m')
print('\033[1;31m•\033[m É escrito em letra minúscula:', '\033[1;32mSim\033[m' if x.islower() else '\033[1;31mNão\033[m'
      )
print('\033[1;31m•\033[m É escrito em letra maiúscula:', '\033[1;32mSim\033[m' if x.isupper() else '\033[1;31mNão\033[m'
      )
print('\033[1;31m•\033[m É um dígito:', '\033[1;32mSim\033[m' if x.isdigit() else '\033[1;31mNão\033[m')
print('\033[1;31m•\033[m É decimal:', '\033[1;32mSim\033[m' if x.isdecimal() else '\033[1;31mNão\033[m')
print('\033[1;31m•\033[m É um identificador:', '\033[1;32mSim\033[m' if x.isidentifier() else '\033[1;31mNão\033[m')
print('\033[1;31m•\033[m É possível imprimir:', '\033[1;32mSim\033[m' if x.isprintable() else '\033[1;31mNão\033[m')
print('\033[1;31m•\033[m É somente espaço:', '\033[1;32mSim\033[m' if x.isspace() else '\033[1;31mNão\033[m')
