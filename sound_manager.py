from constants import LASER_SOUND_PATH, EXPLOSION_SOUND_PATH, BACKGROUND_MUSIC_PATH
import pygame


class SoundManager:
    def __init__(self):
        pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=1024)
        self.laser_sound = pygame.mixer.Sound(LASER_SOUND_PATH)
        self.explosion_sound = pygame.mixer.Sound(EXPLOSION_SOUND_PATH)
        pygame.mixer.music.load(BACKGROUND_MUSIC_PATH)

        # Set volume
        self.laser_sound.set_volume(1.0)
        self.explosion_sound.set_volume(1.0)
        pygame.mixer.music.set_volume(1.0)

    def play_background_music(self):
        pygame.mixer.music.play(-1)

    def play_laser_sound(self):
        self.laser_sound.play()

    def play_explosion_sound(self):
        self.explosion_sound.play()
