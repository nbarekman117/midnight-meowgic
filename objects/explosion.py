import pygame
from config import EXPLOSION_SPRITE_SHEET, EXPLOSION_FRAME_WIDTH, EXPLOSION_FRAME_HEIGHT
from objects.game_object import GameObject


class Explosion(GameObject):
    def __init__(self, x, y):
        self.frames = [EXPLOSION_SPRITE_SHEET.subsurface(
            pygame.Rect(i * EXPLOSION_FRAME_WIDTH, 0, EXPLOSION_FRAME_WIDTH, EXPLOSION_FRAME_HEIGHT)) for i in
            range(EXPLOSION_SPRITE_SHEET.get_width() // EXPLOSION_FRAME_WIDTH)]
        self.current_frame = 0
        super().__init__(x, y, self.frames[self.current_frame])
        self.animation_speed = 1
        self.animation_counter = 0
        self.finished = False

    def update_animation(self):
        if not self.finished:
            self.animation_counter += 1
            if self.animation_counter >= self.animation_speed:
                self.animation_counter = 0
                self.current_frame += 1
                if self.current_frame >= len(self.frames):
                    self.finished = True
                else:
                    self.img = self.frames[self.current_frame]

    def draw(self, screen):
        self.update_animation()
        if not self.finished:
            super().draw(screen)
