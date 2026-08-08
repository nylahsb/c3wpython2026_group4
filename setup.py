import pygame


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
background = pygame.image.load("spacebg.png").convert()

running = True

while running:

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #drawing/rendering
    screen.blit(background, (0, 0))
    pygame.display.flip()
pygame.quit()

