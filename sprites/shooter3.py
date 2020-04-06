import math
import random
from pathlib import Path
import arcade

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
POWERUPS = 50
def dimensions():
    return SCREEN_WIDTH, SCREEN_HEIGHT

SCREEN_TITLE = "Shooter Verson 3.0"

def png_path(image_name):
    '''Return an image path for PNG file
    ex.
    >> png_path('playerShip1_red.png')
    Path('PNG/playerShip1_red.png')
    '''
    png_dir = Path('PNG')
    return png_dir / image_name

def powerup_path(image_name):
    return png_path('Power-ups') / image_name

def random_points(w, h, n_points):
    points = []
    for i in range(n_points):
        points.append(
            (random.randrange(w), random.randrange(h))
        )
        
    return points
class SpaceShooter(arcade.Window):
    '''Custom window sublass for our SpaceShooter game
    '''
    def __init__(self):
        # Call the parent class initializer
        w, h = dimensions()
        super().__init__(w, h, SCREEN_TITLE)

        self.player_sprite = None
        self.mouse_location = (0, 0)
        self.score = 0
        self.movement = 2
        self.keys_pressed = set()
        self.key_lookup = {
            arcade.key.W: 'w',
            arcade.key.A: 'a',
            arcade.key.S: 's',
            arcade.key.D: 'd',
        }

        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):
        self.score = 0
        
        # Set up the player sprites
        path = png_path('playerShip2_blue.png')
        self.player_sprite = arcade.Sprite(path)

        w, h = dimensions()
        self.player_sprite.center_x = w // 2
        self.player_sprite.center_y = h // 2

        # Set up the powerups
        self.powerup_list = arcade.SpriteList()

        for (x, y) in random_points(w, h, POWERUPS):
            path = powerup_path('star_gold.png')
            powerup = arcade.Sprite(path)
            powerup.center_x = x
            powerup.center_y = y
            self.powerup_list.append(powerup)

    def on_draw(self):
        arcade.start_render()

        self.player_sprite.draw()
        self.powerup_list.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        self.mouse_location = (x, y)

    def on_key_press(self, key, modifiers):
        
        if key in self.key_lookup:
            self.keys_pressed.add(self.key_lookup[key])
        print(self.keys_pressed)
    
    def on_key_release(self, key, modifiers):
        # remove keys we care about from our keys_pressed set
        if key in self.key_lookup:
            self.keys_pressed.remove(self.key_lookup[key])

        print(self.keys_pressed)


    
    def on_update(self, delta_time):
        # Check for WADS keys and perform movement
        dx, dy = 0, 0
        if 'w' in self.keys_pressed:
            dy += self.movement

        if 's' in self.keys_pressed:
            dy -= self.movement

        if 'a' in self.keys_pressed:
            dx -= self.movement

        if 'd' in self.keys_pressed:
            dx += self.movement

        self.player_sprite.change_x = dx
        self.player_sprite.change_y = dy

        mouse_x, mouse_y = self.mouse_location
        player_x, player_y = self.player_sprite.position
        x, y = mouse_x - player_x, mouse_y - player_y
        angle_rad = math.atan2(y, x)
        angle_deg = math.degrees(angle_rad)
        self.player_sprite.angle = angle_deg - 90

        # Update our sprites
        self.player_sprite.update()
        self.powerup_list.update()

        # Do collision detection
        powerup_hit_list = arcade.check_for_collision_with_list(
            self.player_sprite, self.powerup_list
        )

        for powerup in powerup_hit_list:
            powerup.remove_from_sprite_lists()
            self.score += 1
        if powerup_hit_list:
            print(self.score)
    
def main():
    window = SpaceShooter()
    window.setup()
    arcade.run()

if __name__ == '__main__':
    main()