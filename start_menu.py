import pygame 

def start_menu(screen):

    WIDTH = 1000
    HEIGHT = 720
    FPS = 30

#pygame.init()

#Create window
#screen = pygame.display.set_mode((1000, 720))

#Set window caption
    pygame.display.set_caption("Start Menu")

#Load background image
    background_image = pygame.image.load("sprites/background.png").convert_alpha()
    background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))


#Create colors
    ORANGE = (255, 165, 0)
    WHITE = (255, 255, 255)
    DARK_BLUE = (0, 0, 139)

#Create title font
    title_font = pygame.font.SysFont("arial", 100, bold=True)
    menu_font= pygame.font.SysFont("arial", 40)
    instruction_font = pygame.font.SysFont("arial", 30)

#render title text
    space_text = title_font.render("SPACE", True, WHITE)
    explorer_text = title_font.render("EXPLORER", True, ORANGE)
    menu_text = menu_font.render("Press SPACE to start", True, WHITE)
    instruction_text1 = instruction_font.render("Use ARROW KEYS to move", True, WHITE)
    instruction_text2 = instruction_font.render("Visit all 3 planets to", True, WHITE)
    instruction_text3 = instruction_font.render("complete mission!", True, WHITE)

    #Rectangles for text

    button = pygame.Surface((500, 60), pygame.SRCALPHA)
    pygame.draw.rect(button, (0, 70, 170, 180), button.get_rect(), border_radius=10)

    button_rect = button.get_rect(center=(500, 400))

    box = pygame.Surface((500, 150), pygame.SRCALPHA)
    pygame.draw.rect(box, (0, 0, 0, 180), box.get_rect(), border_radius=10)

    pygame.draw.rect(box, WHITE, box.get_rect(), width=2, border_radius=10)

    box_rect = box.get_rect(center=(500, 540))

#Position text
    space_text_rect = space_text.get_rect(center=(500, 180))
    explorer_rect = explorer_text.get_rect(center=(500, 280))
    menu_text_rect = menu_text.get_rect(center=(500, 400),)
    instruction_text1_rect = instruction_text1.get_rect(center=(500, 500))
    instruction_text2_rect = instruction_text2.get_rect(center=(500, 540))
    instruction_text3_rect = instruction_text3.get_rect(center=(500, 580))

#Create game loop

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return "transition"

#Draw background
        screen.blit(background_image, (0, 0))


#Draw aspects
        screen.blit(background_image, (0, 0))
        screen.blit(space_text, space_text_rect)
        screen.blit(explorer_text, explorer_rect)

        screen.blit(button, button_rect)
        screen.blit(menu_text, menu_text_rect)

        screen.blit(box, box_rect)
        screen.blit(instruction_text1, instruction_text1_rect)
        screen.blit(instruction_text2, instruction_text2_rect)
        screen.blit(instruction_text3, instruction_text3_rect)

        pygame.display.flip()
    pygame.quit()

