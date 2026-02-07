import pygame
from apple import Apple

A = Apple(3, 2)
print(A.coord)
A.randomize(12, 12)
print(A.coord)

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
