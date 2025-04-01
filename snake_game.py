import pygame
import time
import random

pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")


WHITE, RED, GREEN, BLACK = (255, 255, 255), (213, 50, 80), (0, 255, 0), (0, 0, 0)

# Clock
clock = pygame.time.Clock()

def snake_game():
    game_over = False
    x, y = WIDTH // 2, HEIGHT // 2
    x_change, y_change = 0, 0
    snake = []
    snake_length = 1
    food_x = round(random.randrange(0, WIDTH - 10) / 10.0) * 10
    food_y = round(random.randrange(0, HEIGHT - 10) / 10.0) * 10

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change, y_change = -10, 0
                elif event.key == pygame.K_RIGHT:
                    x_change, y_change = 10, 0
                elif event.key == pygame.K_UP:
                    x_change, y_change = 0, -10
                elif event.key == pygame.K_DOWN:
                    x_change, y_change = 0, 10

        x += x_change
        y += y_change

        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_over = True

        win.fill(BLACK)
        pygame.draw.rect(win, GREEN, [food_x, food_y, 10, 10])

        snake.append([x, y])
        if len(snake) > snake_length:
            del snake[0]

        for segment in snake[:-1]:
            if segment == [x, y]:
                game_over = True

        for segment in snake:
            pygame.draw.rect(win, WHITE, [segment[0], segment[1], 10, 10])

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIDTH - 10) / 10.0) * 10
            food_y = round(random.randrange(0, HEIGHT - 10) / 10.0) * 10
            snake_length += 1

        pygame.display.update()
        clock.tick(15)

    pygame.quit()

snake_game()
