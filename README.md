# skibidi-midnight-meowgic


What is this game?
Midnight Meowgic is a Halloween-themed space-invader-style game where you control a witch cat to defeat enemies. The goal is to survive through multiple levels that add on increasingly difficult enemies while maintaining your health and scoring points.

How to play this game?
The player controls the witch cat using arrow keys to move up and down and using the spacebar to shoot magical projectiles. The objective is to destroy the enemies before they pass the player and reach the end of the screen. Maintain your health and increase your score by defeating enemies, which have different point attributions depending on their difficulty. 

What Game Object(s) are included in this Game?
Player (Witch Cat): The player-controlled character that shoots projectiles.
Enemies: Three types of enemies that appear at different levels (bats, ghosts, and monsters)
Projectiles (Magic bolts): Fired by the player to attack enemies.
Explosion animation: Triggered when a projectile hits an enemy.
UI Elements:
Score Display
Health Bar
Level Number

How and when are these game objects updated/created/deleted?
Player: Updated in every frame for movement and shooting actions.
Enemies: Created at the start of each level and updated with their movements toward the player. Deleted when they are destroyed by the player’s projectiles.
Projectiles: Created when the player shoots. Updated every frame for collision detection. Deleted when they hit an enemy or go off-screen.
Explosion animation: Created when a projectile collides with an enemy. Deleted after the animation ends.
UI Elements: Continuously updated as the player’s health, score, and level change.

How do I win/lose this game (What is the game over scenario)?
The game is over when the player’s health reaches zero after too many enemies reach the end of the screen. Players have 100 health points, bats are -10, ghosts are -15, and monsters are -20 health points. 


References
Font
Font: https://gowldev.itch.io/halloween-pixels 

Images
Backgrounds: https://craftpix.net/freebies/free-halloween-2d-game-backgrounds/?num=1&count=10&sq=halloween&pos=4 
Bat Sprite: https://elthen.itch.io/bat-sprite-pack 
Explosion Sprite: https://craftpix.net/freebies/free-animated-explosion-sprite-pack/ 
Ghost Sprite: https://www.ascensiongamedev.com/topic/4393-sprite-recolors-and-other-resources/ 
Player Sprite: https://www.vecteezy.com/png/27190929-pixel-art-witch-s-black-cat-with-witch-hat 
Monster Sprite: https://free-game-assets.itch.io/swamp-bosses-pixel-art-pack 

Music
Background Music: Music by <a href="https://pixabay.com/users/moodmode-33139253/?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=166454">Vlad Krotov</a> from <a href="https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=166454">Pixabay</a> 
Laser: Sound Effect by <a href="https://pixabay.com/users/driken5482-45721595/?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=236669">Driken Stan</a> from <a href="https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=236669">Pixabay</a> 
Explosion (enemy collide): Sound Effect by <a href="https://pixabay.com/users/cyberwaveorchestra-23801316/?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=241821">Cyberwave Orchestra</a> from <a href="https://pixabay.com/sound-effects//?utm_source=link-attribution&utm_medium=referral&utm_campaign=music&utm_content=241821">Pixabay</a> 

