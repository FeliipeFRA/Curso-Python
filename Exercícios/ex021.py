import pygame
print('\033[1;31;40m~= TAL DO PLAYER =~\033[m\n' + '\033[1;31m-\033[m' * 19)
play = input('\033[1;31m•\033[mAperte \033[1;31mENTER\033[m para \033[1;32mCOMEÇAR\033[m a música!')
pygame.init()
pygame.mixer.music.load("ex021.mp3")
pygame.mixer.music.play()
pause = input('\033[1;31m-\033[m' * 19 + '\n\033[1;31m•\033[mAperte \033[1;31mENTER\033[m para'
                                         '\033[1;31m ENCERRAR\033[m a música!')
pygame.event.wait()
