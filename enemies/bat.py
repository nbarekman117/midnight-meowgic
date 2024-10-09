from config import BAT_SPRITE_SHEET, BAT_FRAME_WIDTH, BAT_FRAME_HEIGHT
from objects.game_object import GameObject
import pygame


class Bat(GameObject):
    def __init__(self, x, y):
        self.frames = [
            BAT_SPRITE_SHEET.subsurface(
                pygame.Rect(i * BAT_FRAME_WIDTH, 0, BAT_FRAME_WIDTH, BAT_FRAME_HEIGHT)
            )
            for i in range(BAT_SPRITE_SHEET.get_width() // BAT_FRAME_WIDTH)
        ]
        self.current_frame = 0
        super().__init__(x, y, self.frames[self.current_frame])
        self.animation_speed = 5
        self.animation_counter = 0

    # Updated move method signature
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
