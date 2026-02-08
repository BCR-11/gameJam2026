import pygame, sys, random
from pygame.math import Vector2

pygame.init()

class SNAKE:
    def __init__(self):
        self.body = [Vector2(10, 10), Vector2(9, 10), Vector2(8, 10)]
        self.direction = Vector2(1, 0) #RIGHT direction
        self.new_block = False

        self.snake_headUP = pygame.transform.scale(pygame.image.load('sprites/snake_headUP.png'), (40, 40))
        self.snake_headDOWN = pygame.transform.scale(pygame.image.load('sprites/snake_headDOWN.png'), (40, 40))
        self.snake_headRIGHT = pygame.transform.scale(pygame.image.load('sprites/snake_headRIGHT.png'), (40, 40))
        self.snake_headLEFT = pygame.transform.scale(pygame.image.load('sprites/snake_headLEFT.png'), (40, 40))
        self.snake_tailUP = pygame.transform.scale(pygame.image.load('sprites/snake_tailUP.png'), (40, 40))
        self.snake_tailDOWN = pygame.transform.scale(pygame.image.load('sprites/snake_tailDOWN.png'), (40, 40))
        self.snake_tailRIGHT = pygame.transform.scale(pygame.image.load('sprites/snake_tailRIGHT.png'), (40, 40))
        self.snake_tailLEFT = pygame.transform.scale(pygame.image.load('sprites/snake_tailLEFT.png'), (40, 40))
        self.snake_body = pygame.transform.scale(pygame.image.load('sprites/snake_body.png'), (40, 40))

    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()
        
        for index, block in enumerate(self.body):
            x_pos, y_pos = int(block.x * cell_size), int(block.y * cell_size)
            snake_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            if index == 0:
                screen.blit(self.snake_head, snake_rect)
            
            elif index == len(self.body) - 1:
                screen.blit(self.snake_tail, snake_rect)
            
            else:
                screen.blit(self.snake_body, snake_rect)

    def update_head_graphics(self):
        head_relative = self.body[1] - self.body[0]
        if head_relative == Vector2(1, 0):
            self.snake_head = self.snake_headLEFT
        if head_relative == Vector2(-1, 0):
            self.snake_head = self.snake_headRIGHT
        if head_relative == Vector2(0, 1):
            self.snake_head = self.snake_headUP
        if head_relative == Vector2(0, -1):
            self.snake_head = self.snake_headDOWN

    def update_tail_graphics(self):
        tail_relative = self.body[-1] - self.body[-2]
        if tail_relative == Vector2(1, 0):
            self.snake_tail = self.snake_tailLEFT
        if tail_relative == Vector2(-1, 0):
            self.snake_tail = self.snake_tailRIGHT
        if tail_relative == Vector2(0, 1):
            self.snake_tail = self.snake_tailUP
        if tail_relative == Vector2(0, -1):
            self.snake_tail = self.snake_tailDOWN 

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


class FRUIT:
    def __init__(self):
        self.x = random.randint(1, cell_number - 2)
        self.y = random.randint(1, cell_number - 2)
        self.pos = Vector2(self.x, self.y)

    def draw_fruit (self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        screen.blit(apple, fruit_rect) 
    
    def randomized(self):
        self.x = random.randint(1, cell_number - 2)
        self.y = random.randint(1, cell_number - 2)
        self.pos = Vector2(self.x, self.y)

apple = pygame.transform.scale(pygame.image.load('sprites/Red_apple.png'), (40, 40))

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()

    def update(self):
        self.snake.snake_movement()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()
        self.check_fail()

    def check_collision(self):
        if self.fruit.pos ==  self.snake.body[0]:
            self.fruit.randomized()
            self.snake.add_block()
    
    def check_fail(self):
        if not 1 <= self.snake.body[0].x < cell_number-1:
            self.game_over()
        if not 1 <= self.snake.body[0].y < cell_number-1:
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def draw_score(self):
        score_text = small_pixel_font.render(f'Score: {len(self.snake.body)-3}', False, (255, 255, 230))
        score_x = int(cell_number*cell_size - 50)
        score_y = 70
        score_rect = score_text.get_rect (midright = (score_x, score_y))
       #screen.blit(score_text, (cell_size*cell_number - 150, 60))
        screen.blit(score_text, score_rect)
        apple_rect = apple.get_rect(midright = (score_rect.left+11, score_rect.centery+6))
        screen.blit(pygame.transform.scale(apple, (20, 20)), apple_rect)

    def game_over(self):
        screen.blit(text, text_rect)

#SCREEN 
cell_size = 40
cell_number = 22 # A 22 by 22 grid, 40 pixels each square.
screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))
pygame.display.set_caption ("Snake")

wall = pygame.transform.scale(pygame.image.load('sprites/Wall.png'), (40, 40))

#FPS
clock = pygame.time.Clock()

#Positions:
x_pos = 540
y_pos = 360
speed = 8


main_game = MAIN()

#FONT FOR WRITING (Pixelated)
pixel_font = pygame.font.Font('font/Minecraft.ttf', 80) # Directory + size
small_pixel_font = pygame.font.Font('font/Minecraft.ttf', 20) # Directory + size

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
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)

    screen.fill((0, 0, 0))
    main_game.draw_elements()
    i = 0
    while i < 22:
        screen.blit(pygame.transform.rotozoom(wall, 270, 1), (0, i*cell_size))
        screen.blit(pygame.transform.rotozoom(wall, 270, 1), (cell_size*(cell_number-1), i*cell_size))
        screen.blit(wall, (i*cell_size, 0))
        screen.blit(wall, (i*cell_size, cell_size*(cell_number-1)))
        i += 1
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()