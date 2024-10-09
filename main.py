import pygame
from constants import WIDTH, HEIGHT
from screens import show_start_screen
from game import run_game

if __name__ == "__main__":
    pygame.init()
    pygame.font.init()

    # Initialize the screen and pass it to the start screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    show_start_screen(screen)
    run_game()
