import pygame


class GameObject:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)  # Use mask for precise collision detection
        self.rect = self.img.get_rect(topleft=(self.x, self.y))

    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))
        self.rect.topleft = (self.x, self.y)  # Update the rect position

    def get_width(self):
        return self.img.get_width()

    def get_height(self):
        return self.img.get_height()
