import pygame
from config import PLAYER_FRAMES
from constants import (
    PLAYER_HEALTH,
    PLAYER_VELOCITY,
    STATE_RUNNING,
    STATE_PAUSED,
    STATE_GAME_OVER,
    WIDTH,
    HEIGHT,
)
from sound_manager import SoundManager


class GameObject:
    def __init__(self, x: float, y: float, frames: list):
        self.x = x
        self.y = y
        self.frames = frames
        self.current_frame = 0

    def move(self, dx: float, dy: float) -> None:
        self.x += dx
        self.y += dy

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.frames[self.current_frame], (self.x, self.y))


class Player(GameObject):
    def __init__(self, x: float, y: float):
        super().__init__(x, y, PLAYER_FRAMES)
        self.health: int = PLAYER_HEALTH
        self.vel: float = PLAYER_VELOCITY
        self.animation_counter = 0
        self.init_health()
        self.init_movement()
        self.init_animations()

    def init_health(self) -> None:
        pass

    def init_movement(self) -> None:
        pass

    def init_animations(self) -> None:
        self.animation_counter: int = 0

    def update(self) -> None:
        self.handle_input()
        self.update_animation()

    def handle_input(self) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.move(-self.vel, 0)
        if keys[pygame.K_RIGHT]:
            self.move(self.vel, 0)
        if keys[pygame.K_UP]:
            self.move(0, -self.vel)
        if keys[pygame.K_DOWN]:
            self.move(0, self.vel)

    def update_animation(self) -> None:
        self.animation_counter += 1
        if self.animation_counter >= len(self.frames):
            pass
        self.current_frame = self.animation_counter


class Game:
    def __init__(self):
        pygame.init()
        self.screen: pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("My Game")
        self.clock = pygame.time.Clock()
        self.state: int = STATE_RUNNING
        self.sound_manager = SoundManager()
        self.player = Player(x=WIDTH // 2, y=HEIGHT // 2)

    def run(self) -> None:
        while True:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(60)

    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    def update(self) -> None:
        if self.state == STATE_RUNNING:
            self.player.update()
            # Update other game objects
        elif self.state == STATE_PAUSED:
            # Handle pause logic
            pass
        elif self.state == STATE_GAME_OVER:
            # Handle game over logic
            pass

    def render(self) -> None:
        self.screen.fill((0, 0, 0))  # Clear screen with black
        self.player.draw(self.screen)
        # Draw other game objects
        pygame.display.flip()


if __name__ == "__main__":
    game = Game()
    game.run()
