import pygame
from constants import WIDTH


class Background:
    def __init__(self, image_path):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (
            WIDTH, pygame.display.get_surface().get_height()))
        self.x1 = 0
        self.x2 = WIDTH
        self.scroll_speed = 1

    def update(self):
        self.x1 -= self.scroll_speed
        self.x2 -= self.scroll_speed

        if self.x1 <= -WIDTH:
            self.x1 = WIDTH
        if self.x2 <= -WIDTH:
            self.x2 = WIDTH

    def draw(self, screen):
        screen.blit(self.image, (self.x1, 0))
        screen.blit(self.image, (self.x2, 0))
