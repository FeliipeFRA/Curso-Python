from random import randint
num = randint(0, 30)
j = ['Santos', 'Varela', 'Léo Pereira', 'Pulgar', 'Ayrton Lucas', 'Éverton Ribeiro', 'Thiago Maia', 'Pedro', 'Gabigol',
     'Cebolinha', 'Arrascaeta', 'Fabrício Bruno', 'Filipe Luís', 'Rossi', 'Gerson', 'Allan', 'Luiz Araújo',
     'David Luiz', 'Matheus Cunha', 'Bruno Henrique', 'Victor Hugo', 'Pablo', 'Cleiton', 'Matheuzinho',
     'Matheus Gonçalves', 'Gabriel Noga', 'Matheus França', 'Wesley', 'Mateusão', 'Igor Jesus']
c = j[num-1]
print('-=-' * 10+'\nADVINHE O JOGADOR DO FLAMENGO\n'+'-=-' * 10)
print('| Computador: Pensei em um jogador do Flamengo... Dúvido você advinhar!\n')
p = str(input('JOGADOR ESCOLHIDO:\n------> ')).strip()
if p.upper() == c.upper():
    print('PARABÉNS!\nVocê acertou!')
else:
    print(f'TENTE NOVAMENTE!\nO jogador que eu pensei foi o {c}!')
