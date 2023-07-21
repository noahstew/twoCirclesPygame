# Pygame setup
import pygame

pygame.init()

# Window setup
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
WINDOW_DIM = (WINDOW_WIDTH, WINDOW_HEIGHT)
DISPLAY = pygame.display.set_mode(WINDOW_DIM)
pygame.display.set_caption("PyShooter")
FPS = 60
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

RED = (255, 0, 0)
ORANGE = (255, 128, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
LIGHT_BLUE = (0, 255, 255)
ROYAL_BLUE = (0, 128, 255)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 255)
PINK = (255, 0, 255)
MAGENTA = (255, 0, 128)

# Player
PLAYER_SPEED = 0.25
PLAYER_SIZE = 20
DASH_DISTANCE = 0.35
class Player:
    def __init__(self, x, y, color, controls):
        self.x = x
        self.y = y
        self.color = color
        self.controls = controls

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    def update(self, keys):
        # Player movement
        if self.controls == 1:
            if keys[pygame.K_w]:
                self.y -= PLAYER_SPEED
            if keys[pygame.K_s]:
                self.y += PLAYER_SPEED
            if keys[pygame.K_a]:
                self.x -= PLAYER_SPEED
            if keys[pygame.K_d]:
                self.x += PLAYER_SPEED
            if keys[pygame.K_w] and keys[pygame.K_SPACE]:
                self.y -= DASH_DISTANCE
            if keys[pygame.K_s] and keys[pygame.K_SPACE]:
                self.y += DASH_DISTANCE
            if keys[pygame.K_a] and keys[pygame.K_SPACE]:
                self.x -= DASH_DISTANCE
            if keys[pygame.K_d] and keys[pygame.K_SPACE]:
                self.x += DASH_DISTANCE

        if self.controls == 2:
            if keys[pygame.K_UP]:
                self.y -= PLAYER_SPEED
            if keys[pygame.K_DOWN]:
                self.y += PLAYER_SPEED
            if keys[pygame.K_LEFT]:
                self.x -= PLAYER_SPEED
            if keys[pygame.K_RIGHT]:
                self.x += PLAYER_SPEED

            if keys[pygame.K_UP] and keys[pygame.K_l]:
                self.y -= DASH_DISTANCE
            if keys[pygame.K_DOWN] and keys[pygame.K_l]:
                self.y += DASH_DISTANCE
            if keys[pygame.K_LEFT] and keys[pygame.K_l]:
                self.x -= DASH_DISTANCE
            if keys[pygame.K_RIGHT] and keys[pygame.K_l]:
                self.x += DASH_DISTANCE

        # Boundary check
        if self.x < PLAYER_SIZE:
            self.x = PLAYER_SIZE
        elif self.x + PLAYER_SIZE > WINDOW_WIDTH:
            self.x = WINDOW_WIDTH - PLAYER_SIZE

        if self.y < PLAYER_SIZE:
            self.y = PLAYER_SIZE
        elif self.y + PLAYER_SIZE > WINDOW_HEIGHT:
            self.y = WINDOW_HEIGHT - PLAYER_SIZE

    def draw(self):
        pygame.draw.circle(DISPLAY, self.color, (self.x, self.y), PLAYER_SIZE)

# Clock setup
clock = pygame.time.Clock()

# Running loop begins
running = True

player_one = Player(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, ROYAL_BLUE, 1)
player_two = Player(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, RED, 2)

while running:
    DISPLAY.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        clock.tick(FPS)
    keys = pygame.key.get_pressed()
    player_one.handle_events()
    player_one.update(keys)
    player_one.draw()
    player_two.handle_events()
    player_two.update(keys)
    player_two.draw()
    pygame.display.update()
pygame.quit()
