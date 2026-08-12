# All sprite classes for final project 
import pygame
import random

WIDTH = 1000
HEIGHT = 720
FPS = 30

# temp screen
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Explorer")
clock = pygame.time.Clock()
background = pygame.image.load("space_explorer_bg.png").convert_alpha()
background = pygame.transform.scale(background, (1000, 720))
# bg_image = pygame.transform.scale(bg_image, (800, 800))

class Cat(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("idle_1.png").convert_alpha()
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

        self.image = pygame.image.load("planet05.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.rect = self.image.get_rect()

        self.rect.x = 700
        self.rect.y = 100

class Earth(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("planet03.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect()

        self.rect.x = 650
        self.rect.y = 400

class Jupiter(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("planet08.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (250, 250))
        self.rect = self.image.get_rect()

        self.rect.x = 100
        self.rect.y = 200

class UFO(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image  = pygame.image.load("UFO.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (125, 125))
        self.rect = self.image.get_rect()

        self.rect.x = 500
        self.rect.y = 300
        self.speed = 7

        self.rect.x = random.randint(0, HEIGHT - self.rect.y)

        self.speed_y = random.randint(8, 12)

    def update(self):
        # Move left by subtracting from the x coordinate
        self.rect.x -= self.speed
        
        # Check if the entire sprite has moved off the left edge
        if self.rect.right < 0:
            self.reset_position()

    def reset_position(self):
        # Place sprite just past the right edge of the screen
        self.rect.x = WIDTH
        # Assign a random vertical position
        self.rect.y = random.randint(50, HEIGHT - 100)

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
ufo = UFO()
star = Star()

SPAWN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_EVENT, 500)

while running:

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
                # falling asteroids
        # elif event.type == SPAWN_EVENT: 
        #     falling_group.add(asteroid)

    ufo.update()

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
        # score += 1
        star.respawn()

    screen.blit(background, (0, 0))
    screen.blit(mars.image, mars.rect)
    screen.blit(earth.image, earth.rect)
    screen.blit(jupiter.image, jupiter.rect)
    screen.blit(star.image, star.rect)
    screen.blit(cat_idle.image, cat_idle.rect)
    screen.blit(ufo.image, ufo.rect)
    pygame.display.flip()

pygame.quit()


