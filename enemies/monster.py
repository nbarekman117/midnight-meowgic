from config import MONSTER_SPRITE_SHEET
from objects.game_object import GameObject
import pygame


class Monster(GameObject):
    def __init__(self, x, y):
        MONSTER_FRAME_WIDTH = 1000 // 4 
        MONSTER_FRAME_HEIGHT = 250

        self.frames = [
            MONSTER_SPRITE_SHEET.subsurface(
                pygame.Rect(i * MONSTER_FRAME_WIDTH, 0, MONSTER_FRAME_WIDTH, MONSTER_FRAME_HEIGHT)
            )
            for i in range(4)
        ]
        self.current_frame = 0
        super().__init__(x, y, self.frames[self.current_frame])
        self.animation_speed = 9
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
