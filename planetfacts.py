# All sprite classes for final project 
#+ planet facts
# import os
# import zipfile
import pygame
import random

WIDTH = 1000
HEIGHT = 720
FPS = 30


#colors
STAR_WHITE = (240, 248, 255)

EARTH_FACTS = [
    "Earth is the only known planet with liquid water on the surface.",
    "Earth is the only planet known to support life.",
    "Earth is the third planet from the Sun."
]

MARS_FACTS = [
    "Mars is the Red Planet, called so due to iron oxides or ferrihydrites found in the atmosphere.",
    "Mars has a very thin atmosphere made up entirely of Carbon Dioxide Co 2 and very cold temperatures of -80 o Celcius.",
    "Mars is 140 million miles from Earth (a 3 year Journey) 1 year on Mars is 687 days."
]

JUPITER_FACTS = [
    " Jupiter is the largest planet in the Solar System- named after an ancient Roman god",
    " Jupiter's stripes and swirls are windy clouds of ammonia and water, floating in an atmosphere of hydrogen and helium. ",
    " 1 day on Jupiter is 9.9 hours and a year is (4333 earth days- to go around the sun)",
    " Jupiter has 95 official moons. Its rings are small dark dust particles from interplanetary meteoroids which smashed into Jupiter’s small innermost moons."
]


# temp screen
pygame.init()
font = pygame.font.Font(None, 24)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Explorer")
clock = pygame.time.Clock()
background = pygame.image.load("spacebg.png").convert_alpha()
background = pygame.transform.scale(background, (1000, 720))
bg_image = pygame.transform.scale(bg_image, (800, 800))

class Cat(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("png/cat/Idle (1).png").convert_alpha()
        # self.frames = [
        #     pygame.image.load("idle_1.png").convert_alpha()
        #     pygame.image.load("idle_2.png").convert_alpha()
        #     pygame.image.load("idle_3.png").convert_alpha()
        # ]
        # self.fram_index = 0
        # self.animation_speed = 0.15
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()

        self.rect.x = 100
        self.rect.y = 100

        self.speed = 6

    # directions 1=up, 2=down, 3=left, 4=right
    def move(self, direction):
        if direction == 1:
            self.rect.y -= self.speed
        elif direction == 2:
            self.rect.y += self.speed
        elif direction == 3:
            self.rect.x -= self.speed
        elif direction == 4:
            self.rect.x += self.speed 


class Mars(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load(("planet05.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.rect = self.image.get_rect()

        self.rect.x = 700
        self.rect.y = 100

class Earth(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load(("planet03.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect()

        self.rect.x = 650
        self.rect.y = 400

class Jupiter(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load(("planet08.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (250, 250))
        self.rect = self.image.get_rect()

        self.rect.x = 100
        self.rect.y = 200

# class UFO(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()

#         self.image  = pygame.image.load("UFO.png").convert_alpha()
#         self.image = pygame.transform.scale(self.image, (125, 125))
#         self.rect = self.image.get_rect()

#         self.rect.x = 500
#         self.rect.y = 300
#         self.speed = 7

#         self.rect.x = random.randint(0, HEIGHT - self.rect.y)

#         self.speed_y = random.randint(8, 12)

#     def update(self):
#         # Move left by subtracting from the x coordinate
#         self.rect.x -= self.speed
        
#         # Check if the entire sprite has moved off the left edge
#         if self.rect.right < 0:
#             self.reset_position()

#     def reset_position(self):
#         # Place sprite just past the right edge of the screen
#         self.rect.x = WIDTH
#         # Assign a random vertical position
#         self.rect.y = random.randint(50, HEIGHT - 100)

    # def respawn(self):
    #     self.rect.x = random.randint(0, WIDTH - self.rect.width)
    #     self.rect.y = 0

    # def update(self):
    #     # Move across
    #     self.rect.x -= self.speed
    #     if self.rect.x > WIDTH:
    #         self.respawn()

class Star(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image  = pygame.image.load("star.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()

        self.rect.x = 650
        self.rect.y = 650

        self.rect.x = random.randint(100, 700)
        self.rect.y = random.randint(100, 700)

    def respawn(self):
        self.rect.x = random.randint(100, 700)
        self.rect.y = random.randint(100, 700)

        self.rect.x = max(0, min(self.rect.x, WIDTH - 100))
        self.rect.y = max(0, min(self.rect.y, HEIGHT - 100))

running = True

cat_idle = Cat()
mars = Mars()
earth = Earth()
jupiter = Jupiter()
# ufo = UFO()
star = Star()

SPAWN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_EVENT, 500)
score = 0
current_fact = "Explore the galaxy and find a planet to learn a fact!"
fact_timer = 0
FACT_COOLDOWN = 90

while running:

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
                # falling asteroids
        # elif event.type == SPAWN_EVENT: 
        #     falling_group.add(asteroid)

    # ufo.update()
    #controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        cat_idle.move(1)
    if keys[pygame.K_s]:
        cat_idle.move(2)
    if keys[pygame.K_a]:
        cat_idle.move(3)
    if keys[pygame.K_d]:
        cat_idle.move(4)

    if cat_idle.rect.colliderect(star.rect):
        star.respawn()
    #making sure the cat is near a planet to display a fact
    near_earth = abs(cat_idle.rect.x - earth.rect.x) < 60 and abs(cat_idle.rect.y - earth.rect.y) < 60
    near_mars = abs(cat_idle.rect.x - mars.rect.x) < 60 and abs(cat_idle.rect.y - mars.rect.y) < 60
    near_jupiter = abs(cat_idle.rect.x - jupiter.rect.x) < 80 and abs(cat_idle.rect.y - jupiter.rect.y) < 80
    #make sure the fact box only updates when the cat is near a planet and the cooldown timer has expired
    if fact_timer <= 0 and (near_earth or near_mars or near_jupiter):
        if near_earth:
            current_fact = random.choice(EARTH_FACTS)
        elif near_mars:
            current_fact = random.choice(MARS_FACTS)
        elif near_jupiter:
            current_fact = random.choice(JUPITER_FACTS)
        fact_timer = FACT_COOLDOWN

    if not (near_earth or near_mars or near_jupiter):
        current_fact = "Explore the galaxy and find a planet to learn a fact!"
        fact_timer = 0
    else:
        fact_timer -= 1
    #drawing the background and all the sprites
    screen.blit(background, (0, 0))
    screen.blit(mars.image, mars.rect)
    screen.blit(earth.image, earth.rect)
    screen.blit(jupiter.image, jupiter.rect)
    screen.blit(star.image, star.rect)
    screen.blit(cat_idle.image, cat_idle.rect)
    # screen.blit(ufo.image, ufo.rect)

    box_x = 30
    box_y = HEIGHT - 120
    box_width = 940
    box_height = 90
    #drawing the fact box
    pygame.draw.rect(screen, (20, 30, 60), (box_x, box_y, box_width, box_height), border_radius=12)
    pygame.draw.rect(screen, (120, 180, 255), (box_x, box_y, box_width, box_height), 2, border_radius=12)
    #displaying the fact box and facts
    title = font.render("Fact Box", True, STAR_WHITE)
    screen.blit(title, (box_x + 15, box_y + 8))

    fact_surface = font.render(current_fact, True, STAR_WHITE)
    screen.blit(fact_surface, (box_x + 15, box_y + 35))

    # score_text = font.render("Score: " + str(score), True, STAR_WHITE)
    # screen.blit(score_text, (20, 20))
    pygame.display.flip()

pygame.quit()


