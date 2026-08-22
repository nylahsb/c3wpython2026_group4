import os

import pygame


import start_menu
import transition_screen
import spriteclassesforfinalproject

#constants

WIDTH = 1000
HEIGHT = 720
FPS = 30

#initializing pygame and making the game window

pygame.init()
pygame.mixer.init()

music_folder = os.path.dirname(__file__)
menu_music_file = os.path.join(
    music_folder,
    "3. Goodbye Sweet Alien.wav",
)
game_music_file = os.path.join(
    music_folder,
    "2. Satellite Interruption.wav",
)
if os.path.exists(menu_music_file):
    pygame.mixer.music.load(menu_music_file)
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(loops=-1, start=25)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Explorer")
clock = pygame.time.Clock()

current_screen = "start"

running = True

while running:

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    if current_screen == "start":
        current_screen = start_menu.start_menu(screen)
    elif current_screen == "transition":
        current_screen = transition_screen.transition_screen(screen)
        if current_screen == "game" and os.path.exists(game_music_file):
            pygame.mixer.music.load(game_music_file)
            pygame.mixer.music.play(-1)
    elif current_screen == "game":
        current_screen = (spriteclassesforfinalproject.spriteclassesforfinalproject(screen))

    #drawing/rendering
    
    pygame.display.flip()

pygame.quit()

