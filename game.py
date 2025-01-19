# FILE: /snake-game/snake-game/src/game.py

import pygame
import random
from settings import *
from utils.score import Score
from utils.sound import Sound

class SnakeGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.running = True
        self.paused = False
        self.score = Score()
        self.sound = Sound()
        self.snake = [(100, 100), (90, 100), (80, 100)]
        self.snake_direction = (SNAKE_SPEED, 0)
        self.food_position = self.spawn_food()
        self.obstacles = self.create_obstacles()
        self.level = 1

    def spawn_food(self):
        x = random.randint(0, (SCREEN_WIDTH - FOOD_SIZE) // FOOD_SIZE) * FOOD_SIZE
        y = random.randint(0, (SCREEN_HEIGHT - FOOD_SIZE) // FOOD_SIZE) * FOOD_SIZE
        return (x, y)

    def create_obstacles(self):
        return [(200, 200), (300, 300), (400, 400)]  # Example static obstacles

    def move_snake(self):
        head_x, head_y = self.snake[0]
        new_head = (head_x + self.snake_direction[0], head_y + self.snake_direction[1])
        self.snake.insert(0, new_head)
        if new_head == self.food_position:
            self.score.increment()
            self.food_position = self.spawn_food()
            self.sound.play_eat_sound()
        else:
            self.snake.pop()

    def check_collisions(self):
        head = self.snake[0]
        if head in self.snake[1:] or head[0] < 0 or head[0] >= SCREEN_WIDTH or head[1] < 0 or head[1] >= SCREEN_HEIGHT:
            self.game_over()
        for obstacle in self.obstacles:
            if head == obstacle:
                self.game_over()

    def game_over(self):
        self.sound.play_game_over_sound()
        self.running = False

    def toggle_pause(self):
        self.paused = not self.paused

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        self.toggle_pause()
                    # Add control handling here

            if not self.paused:
                self.move_snake()
                self.check_collisions()

            self.screen.fill(BACKGROUND_COLOR)
            # Draw snake, food, and obstacles here
            pygame.display.flip()
            self.clock.tick(SNAKE_SPEED)

        pygame.quit()