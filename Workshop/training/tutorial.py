import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((1080, 720))
pygame.display.set_caption("TUTORIAL")
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

#SURFACE
#test_surface = pygame.Surface((100, 200))
#test_surface.fill('Red')
sky_surface = pygame.image.load('graphics/Sky.png').convert()
sky_surface = pygame.transform.scale(sky_surface, (1080, 533))
ground_surface = pygame.image.load('graphics/ground.png').convert()
ground_surface = pygame.transform.scale(ground_surface, (1080, 227))
text_surface = test_font.render("My game", False, 'Black') #Text + Antialising, aka smooth the edges or not + color
text_rect = text_surface.get_rect(center = (540, 100))

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (850, 500))

player_surface = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (150, 500))

#COLORS
WHITE = (255, 255, 255)
BLUE = (60, 60, 255)
GREEN = (0, 255, 0)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#    pygame.draw.rect(screen, GREEN, (100, 100, 100, 200))
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 500))
    screen.blit(text_surface, text_rect)
    snail_rect.left -= 8
    if snail_rect.right < 0:
        snail_rect.left = 1080
    screen.blit(snail_surface, snail_rect)
    player_rect.left +=4
    #print(player_rect.left) Find out which pixel, position in x or y (here x) is on that side of the rectangle (in this example the left of the player)
    if player_rect.right > 1180:
        player_rect.right = 0
    screen.blit(player_surface, player_rect)

    if player_rect.colliderect(snail_rect):
        print()

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()