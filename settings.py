# FILE: /snake-game/snake-game/src/settings.py
INITIAL_SPEED = 15  # Initial speed of the snake
SCREEN_WIDTH = 800  # Width of the game window
SCREEN_HEIGHT = 600  # Height of the game window
BACKGROUND_COLOR = (0, 0, 0)  # RGB color for the background
SNAKE_COLOR = (0, 255, 0)  # RGB color for the snake
FOOD_COLOR = (255, 0, 0)  # RGB color for the food
OBSTACLE_COLOR = (255, 255, 0)  # RGB color for obstacles

# Control mappings
CONTROLS = {
    "UP": "w",
    "DOWN": "s",
    "LEFT": "a",
    "RIGHT": "d",
    "PAUSE": "p",
    "RESTART": "r"
}

# Game settings
MAX_LEVELS = 3  # Total number of levels in the game
SCORE_INCREMENT = 10  # Points awarded for eating food
GAME_OVER_SCREEN_DURATION = 3000  # Duration of the game over screen in milliseconds