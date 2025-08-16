import pygame
import sys

pygame.init()

# Ekran boyutu
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dinozor Oyunu")

# Renkler
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Dino ayarları
dino = pygame.Rect(50, 300, 50, 50)
gravity = 1
dino_y_velocity = 0
jumping = False

# Engel
obstacle = pygame.Rect(1000, 300, 50, 50)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN and not jumping:
            if event.key == pygame.K_SPACE:
                dino_y_velocity = -15
                jumping = True

    # Dino hareketi
    dino_y_velocity += gravity
    dino.y += dino_y_velocity
    if dino.y >= 300:
        dino.y = 300
        jumping = False

    # Engel hareketi
    obstacle.x -= 5
    if obstacle.x < -50:
        obstacle.x = 800

    # Çarpışma kontrolü
    if dino.colliderect(obstacle):
        print("Oyun Bitti!")
        pygame.quit()
        sys.exit()

    # Çizimler
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, dino)
    pygame.draw.rect(screen, BLACK, obstacle)
    pygame.display.update()

    clock.tick(60)
