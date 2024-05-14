import pygame
from game import Game
from screen import Screen

# Initialize PyGame
# setup for sounds_music, defaults are good
pygame.mixer.init()
pygame.init()
# create the screen object
pygame.display.set_mode((Screen.width, Screen.height))

# play
game = Game()
game.play()