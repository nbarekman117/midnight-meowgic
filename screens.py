import pygame
from ui import load_font
from constants import WIDTH, HEIGHT, WHITE, PURPLE, RED, BLACK, LOAD_BACKGROUND_PATH


def show_start_screen(screen):
    background_img = pygame.image.load(LOAD_BACKGROUND_PATH)
    background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

    halloween_font = load_font(80)
    instruction_font = load_font(40)

    shadow_color = BLACK
    shadow_offset = (5, 5)

    screen.blit(background_img, (0, 0))

    title_text = halloween_font.render("Midnight Meowgic", True, PURPLE)
    title_shadow = halloween_font.render("Midnight Meowgic", True, shadow_color)

    title_position = (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 4)

    screen.blit(title_shadow, (title_position[0] + shadow_offset[0], title_position[1] + shadow_offset[1]))
    screen.blit(title_text, title_position)

    instruction_text = instruction_font.render("Press any key to start", True, WHITE)
    screen.blit(instruction_text, (WIDTH // 2 - instruction_text.get_width() // 2, HEIGHT // 2))

    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYUP:
                waiting = False


def show_game_over_screen(screen):
    game_over_font = load_font(100)
    game_over_text = game_over_font.render("Game Over", True, RED)
    screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2))
    pygame.display.flip()
    pygame.time.wait(3000)


def show_game_win_screen(screen):
    win_font = load_font(100)
    win_text = win_font.render("You Win!", True, PURPLE)
    screen.blit(win_text, (WIDTH // 2 - win_text.get_width() // 2, HEIGHT // 2))
    pygame.display.flip()
    pygame.time.wait(3000)
