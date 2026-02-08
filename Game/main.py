import pygame, sys, random
from pygame.math import Vector2

pygame.init()

class SNAKE:
    def __init__(self):
        self.body = [Vector2(10, 10), Vector2(9, 10), Vector2(8, 10)]
        self.direction = Vector2(1, 0) #Right direction
        self.new_block = False

    def draw_snake(self):
        for block in self.body:
            x_pos, y_pos = int(block.x * cell_size), int(block.y * cell_size)
            snake_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(screen, ('#008a4c'), snake_rect)

    def snake_movement (self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

#FRUITS
class FRUIT:
    def __init__(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

    def draw_fruit (self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        pygame.draw.rect(screen, ('#ff0048') , fruit_rect)
    
    def randomized(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()

    def update(self):
        self.snake.snake_movement()
        self.check_collision()

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()

    def check_collision(self):
        if self.fruit.pos ==  self.snake.body[0]:
            self.fruit.randomized()
            self.snake.add_block()


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
snakes_rect = snake_surf.get_rect(center = (x_pos, 360))

main_game = MAIN()

#FONT FOR WRITING (Pixelated)
pixel_font = pygame.font.Font('font/Minecraft.ttf', 80) # Directory + size
#Text
text = pixel_font.render('Game Over', False, (255, 255, 230))
text_rect = text.get_rect(center = (cell_number *cell_size/2, cell_number*cell_size/2))

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)


running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:
            running = False
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                main_game.snake.direction = Vector2(1, 0)
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                main_game.snake.direction = Vector2(-1, 0)

    screen.fill((0, 0, 0)) #fill screen in black
    screen.blit(text, text_rect)
    main_game.draw_elements()
    
        
    
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()