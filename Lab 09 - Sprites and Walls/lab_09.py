import random
import arcade
from pyglet.math import Vec2

SPRITE_SCALING = 0.5
SPRITE_SCALING_BOX = 1
SPRITE_SCALING_STAR = 0.5

DEFAULT_SCREEN_WIDTH = 1000
DEFAULT_SCREEN_HEIGHT = 800
SCREEN_TITLE = "Sprite Move with Scrolling Screen Example"
NUMBER_OF_STARS = 50

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = 220

# How fast the camera pans to the player. 1.0 is instant.
CAMERA_SPEED = 0.1

# How fast the character moves
PLAYER_MOVEMENT_SPEED = 7


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title, resizable=True)

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        # Sprite lists
        self.player_list = None
        self.wall_list = None
        self.star_list = None

        # Set up the player
        self.player_sprite = None

        # Set up the score
        self.score = 0

        # Physics engine so we don't run into walls.
        self.physics_engine = None

        # Track the current state of what key is pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        # Create the cameras. One for the GUI, one for the sprites.
        # We scroll the 'sprite world' but not the GUI.
        self.camera_sprites = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)
        self.camera_gui = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)

        # Load sounds
        # Sound downloaded from OpenGameArt.org
        self.good = arcade.load_sound("good.wav")
        self.good_player = None

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Set up the score
        self.score = 0

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.star_list = arcade.SpriteList()

        # Set up the player
        # Artwork from python arcade built-in resources
        self.player_sprite = arcade.Sprite(":resources:images/space_shooter/playerShip3_orange.png",
                                           SPRITE_SCALING)
        self.player_sprite.center_x = 256
        self.player_sprite.center_y = 512
        self.player_list.append(self.player_sprite)

        # Artwork from python arcade built-in resources
        for x in range(-450, 950, 256):
            for y in range(-450, 950, 256):
                wall = arcade.Sprite(":resources:images/space_shooter/meteorGrey_med1.png", SPRITE_SCALING_BOX)
                wall.center_x = random.randrange(-450, 950)
                wall.center_y = random.randrange(-450, 950)
                self.wall_list.append(wall)

        # Artwork from python arcade built-in resources
        for x in range(-450, 950, 256):
            for y in range(-450, 950, 256):
                wall = arcade.Sprite(":resources:images/space_shooter/meteorGrey_big2.png", 0.8)
                wall.center_x = random.randrange(-450, 950)
                wall.center_y = random.randrange(-450, 950)
                self.wall_list.append(wall)

        # Artwork from python arcade built-in resources
        for x in range(-450, 950, 320):
            for y in range(-450, 950, 320):
                wall = arcade.Sprite(":resources:images/space_shooter/meteorGrey_big3.png", 0.8)
                wall.center_x = random.randrange(-450, 950)
                wall.center_y = random.randrange(-450, 950)
                self.wall_list.append(wall)

        # Artwork from kenny.nl platformer pack redux
        # set up barrier box
        for y in range(-500, 1000, 64):
            wall = arcade.Sprite("chain.png", 0.5)
            wall.center_x = -500
            wall.center_y = y
            self.wall_list.append(wall)

        # Artwork from kenny.nl platformer pack redux
        for y in range(-500, 1000, 64):
            wall = arcade.Sprite("chain.png", 0.5)
            wall.center_x = 1000
            wall.center_y = y
            self.wall_list.append(wall)

        # Artwork from kenny.nl platformer pack redux
        for x in range(-500, 1000, 64):
            wall = arcade.Sprite("chain_side.png", 0.5)
            wall.center_x = x
            wall.center_y = -500
            self.wall_list.append(wall)

        # Artwork from kenny.nl platformer pack redux
        for x in range(-500, 1000, 64):
            wall = arcade.Sprite("chain_side.png", 0.5)
            wall.center_x = x
            wall.center_y = 1000
            self.wall_list.append(wall)

        # -- Randomly place stars where there are no walls
        # Create the stars
        for i in range(NUMBER_OF_STARS):

            # Create the star instance
            # Artwork from kenny.nl platformer pack redux
            star = arcade.Sprite("star.png", SPRITE_SCALING_STAR)

            # Boolean variable if we successfully placed the star
            star_placed_successfully = False

            # Keep trying until success
            while not star_placed_successfully:
                # Position the star
                star.center_x = random.randrange(-450, 950)
                star.center_y = random.randrange(-450, 950)

                # See if the star is hitting a wall
                wall_hit_list = arcade.check_for_collision_with_list(star, self.wall_list)

                # See if the star is hitting another star
                star_hit_list = arcade.check_for_collision_with_list(star, self.star_list)

                if len(wall_hit_list) == 0 and len(star_hit_list) == 0:
                    # It is!
                    star_placed_successfully = True

            # Add the star to the lists
            self.star_list.append(star)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        # Set the background color
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """ Render the screen. """

        # This command has to happen before we start drawing
        self.clear()

        # Select the camera we'll use to draw all our sprites
        self.camera_sprites.use()

        # Draw all the sprites.
        self.wall_list.draw()
        self.player_list.draw()
        self.star_list.draw()

        # Select the (un-scrolled) camera for our GUI
        self.camera_gui.use()

        # Draw the GUI
        arcade.draw_rectangle_filled(self.width // 2,
                                     20,
                                     self.width,
                                     40,
                                     arcade.color.ALMOND)
        text = f"Score: {self.score}"
        arcade.draw_text(text, 10, 10, arcade.color.BLACK_BEAN, 20)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.up_pressed = True
        elif key == arcade.key.DOWN:
            self.down_pressed = True
        elif key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP:
            self.up_pressed = False
        elif key == arcade.key.DOWN:
            self.down_pressed = False
        elif key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Calculate speed based on the keys pressed
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0

        if self.up_pressed and not self.down_pressed:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

            # Generate a list of all sprites that collided with the player.
        star_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                             self.star_list)
        # Loop through each colliding sprite, remove it, and add to the score.
        # Sound downloaded from OpenGameArt.org
        for star in star_hit_list:
            star.remove_from_sprite_lists()
            self.score += 1
            self.good_player = arcade.play_sound(self.good)

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()

        # Scroll the screen to the player
        self.scroll_to_player()

    def scroll_to_player(self):
        """
        Scroll the window to the player.

        if CAMERA_SPEED is 1, the camera will immediately move to the desired position.
        Anything between 0 and 1 will have the camera move to the location with a smoother
        pan.
        """

        position = Vec2(self.player_sprite.center_x - self.width / 2,
                        self.player_sprite.center_y - self.height / 2)
        self.camera_sprites.move_to(position, CAMERA_SPEED)

    def on_resize(self, width, height):
        """
        Resize window
        Handle the user grabbing the edge and resizing the window.
        """
        self.camera_sprites.resize(int(width), int(height))
        self.camera_gui.resize(int(width), int(height))


def main():
    """ Main function """
    window = MyGame(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
