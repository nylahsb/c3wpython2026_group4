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
    elif current_screen == "game":
        current_screen = (spriteclassesforfinalproject.spriteclassesforfinalproject(screen))

    #drawing/rendering
    
    pygame.display.flip()

pygame.quit()

