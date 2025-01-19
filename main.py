import pygame
from game import Game
from settings import Settings

def main():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Snake Game")

    game = Game(screen, settings)

    while True:
        game.handle_events()
        game.update()
        game.draw()

if __name__ == "__main__":
    main()