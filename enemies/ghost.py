from config import GHOST_SPRITE_SHEET
from objects.game_object import GameObject
import pygame


class Ghost(GameObject):
    def __init__(self, x, y):
        GHOST_FRAME_WIDTH = 256 // 4
        GHOST_FRAME_HEIGHT = 60

        self.frames = [
            GHOST_SPRITE_SHEET.subsurface(pygame.Rect(i * GHOST_FRAME_WIDTH, 0, GHOST_FRAME_WIDTH, GHOST_FRAME_HEIGHT))
            for i in range(4)
        ]
        self.current_frame = 0
        super().__init__(x, y, self.frames[self.current_frame])
        self.animation_speed = 6
        self.animation_counter = 0

    def move(self, dx=0, dy=0):
        self.x += dx

    def update_animation(self):
        self.animation_counter += 1
        if self.animation_counter >= self.animation_speed:
            self.animation_counter = 0
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.img = self.frames[self.current_frame]

    def draw(self, screen):
        self.update_animation()
        super().draw(screen)
