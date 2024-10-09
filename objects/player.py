import pygame
from config import PLAYER_FRAMES, LASER_HEIGHT, RED, GREEN
from objects.laser import Laser
from objects.game_object import GameObject


class Player(GameObject):
    def __init__(self, x, y, sound_manager):
        self.frames = PLAYER_FRAMES
        self.current_frame = 0
        self.animation_speed = 10
        self.animation_counter = 0
        super().__init__(x, y, self.frames[self.current_frame])
        self.health = 100
        self.vel = 5
        self.sound_manager = sound_manager

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def shoot(self):
        self.sound_manager.play_laser_sound()
        return Laser(self.x + self.get_width(), self.y + self.get_height() // 2 - LASER_HEIGHT // 2)

    def draw_health(self, screen):
        pygame.draw.rect(screen, RED, (self.x, self.y + self.get_height() + 10, self.get_width(), 10))
        pygame.draw.rect(screen, GREEN,
                         (self.x, self.y + self.get_height() + 10, self.get_width() * (self.health / 100), 10))

    def update_animation(self):
        self.animation_counter += 1
        if self.animation_counter >= self.animation_speed:
            self.animation_counter = 0
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.img = self.frames[self.current_frame]

    def draw(self, screen):
        self.update_animation()
        super().draw(screen)
