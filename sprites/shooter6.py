import math
import random
from pathlib import Path
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
def screen_dimensions():
    return SCREEN_WIDTH, SCREEN_HEIGHT

WORLD_WIDTH = 5000
WORLD_HEIGHT = 5000
def world_dimensions():
    return WORLD_WIDTH, WORLD_HEIGHT

SCREEN_TITLE = "Shooter Verson 6.0"
POWERUPS = 500

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

def laser_path(image_name):
    return png_path('Lasers') / image_name

def enemies_path(image_name):
    return png_path('Enemies') / image_name

def random_points(w, h, n_points):
    points = []
    for i in range(n_points):
        points.append(
            (random.randrange(w), random.randrange(h))
        )
        
    return points

def angle_to_point(sprite, x, y):
    sprite_x, sprite_y = sprite.position
    angle_rad = math.atan2(
        y - sprite_y, x - sprite_x
    )
    angle_deg = math.degrees(angle_rad)
    return angle_deg

def angle_to_sprite(from_sprite, to_sprite):
    x, y = to_sprite.position
    return angle_to_point(from_sprite, x, y)

def vector_from_angle(angle):
    return(
        math.cos(math.radians(angle)),
        math.sin(math.radians(angle))
    )

class SpaceShooter(arcade.Window):
    '''Custom window sublass for our SpaceShooter game
    '''
    def __init__(self):
        # Call the parent class initializer
        sw, sh = screen_dimensions()
        super().__init__(sw, sh, SCREEN_TITLE)

        self.player_sprite = None
        self.powerup_list = None
        self.bullet_list = None
        self.enemies_list = None
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

        self.viewport = (0, sw, 0, sh)

        arcade.set_background_color(arcade.color.BLACK)

    def reset_viewport(self):
        px, py = self.player_sprite.position
        sw, sh = screen_dimensions()
        self.viewport = (
        px - sw // 2, # min x
        px + sw // 2, # max x
        py - sh // 2, # min y
        py + sh // 2 # max y
        )

        self.set_viewport(*self.viewport)

    def setup(self):
        self.score = 0
        
        # Set up the player sprites
        path = png_path('playerShip2_blue.png')
        self.player_sprite = arcade.Sprite(path)

        ww, wh = world_dimensions()

        self.player_sprite.center_x = ww // 2
        self.player_sprite.center_y = wh // 2

        self.reset_viewport() 

        # Set up the powerups
        self.powerup_list = arcade.SpriteList()

        for (x, y) in random_points(ww, wh, POWERUPS):
            path = powerup_path('star_gold.png')
            powerup = arcade.Sprite(path)
            powerup.center_x = x
            powerup.center_y = y
            self.powerup_list.append(powerup)
        
        # Set up bullet list
        self.bullet_list = arcade.SpriteList()
        
        # Set up our enemies list
        self.enemies_list = arcade.SpriteList()

        # XXX Fix XXX Starting out only one
        self.enemies_list.append(
            arcade.Sprite(enemies_path('enemyBlack2.png'))
        )
        self.enemies_list[0].center_x = self.player_sprite.center_x + 200
        self.enemies_list[0].center_y = self.player_sprite.center_y

    def on_draw(self):
        arcade.start_render()

        self.bullet_list.draw()
        self.powerup_list.draw()
        self.enemies_list.draw()
        self.player_sprite.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        view_x, _, view_y, _ = self.viewport
        world_x, world_y = (
            x + view_x, y + view_y
        )
        self.mouse_location = (world_x, world_y)

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            path = laser_path('laserBlue14.png')

            bullet = arcade.Sprite(path)

            bullet.angle = self.player_sprite.angle
            dx, dy =  vector_from_angle(bullet.angle + 90)
            forward_pixels = 35

            px, py = self.player_sprite.position
            bullet.center_x = px + dx * forward_pixels
            bullet.center_y = py + dy * forward_pixels

            bullet_speed = 10
            bullet.change_x = dx * bullet_speed
            bullet.change_y = dy * bullet_speed
            self.bullet_list.append(bullet)

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
        angle_deg = angle_to_point(
            self.player_sprite, mouse_x, mouse_y
        )
        self.player_sprite.angle = angle_deg - 90

        # Orient all enemies to player location
        for enemy in self.enemies_list:
            angle_deg = angle_to_sprite(enemy, self.player_sprite)
            enemy.angle = angle_deg + 90
            if arcade.check_for_collision(enemy, self.player_sprite):
                enemy.change_x = 0
                enemy.change_y = 0
            else:
                dx, dy = vector_from_angle(enemy.angle - 90)
                enemy_speed = 1
                enemy.change_x = dx * enemy_speed
                enemy.change_y = dy * enemy_speed


        # Update our sprites
        self.player_sprite.update()
        self.powerup_list.update()
        self.bullet_list.update()
        self.enemies_list.update()

        # Update the viewport
        self.reset_viewport()

        # Do collision detection
        powerup_hit_list = arcade.check_for_collision_with_list(
            self.player_sprite, self.powerup_list
        )

        for powerup in powerup_hit_list:
            powerup.remove_from_sprite_lists()
            self.score += 1
        if powerup_hit_list:
            print(self.score)

        # Test for bullets leaving viewport
        v_min_x, v_max_x,v_min_y, v_max_y = self.viewport
        for bullet in self.bullet_list:
            bx, by = bullet.position
            if bx > v_max_x or bx < v_min_x or by < v_min_y or by > v_max_y:
                bullet.remove_from_sprite_lists()

    
def main():
    window = SpaceShooter()
    window.setup()
    arcade.run()

if __name__ == '__main__':
    main()