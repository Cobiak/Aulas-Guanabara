### FAÇA UM PROGRAMA EM PYTHON QUE ABRA E REPRODUZA O ÁUDIO DE UM ARQUIVO MP3.

import pygame     ####   módulo para criar jogos

pygame.init()
pygame.mixer.music.load('omae.mp3')   ### arquivo deve estar na pasta de projetos (conforme erro que aparecer)
pygame.mixer.music.play()
input()
pygame.event.wait()