import random
adv1 = str(input('Time casa: '))
adv2 = str(input('Time visitante: '))
gf0 = 0
gf1 = 1
gf2 = 2
gf3 = 3
gf4 = 4
gf5 = 5
ga0 = 0
ga1 = 1
ga2 = 2
ga3 = 3
ga4 = 4
ga5 = 5
gols_fla = [gf0, gf1, gf2, gf3, gf4, gf5]
gols_ad = [ga0, ga1, ga2, ga3, ga4, ga5]
ad1 = random.choice(gols_fla)
ad2 = random.choice(gols_ad)
print(f'O placar do jogo será {adv1} {ad1} X {ad2} {adv2}')
