from config import *
from enemy import Enemy, Ghost, Monster, Explosion
from screens import show_start_screen, show_game_over_screen
from ui import Score, draw_level_number, HealthBar
from background import Background
from sound_manager import SoundManager
import random
from game_object import Player, Explosion

# Initialize pygame and mixer
pygame.init()


def run_game():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Midnight Meowgic")
    clock = pygame.time.Clock()

    # Create SoundManager instance
    sound_manager = SoundManager()
    sound_manager.play_background_music()  # Play background music

    # Create game objects
    player = Player(50, HEIGHT // 2, sound_manager)  # Pass SoundManager to Player class
    enemies = [Enemy(random.randint(WIDTH + 100, WIDTH + 1000), random.randint(0, HEIGHT - BAT_FRAME_HEIGHT)) for _ in range(5)]
    ghosts = []
    monsters = []
    lasers = []
    explosions = []
    score = Score()
    background1 = Background("assets/Background1.png")
    background2 = Background("assets/Background2.png")
    background3 = Background("assets/Background3.png")
    health_bar = HealthBar(PLAYER_HEALTH, WIDTH, HEIGHT)  # Initialize health bar with screen dimensions

    current_level = 1  # Track the current level
    last_shot_time = 0
    shot_cooldown = 500

    running = True
    while running:
        clock.tick(FPS)
        screen.fill(BLACK)

        current_time = pygame.time.get_ticks()

        # Change the level and background based on score
        if score.value >= 100 and current_level == 1:
            current_level = 2
            ghosts = [Ghost(random.randint(WIDTH + 100, WIDTH + 1000), random.randint(0, HEIGHT - 60)) for _ in range(3)]
            print("Level 2 reached!")
        elif score.value >= 300 and current_level == 2:
            current_level = 3
            monsters = [Monster(random.randint(WIDTH - 250, WIDTH), random.randint(0, HEIGHT - 250)) for _ in range(2)]
            print("Level 3 reached!")

        # Update background based on the level
        if current_level == 1:
            background1.update()
            background1.draw(screen)
        elif current_level == 2:
            background2.update()
            background2.draw(screen)
        elif current_level == 3:
            background3.update()
            background3.draw(screen)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Keydown events for shooting and sound
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if current_time - last_shot_time > shot_cooldown:
                        if len(lasers) < 3:
                            new_laser = player.shoot()
                            lasers.append(new_laser)
                            last_shot_time = current_time
                            print("Attempting to play laser sound...")
                            sound_manager.play_laser_sound()

                if event.key == pygame.K_e:
                    print("Attempting to play explosion sound...")
                    sound_manager.play_explosion_sound()

        # Player input for movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and player.y - player.vel > 0:
            player.move(0, -player.vel)
        if keys[pygame.K_DOWN] and player.y + player.vel + player.get_height() < HEIGHT:
            player.move(0, player.vel)

        # Update lasers and check collisions
        lasers_to_remove = []
        enemies_to_remove = []
        ghosts_to_remove = []
        monsters_to_remove = []

        for laser in lasers:
            laser.move(10)

            if laser.off_screen(WIDTH):
                lasers_to_remove.append(laser)
                continue

            # Collision detection for regular enemies
            for enemy in enemies:
                if laser.rect.colliderect(enemy.rect):
                    lasers_to_remove.append(laser)
                    enemies_to_remove.append(enemy)
                    explosions.append(Explosion(enemy.x, enemy.y))
                    sound_manager.play_explosion_sound()
                    score.update(10)  # Increase score by 10 for each hit
                    break

            # Collision detection for ghosts in Level 2
            for ghost in ghosts:
                if laser.rect.colliderect(ghost.rect):
                    lasers_to_remove.append(laser)
                    ghosts_to_remove.append(ghost)
                    explosions.append(Explosion(ghost.x, ghost.y))
                    sound_manager.play_explosion_sound()
                    score.update(20)  # Increase score by 20 for ghost hits
                    break

            # Collision detection for monsters in Level 3
            for monster in monsters:
                if laser.rect.colliderect(monster.rect):
                    lasers_to_remove.append(laser)
                    monsters_to_remove.append(monster)
                    explosions.append(Explosion(monster.x, monster.y))
                    sound_manager.play_explosion_sound()
                    score.update(30)  # Increase score by 30 for monster hits
                    break

        for laser in lasers_to_remove:
            if laser in lasers:
                lasers.remove(laser)

        for enemy in enemies_to_remove:
            if enemy in enemies:
                enemies.remove(enemy)
                enemies.append(Enemy(random.randint(WIDTH + 100, WIDTH + 1000), random.randint(0, HEIGHT - BAT_FRAME_HEIGHT)))

        # Handle ghost removal and re-spawning in Level 2
        for ghost in ghosts_to_remove:
            if ghost in ghosts:
                ghosts.remove(ghost)
                ghosts.append(Ghost(random.randint(WIDTH + 100, WIDTH + 1000), random.randint(0, HEIGHT - 60)))

        # Handle monster removal and re-spawning in Level 3
        for monster in monsters_to_remove:
            if monster in monsters:
                monsters.remove(monster)
                # Respawn the monster, ensuring it fits within the screen bounds
                monsters.append(Monster(random.randint(WIDTH - 250, WIDTH), random.randint(0, HEIGHT - 250)))

        # Move regular enemies in Level 1
        for enemy in enemies[:]:
            enemy.move(-2)
            if enemy.x < 0:
                health_bar.take_damage(10)  # Example: Player takes 10 damage
                enemies.remove(enemy)
                enemies.append(Enemy(random.randint(WIDTH + 100, WIDTH + 1000), random.randint(0, HEIGHT - BAT_FRAME_HEIGHT)))

        # Move ghosts faster in Level 2
        for ghost in ghosts[:]:
            ghost.move(-4)
            if ghost.x < 0:
                health_bar.take_damage(15)
                ghosts.remove(ghost)
                ghosts.append(Ghost(random.randint(WIDTH + 100, WIDTH + 1000), random.randint(0, HEIGHT - 60)))

        # Move monsters faster in Level 3
        for monster in monsters[:]:
            monster.move(-2)
            if monster.x < 0:
                health_bar.take_damage(20)
                monsters.remove(monster)
                monsters.append(Monster(random.randint(WIDTH - 250, WIDTH), random.randint(0, HEIGHT - 250)))

        # Draw player, enemies, ghosts, monsters, lasers, and explosions
        player.draw(screen)
        for enemy in enemies:
            enemy.draw(screen)
        for ghost in ghosts:
            ghost.draw(screen)
        for monster in monsters:
            monster.draw(screen)
        for laser in lasers:
            laser.draw(screen)
        for explosion in explosions[:]:
            explosion.draw(screen)
            if explosion.finished:
                explosions.remove(explosion)
        score.draw(screen)

        # Draw level number at the top
        draw_level_number(screen, current_level)

        # Draw health bar
        health_bar.draw(screen)

        # Check for game over
        if health_bar.current_health <= 0:
            show_game_over_screen(screen)
            running = False

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    # Initialize the screen and pass it to the s tart screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    show_start_screen(screen)  # Pass the screen to the start screen function
    run_game()
