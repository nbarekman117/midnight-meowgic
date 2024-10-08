import pygame
from config import PLAYER_FRAMES, MAGICBALL_FRAMES, EXPLOSION_SPRITE_SHEET, EXPLOSION_FRAME_WIDTH, \
    EXPLOSION_FRAME_HEIGHT, \
    RED, GREEN, LASER_HEIGHT


class GameObject:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)
        self.rect = self.img.get_rect(topleft=(self.x, self.y))

    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))
        self.rect.topleft = (self.x, self.y)

    def get_width(self):
        return self.img.get_width()

    def get_height(self):
        return self.img.get_height()


# The Player class
class Player(GameObject):
    def __init__(self, x, y, sound_manager):
        self.frames = PLAYER_FRAMES  # Use the frames from the sprite sheet
        self.current_frame = 0
        self.animation_speed = 10  # Adjust to control the speed of animation
        self.animation_counter = 0
        super().__init__(x, y, self.frames[self.current_frame])
        self.health = 100
        self.vel = 5
        self.sound_manager = sound_manager

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def shoot(self):
        self.sound_manager.play_laser_sound()  # Play laser sound using SoundManager
        return Laser(self.x + self.get_width(), self.y + self.get_height() // 2 - LASER_HEIGHT // 2)

    def draw_health(self, screen):
        pygame.draw.rect(screen, RED, (self.x, self.y + self.get_height() + 10, self.get_width(), 10))
        pygame.draw.rect(screen, GREEN,
                         (self.x, self.y + self.get_height() + 10, self.get_width() * (self.health / 100), 10))

    def update_animation(self):
        self.animation_counter += 1
        if self.animation_counter >= self.animation_speed:
            self.animation_counter = 0
            self.current_frame = (self.current_frame + 1) % len(self.frames)  # Cycle through frames
            self.img = self.frames[self.current_frame]

    def draw(self, screen):
        self.update_animation()  # Update animation before drawing
        super().draw(screen)


# The Laser class
class Laser(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y, MAGICBALL_FRAMES[0])
        self.vel = 10
        self.frame_index = 0
        self.animation_speed = 5
        self.frame_counter = 0

    def move(self, dx=None):
        self.x += dx if dx is not None else self.vel
        self.rect.topleft = (self.x, self.y)

        # Update the frame index for animation
        self.frame_counter += 1
        if self.frame_counter >= self.animation_speed:
            self.frame_counter = 0
            self.frame_index = (self.frame_index + 1) % len(MAGICBALL_FRAMES)
            self.img = MAGICBALL_FRAMES[self.frame_index]

    def off_screen(self, width):
        return not (0 <= self.x <= width)


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
