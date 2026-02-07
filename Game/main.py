import pygame, sys, random
from pygame.math import Vector2

pygame.init()

#FRUITS
class FRUIT:
    def __init__(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

    def draw_fruit (self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        pygame.draw.rect(screen, ('#ff0048') , fruit_rect)

#SCREEN 
cell_size = 40
cell_number = 20 # A 20 by 20 grid, 40 pixels each square.
screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))
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

fruit = FRUIT()

#FONT FOR WRITING (Pixelated)
pixel_font = pygame.font.Font('font/Minecraft.ttf', 80) # Directory + size
#Text
text = pixel_font.render('Game Over', False, (255, 255, 230))
text_rect = text.get_rect(center = (cell_number *cell_size/2, cell_number*cell_size/2))


running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0)) #fill screen in black
    screen.blit(text, text_rect)
    fruit.draw_fruit()

    keys = pygame.key.get_pressed()
    
        
    
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()