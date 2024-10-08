from config import BAT_SPRITE_SHEET, BAT_FRAME_WIDTH, BAT_FRAME_HEIGHT, EXPLOSION_SPRITE_SHEET, EXPLOSION_FRAME_WIDTH, \
    EXPLOSION_FRAME_HEIGHT, GHOST_SPRITE_SHEET, MONSTER_SPRITE_SHEET
from game_object import GameObject
import pygame


# Regular bat enemy
class Enemy(GameObject):
    def __init__(self, x, y):
        self.frames = [
            BAT_SPRITE_SHEET.subsurface(pygame.Rect(i * BAT_FRAME_WIDTH, 0, BAT_FRAME_WIDTH, BAT_FRAME_HEIGHT)) for i in
            range(BAT_SPRITE_SHEET.get_width() // BAT_FRAME_WIDTH)]
        self.current_frame = 0
        super().__init__(x, y, self.frames[self.current_frame])
        self.animation_speed = 5
        self.animation_counter = 0

    def move(self, dx):
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


# Ghost enemy for Level 2
class Ghost(GameObject):
    def __init__(self, x, y):
        GHOST_FRAME_WIDTH = 256 // 4  # 4 frames across, 60px height
        GHOST_FRAME_HEIGHT = 60

        # Extract frames from the sprite sheet (1 row, 4 columns)
        self.frames = [
            GHOST_SPRITE_SHEET.subsurface(pygame.Rect(i * GHOST_FRAME_WIDTH, 0, GHOST_FRAME_WIDTH, GHOST_FRAME_HEIGHT))
            for i in range(4)]
        self.current_frame = 0
        super().__init__(x, y, self.frames[self.current_frame])
        self.animation_speed = 6
        self.animation_counter = 0

    def move(self, dx):
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


# Monster enemy for Level 3
# Monster enemy for Level 3
class Monster(GameObject):
    def __init__(self, x, y):
        MONSTER_FRAME_WIDTH = 1000 // 4  # 4 frames across, each frame is 250px wide
        MONSTER_FRAME_HEIGHT = 250

        # Extract frames from the monster sprite sheet (1 row, 4 columns)
        self.frames = [
            MONSTER_SPRITE_SHEET.subsurface(
                pygame.Rect(i * MONSTER_FRAME_WIDTH, 0, MONSTER_FRAME_WIDTH, MONSTER_FRAME_HEIGHT))
            for i in range(4)
        ]
        self.current_frame = 0
        super().__init__(x, y, self.frames[self.current_frame])
        self.animation_speed = 9
        self.animation_counter = 0

    def move(self, dx):
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


# Explosion class remains the same
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
