import pygame
from constants import WHITE, FONT_PATH


# Load the custom font or fallback to system font
def load_font(size):
    try:
        return pygame.font.Font(FONT_PATH, size)
    except FileNotFoundError:
        return pygame.font.Font(None, size)


# Class to display the score
class Score:
    def __init__(self):
        self.value = 0

    def update(self, points):
        self.value += points

    def draw(self, screen):
        font = load_font(30)
        score_text = font.render(f"Score: {self.value}", True, WHITE)
        screen.blit(score_text, (10, 10))


class HealthBar:
    def __init__(self, max_health, screen_width, screen_height):
        self.max_health = max_health
        self.current_health = max_health
        self.screen_width = screen_width
        self.screen_height = screen_height

    def take_damage(self, damage):
        self.current_health = max(0, self.current_health - damage)

    def draw(self, screen):
        # Health bar dimensions
        bar_length = 200
        bar_height = 20
        health_ratio = self.current_health / self.max_health

        bar_x = 100
        bar_y = self.screen_height - bar_height - 20

        # Draw background (red for lost health)
        pygame.draw.rect(screen, (255, 0, 0), (bar_x, bar_y, bar_length, bar_height))

        # Draw the remaining health (green)
        pygame.draw.rect(screen, (0, 255, 0), (bar_x, bar_y, bar_length * health_ratio, bar_height))

        # Render the "Health" label
        font = load_font(24)
        health_label_text = font.render("Health", True, WHITE)
        screen.blit(health_label_text, (10, bar_y))


# Function to draw level number
def draw_level_number(screen, level):
    font = load_font(36)
    level_text = font.render(f"Level {level}", True, WHITE)
    text_rect = level_text.get_rect(center=(screen.get_width() // 2, 20))
    screen.blit(level_text, text_rect)
