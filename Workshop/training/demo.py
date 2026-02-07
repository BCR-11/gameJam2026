import pygame
import sys


pygame.init()
WIDTH = 1080
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My First Pygame!")

#CLOCK
clock = pygame.time.Clock()
FPS = 60

#COLORS
WHITE = (255, 255, 255)
BLUE = (60, 60, 255)
GREEN = (0, 255, 0)

#PLAYER
x = 100
y = 100
speed = 5
size = 50

running = True
while running:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    #wasd and arrows
    if keys[pygame.K_w]:
        y-= speed
    if keys[pygame.K_UP]:
        y-= speed

    if keys[pygame.K_s]:
        y+= speed

    if keys[pygame.K_DOWN]:
        y+= speed


    if keys[pygame.K_a]:
        x-= speed

    if keys[pygame.K_LEFT]:
        x-= speed

    if keys[pygame.K_d]:
        x+= speed

    if keys[pygame.K_RIGHT]:
        x+= speed

    #DRAWING
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, GREEN, (x, y, size, size))


    pygame.display.flip()


pygame.quit()
sys.exit()