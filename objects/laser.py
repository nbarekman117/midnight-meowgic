from config import MAGICBALL_FRAMES
from objects.game_object import GameObject


class Laser(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y, MAGICBALL_FRAMES[0])
        self.vel = 10
        self.frame_index = 0
        self.animation_speed = 5
        self.frame_counter = 0

    def move(self, dx=None):
        self.x += dx if dx is not None else self.vel
        self.rect.topleft = (self.x, self.y)  # Update the rect position

        # Update the frame index for animation
        self.frame_counter += 1
        if self.frame_counter >= self.animation_speed:
            self.frame_counter = 0
            self.frame_index = (self.frame_index + 1) % len(MAGICBALL_FRAMES)
            self.img = MAGICBALL_FRAMES[self.frame_index]

    def off_screen(self, width):
        return not (0 <= self.x <= width)
