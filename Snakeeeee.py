import pygame
import random
# initializing pygame
pygame.init()
#colors
white = (255, 255, 255) #rgb format
red = (255, 0, 0)
blue = (0,0,0)
# creating windown
screen_width = 900
screen_height = 600
gameWindown = pygame.display.set_mode((screen_width,screen_height))
#game title
pygame.display.set_caption("Anaconda")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindown.blit(screen_text, [x, y])
def plot_snake(gameWindown, color, snake_list, snake_size):
    for x,y in snake_list:
        pygame.draw.rect(gameWindown, color, [x,y,snake_size,snake_size])
#game loop
def gameloop():
    exit_game= False
    game_over=False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snake_list = []
    snake_length = 1
    food_x = random.randint(20, screen_width -20)
    food_y = random.randint(60, screen_height -20)
    score = 0
    init_velocity = 4
    snake_size = 30
    fps =60 # frames per second
    while not exit_game:
        if game_over:
            gameWindown.fill(white)
            text_screen("Game Over! Press Enter To Continue", red, 100, 250)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_x = - init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_DOWN:
                        velocity_x = init_velocity
                        velocity_y = 0
            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y
            if abs(snake_x - food_x)<10 and abs(snake_y - food_y)<10:
                score +=1
                food_x = random.randint(20, screen_width - 30)
                food_y = random.randint(60, screen_height - 30)
                snake_length +=5
            gameWindown.fill(white)
            text_screen("Score: " + str(score * 10), red, 5, 5)
            pygame.draw.rect(gameWindown, red, [food_x, food_y, snake_size, snake_size])
            pygame.draw.line(gameWindown, red, (0, 40), (900, 40), 5)
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)
            if len(snake_list)>snake_length:
                del snake_list[0]
            if head in snake_list[:-1]:
                game_over = True
            if snake_x < 0 or snake_x > screen_width -20 or snake_y <50 or snake_y > screen_height-20:
                game_over = True
            plot_snake(gameWindown, blue, snake_list, snake_size)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()
gameloop()


