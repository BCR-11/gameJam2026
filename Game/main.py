import pygame
import sys
pygame.init()

#SCREEN 
screen = pygame.display.set_mode((1080, 720))
pygame.display.set_caption ("Snake")
#FPS
clock = pygame.time.Clock()

#Positions:
x_pos = 540
y_pos = 360
speed = 8


#Characters
snake_surf = pygame.transform.rotozoom(pygame.image.load('sprites/snake_headUP.png'), 0, 2)
snake_rect = snake_surf.get_rect(center = (x_pos, 360))


#FONT FOR WRITING (Pixelated)
pixel_font = pygame.font.Font('font/Minecraft.ttf', 80) # Directory + size
#Text
text = pixel_font.render('Game Over', False, (255, 255, 230))
text_rect = text.get_rect(center = (540, 360))




running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0)) #fill screen in black
    screen.blit(text, text_rect)

    keys = pygame.key.get_pressed()

        
    
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()