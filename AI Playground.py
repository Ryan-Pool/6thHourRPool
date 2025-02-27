import pygame
import random

# Initialize pygame
pygame.init()

# Set up game constants
WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Snake and food initialization
snake = [(100, 100), (90, 100), (80, 100)]
snake_dir = (GRID_SIZE, 0)
food = (random.randint(0, (WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE,
        random.randint(0, (HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE)
clock = pygame.time.Clock()
game_over = False

# Game loop
while not game_over:
    screen.fill(BLACK)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_dir != (0, GRID_SIZE):
                snake_dir = (0, -GRID_SIZE)
            elif event.key == pygame.K_DOWN and snake_dir != (0, -GRID_SIZE):
                snake_dir = (0, GRID_SIZE)
            elif event.key == pygame.K_LEFT and snake_dir != (GRID_SIZE, 0):
                snake_dir = (-GRID_SIZE, 0)
            elif event.key == pygame.K_RIGHT and snake_dir != (-GRID_SIZE, 0):
                snake_dir = (GRID_SIZE, 0)

    # Move snake
    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])

    # Check for collisions
    if (new_head in snake or
            new_head[0] < 0 or new_head[0] >= WIDTH or
            new_head[1] < 0 or new_head[1] >= HEIGHT):
        game_over = True
        break

    snake.insert(0, new_head)

    # Check if food is eaten
    if new_head == food:
        food = (random.randint(0, (WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE,
                random.randint(0, (HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE)
    else:
        snake.pop()

    # Draw food
    pygame.draw.rect(screen, RED, (food[0], food[1], GRID_SIZE, GRID_SIZE))

    # Draw snake
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))

    pygame.display.flip()
    clock.tick(10)

pygame.quit()
