# All sprite classes for final project 
import pygame
import random
import math

def spriteclassesforfinalproject(screen):

    WIDTH = 1000
    HEIGHT = 720
    FPS = 30

# temp screen
    #pygame.init()

    #screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Space Explorer")
    clock = pygame.time.Clock()
    background = pygame.image.load("sprites/space.png").convert_alpha()
    background = pygame.transform.scale(background, (1000, 720))
# bg_image = pygame.transform.scale(bg_image, (800, 800))

# Fonts for the planet discovery card
    discovery_font = pygame.font.Font(None, 55)
    planet_name_font = pygame.font.Font(None, 48)
    fact_font = pygame.font.Font(None, 27)
    small_font = pygame.font.Font(None, 25)
    board_font = pygame.font.Font(None, 34)

    PLANET_FACTS = {
        "Mars": (
            "Mars is the Red Planet, called so due to iron oxides "
            "or ferrihydrites found in the atmosphere.",
            "Mars has a very thin atmosphere made up entirely of Carbon Dioxide "
            "Co 2 and very cold temperatures of -80 o Celcius.",
            "Mars is 140 million miles from Earth (a 3 year Journey)"
            "1 year on Mars is 687 days."
        ),
        "Earth": (
            "Earth is the only known planet with liquid water "
            "on the surface.",
            "Earth is the only planet known to support life.",
            "Earth is the third planet from the Sun."
        ),
        "Jupiter": (
            "Jupiter's stripes and swirls are windy clouds of ammonia"
            "and water, floating in an atmosphere of hydrogen and helium.",
            "1 day on Jupiter is 9.9 hours and a year is (4333 earth days- "
            "to go around the sun)",
            "Jupiter has 95 official moons. Its rings are small dark dust particles "
            "from interplanetary meteoroids which smashed into Jupiter's small "
            "innermost moons."
        )
}

    class Cat(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load("sprites/idle_1.png").convert_alpha()
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

            self.image = pygame.image.load("sprites/planet08.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (200, 200))
            self.rect = self.image.get_rect()

            self.rect.x = 100
            self.rect.y = 200

    class Earth(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()

            self.image = pygame.image.load("sprites/planet03.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (150, 150))
            self.rect = self.image.get_rect()

            self.rect.x = 650
            self.rect.y = 400

    class Jupiter(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()

            self.image = pygame.image.load("sprites/planet05.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (250, 250))
            self.rect = self.image.get_rect()

            self.rect.x = 700
            self.rect.y = 100

    class UFO(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()

            self.image  = pygame.image.load("sprites/UFO.png").convert_alpha()
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

            self.image  = pygame.image.load("sprites/star.png").convert_alpha()
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

    show_fact = False
    current_planet = ""
    current_fact = ""
    current_planet_image = None

    discovered_planets = set()

    planet_can_trigger = True

    # Round information
    MAX_LIVES = 3
    STAR_GOAL = 20

    lives = MAX_LIVES
    score = 0

    mission_complete = False
    mission_complete_time = 0

    # Prevent one UFO collision from removing every life
    last_ufo_hit_time = 0
    UFO_HIT_COOLDOWN = 1200

    SPAWN_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(SPAWN_EVENT, 500)

    def reached_planet_center(cat, planet):
        x_distance = cat.rect.centerx - planet.rect.centerx
        y_distance = cat.rect.centery - planet.rect.centery

        distance = math.hypot(x_distance, y_distance)

        center_radius = min(
            planet.rect.width,
            planet.rect.height
        ) * 0.25

        return distance <= center_radius

    def draw_wrapped_text(surface, text, font, color, center_x, start_y, max_width):
        words = text.split()
        lines = []
        current_line = ""

        for word in words:
            test_line = current_line + word + " "
            test_surface = font.render(test_line, True, color)

            if test_surface.get_width() <= max_width:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word + " "

        if current_line:
            lines.append(current_line)

        y = start_y

        for line in lines:
            line_surface = font.render(line.strip(), True, color)
            line_rect = line_surface.get_rect(
                center=(center_x, y)
            )
            surface.blit(line_surface, line_rect)
            y += line_surface.get_height() + 7

        return y


    while running:

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                # falling asteroids
        # elif event.type == SPAWN_EVENT: 
        #     falling_group.add(asteroid)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and show_fact:
                    show_fact = False

        # Only move the UFO and player when a fact is not showing
        if not show_fact and not mission_complete:
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


        # Collect a star
        
        if (
            not show_fact
            and not mission_complete
            and score < STAR_GOAL
            and cat_idle.rect.colliderect(star.rect)
        ):
            score += 1

            if score < STAR_GOAL:
                star.respawn()


        # Check for a collision with the UFO
        current_time = pygame.time.get_ticks()

        if (
            not show_fact
            and not mission_complete
            and current_time - last_ufo_hit_time
            >= UFO_HIT_COOLDOWN
            and pygame.sprite.collide_mask(cat_idle, ufo)
        ):
            lives -= 1
            last_ufo_hit_time = current_time

            # Move the cat and UFO apart after the collision
            cat_idle.rect.x = 100
            cat_idle.rect.y = 100
            ufo.reset_position()

            # Start the round again after losing every life
            if lives <= 0:
                lives = MAX_LIVES
                score = 0

                cat_idle.rect.x = 100
                cat_idle.rect.y = 100

                star.respawn()
                ufo.reset_position()

        # Check whether the cat is near each planet's center
        touching_mars = reached_planet_center(cat_idle, mars)

        touching_earth = reached_planet_center(cat_idle, earth)

        touching_jupiter = reached_planet_center(cat_idle, jupiter)

        # Open a fact only once per approach
        if not show_fact and planet_can_trigger:

            if touching_mars:
                current_planet = "Mars"
                current_fact = random.choice(PLANET_FACTS["Mars"])
                current_planet_image = mars.image

                discovered_planets.add("Mars")
                show_fact = True
                planet_can_trigger = False

            elif touching_earth:
                current_planet = "Earth"
                current_fact = random.choice(PLANET_FACTS["Earth"])
                current_planet_image = earth.image

                discovered_planets.add("Earth")
                show_fact = True
                planet_can_trigger = False

            elif touching_jupiter:
                current_planet = "Jupiter"
                current_fact = random.choice(PLANET_FACTS["Jupiter"])
                current_planet_image = jupiter.image

                discovered_planets.add("Jupiter")
                show_fact = True
                planet_can_trigger = False

        # Allow another fact after the cat leaves the planet
        if not (touching_mars
            or touching_earth
            or touching_jupiter):
            planet_can_trigger = True



        # Complete the mission after meeting both goals
        if (
            not show_fact
            and not mission_complete
            and score >= STAR_GOAL
            and len(discovered_planets) == 3
        ):
            mission_complete = True
            mission_complete_time = pygame.time.get_ticks()

        # Begin another round after three seconds
        if (
            mission_complete
            and pygame.time.get_ticks()
            - mission_complete_time >= 3000
        ):
            mission_complete = False

            # Reset only the round information
            score = 0
            lives = MAX_LIVES

            cat_idle.rect.x = 100
            cat_idle.rect.y = 100

            star.respawn()
            ufo.reset_position()

            # Planet discoveries intentionally do not reset
            planet_can_trigger = True


        screen.blit(background, (0, 0))
        screen.blit(mars.image, mars.rect)
        screen.blit(earth.image, earth.rect)
        screen.blit(jupiter.image, jupiter.rect)

        # Hide the star after collecting all 20
        if score < STAR_GOAL:
            screen.blit(star.image, star.rect)

        screen.blit(cat_idle.image, cat_idle.rect)
        screen.blit(ufo.image, ufo.rect)

        # Top scoreboard background
        scoreboard = pygame.Surface(
            (940, 55),
            pygame.SRCALPHA
        )

        pygame.draw.rect(
            scoreboard,
            (10, 18, 55, 210),
            scoreboard.get_rect(),
            border_radius=15
        )

        screen.blit(scoreboard, (30, 15))

        # Star score
        score_text = board_font.render(
            f"Stars: {score}/{STAR_GOAL}",
            True,
            (255, 205, 75)
        )

        screen.blit(score_text, (55, 33))

        # Lives
        lives_text = board_font.render(
            f"Lives: {lives}",
            True,
            (255, 255, 255)
        )

        screen.blit(lives_text, (445, 33))

        # Planet progress
        planets_text = board_font.render(
            f"Planets: {len(discovered_planets)}/3",
            True,
            (120, 220, 255)
        )

        screen.blit(planets_text, (780, 33))

        # Green checkmark when all planets are discovered
        if len(discovered_planets) == 3:
            check_center = (930, 43)

            pygame.draw.circle(
                screen,
                (65, 190, 100),
                check_center,
                11
            )

            pygame.draw.line(
                screen,
                (255, 255, 255),
                (925, 43),
                (929, 47),
                3
            )

            pygame.draw.line(
                screen,
                (255, 255, 255),
                (929, 47),
                (936, 38),
                3
            )

        # Draw the planet discovery card
                # Draw the planet discovery card
        if show_fact:

            # Darken the gameplay behind the card
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            overlay.fill((5, 5, 25, 155))
            screen.blit(overlay, (0, 0))

            # Main card
            card_rect = pygame.Rect(200, 45, 600, 630)

            pygame.draw.rect(screen, (10, 18, 55), card_rect, border_radius=30)

            # Gold card border
            pygame.draw.rect(screen, (255, 205, 75), card_rect, width=3, border_radius=30)

            # Planet Discovered heading
            discovery_title = discovery_font.render("PLANET DISCOVERED!", True, (255, 205, 75))

            discovery_title_rect = discovery_title.get_rect(
                center=(WIDTH // 2, 95)
            )

            screen.blit(discovery_title, discovery_title_rect)

            # Large planet image
            card_planet_image = pygame.transform.smoothscale(current_planet_image, (170, 170))

            card_planet_rect = card_planet_image.get_rect(center=(WIDTH // 2, 215))

            screen.blit(card_planet_image, card_planet_rect)

            # Planet name
            planet_name_text = planet_name_font.render(current_planet.upper(), True, (255, 255, 255))

            planet_name_rect = planet_name_text.get_rect(center=(WIDTH // 2, 325))

            screen.blit(planet_name_text, planet_name_rect)

            # Educational fact
            draw_wrapped_text(screen, current_fact, fact_font, (235, 235, 245), WIDTH // 2, 370, 500)

            # Left side of gold divider
            pygame.draw.line(screen,
                (255, 205, 75),
                (290, 465),
                (470, 465), 2)

            # Circle in the middle of divider
            pygame.draw.circle(screen,
                (255, 205, 75),
                (500, 465), 6)

            # Right side of gold divider
            pygame.draw.line(screen,
                (255, 205, 75),
                (530, 465),
                (710, 465), 2)

            # Discovery progress text
            progress_message = (f"{len(discovered_planets)} of 3 "
                "planets discovered")

            progress_text = small_font.render(progress_message, True, (255, 205, 75))

            progress_rect = progress_text.get_rect(center=(WIDTH // 2, 505))

            screen.blit(progress_text, progress_rect)

            # Information for the three small icons
            planet_icons = [
                ("Mars", mars.image),
                ("Earth", earth.image),
                ("Jupiter", jupiter.image)
            ]

            icon_positions = [
                420,
                500,
                580
            ]

            # Draw each small planet
            for index, planet_information in enumerate(
                planet_icons):
                planet_name = planet_information[0]
                planet_image = planet_information[1]

                icon = pygame.transform.smoothscale(planet_image, (55, 55))

                # Fade planets that haven't been discovered
                if planet_name not in discovered_planets:
                    icon = icon.copy()
                    icon.set_alpha(65)
                    border_color = (80, 85, 110)

                else:
                    border_color = (255, 205, 75)

                icon_rect = icon.get_rect(center=(icon_positions[index], 565))

                # Circle around each icon
                pygame.draw.circle(screen, border_color, icon_rect.center, 34, 3)

                screen.blit(icon, icon_rect)

            # Continue instruction
            continue_text = small_font.render("Press SPACE to continue", True, (255, 255, 255))

            continue_rect = continue_text.get_rect(center=(WIDTH // 2, 630))

            screen.blit(continue_text, continue_rect)


                    # Mission Complete screen
        if mission_complete:

            complete_overlay = pygame.Surface(
                (WIDTH, HEIGHT),
                pygame.SRCALPHA
            )

            complete_overlay.fill((5, 5, 25, 210))
            screen.blit(complete_overlay, (0, 0))

            complete_box = pygame.Rect(
                220,
                190,
                560,
                340
            )

            pygame.draw.rect(
                screen,
                (10, 18, 55),
                complete_box,
                border_radius=30
            )

            pygame.draw.rect(
                screen,
                (255, 205, 75),
                complete_box,
                width=4,
                border_radius=30
            )

            complete_title = discovery_font.render(
                "MISSION COMPLETE!",
                True,
                (255, 205, 75)
            )

            complete_title_rect = complete_title.get_rect(
                center=(WIDTH // 2, 270)
            )

            screen.blit(
                complete_title,
                complete_title_rect
            )

            complete_message = fact_font.render(
                "You collected 20 stars and explored every planet!",
                True,
                (255, 255, 255)
            )

            complete_message_rect = complete_message.get_rect(
                center=(WIDTH // 2, 345)
            )

            screen.blit(
                complete_message,
                complete_message_rect
            )

            next_round_text = small_font.render(
                "A new round will begin...",
                True,
                (150, 210, 255)
            )

            next_round_rect = next_round_text.get_rect(
                center=(WIDTH // 2, 415)
            )

            screen.blit(
                next_round_text,
                next_round_rect
            )

        pygame.display.flip()

pygame.quit()