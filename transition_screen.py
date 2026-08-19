import pygame

def transition_screen(screen):

#pygame.init()

    WIDTH = 1000
    HEIGHT = 720
    FPS = 30

#screen = pygame.display.set_mode((WIDTH, HEIGHT))

    pygame.display.set_caption("Transition screen")

#Load background image
    background_image = pygame.image.load("sprites/background.png")
    background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))


#Create colors
    WHITE = (255, 255, 255)

#Create font
    title_font = pygame.font.SysFont("arial", 55, bold=True)

#Add text
    travel_text = title_font.render("Travelling to your new", True, WHITE)
    adventure_text = title_font.render("adventure....", True, WHITE)

#Position text
    travel_text_rect = travel_text.get_rect(center=(500, 320))
    adventure_text_rect = adventure_text.get_rect(center=(500,400))

    start_time = pygame.time.get_ticks()
    clock = pygame.time.Clock()

#Create game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

#Draw aspects
        screen.blit(background_image, (0, 0))
        screen.blit(travel_text, travel_text_rect)
        screen.blit(adventure_text, adventure_text_rect)

        pygame.display.flip()
        clock.tick(60)

    #After 1 second
        if pygame.time.get_ticks() - start_time >= 1000:
            return "game"

    pygame.quit()