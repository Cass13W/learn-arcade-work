import random

import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_FLY = 0.2
FLY_COUNT = 50
SPRITE_SCALING_BEE = 0.2
BEE_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        # Variables that will hold sprite lists.
        self.player_list = None
        self.fly_list = None
        self.bee_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        # Load sounds
        self.good = arcade.load_sound("good.wav")
        self.good_player = None
        self.bad = arcade.load_sound("bad.wav")
        self.bad_player = None

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.fly_list = arcade.SpriteList()
        self.bee_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # frog image from arcade built-in resources
        self.player_sprite = arcade.Sprite("frog.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the food
        for i in range(FLY_COUNT):
            # Create the fly instance
            # fly image from arcade built-in resources
            fly = arcade.Sprite("fly.png", SPRITE_SCALING_FLY)

            # Position the fly
            fly.center_x = random.randrange(SCREEN_WIDTH)
            fly.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the fly to the lists
            self.fly_list.append(fly)

        # Create the bad sprite
        for i in range(BEE_COUNT):
            # Create the bee instance
            # bee image from arcade built-in resources
            bee = arcade.Sprite("bee.png", SPRITE_SCALING_BEE)

            # Position the bee
            bee.center_x = random.randrange(SCREEN_WIDTH)
            bee.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the bee to the lists
            self.bee_list.append(bee)

    def on_draw(self):
        arcade.start_render()
        # Draw the sprite lists
        self.fly_list.draw()
        self.player_list.draw()
        self.bee_list.draw()
        if len(self.fly_list) != 0:

            # Put the text on the screen.
            output = f"Score: {self.score}"
            arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

        else:
            # Game over screen
            arcade.draw_text('GAME OVER', 200, 300, arcade.color.RED, 50)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """

        if len(self.fly_list) != 0:
            # Move the center of the player sprite to match the mouse x, y
            self.player_sprite.center_x = x
            self.player_sprite.center_y = y
        else:
            # Stop player sprite motion
            self.player_sprite.center_x = 0
            self.player_sprite.center_y = 0

    def update(self, delta_time):
        """ Movement and game logic """
        # Move the bugs
        if len(self.fly_list) != 0:
            for fly in self.fly_list:
                fly.center_x += 2
                if fly.center_x > SCREEN_WIDTH:
                    fly.center_x = 0
                    fly.center_y = random.randint(20, SCREEN_HEIGHT - 20)

            for bee in self.bee_list:
                bee.center_y += .5
                if bee.center_y > SCREEN_HEIGHT:
                    bee.center_y = 0
                    bee.center_x = random.randint(20, SCREEN_WIDTH - 20)

            # Call update on all sprites
            self.fly_list.update()
            self.bee_list.update()

            # Generate a list of all sprites that collided with the player.
            fly_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                                self.fly_list)
            # Loop through each colliding sprite, remove it, and add to the score.
            for fly in fly_hit_list:
                fly.remove_from_sprite_lists()
                self.score += 1
                self.good_player = arcade.play_sound(self.good)

            # Generate a list of all sprites that collided with the player.
            bee_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                                self.bee_list)
            # Loop through each colliding sprite, remove it, and add to the score.
            for bee in bee_hit_list:
                bee.remove_from_sprite_lists()
                self.score -= 1
                self.bad_player = arcade.play_sound(self.bad)

        else:
            # Stop the bees from moving
            for bee in self.bee_list:
                bee.center_y += 0
                if bee.center_y > SCREEN_HEIGHT:
                    bee.center_y = 0
                    bee.center_x = random.randint(20, SCREEN_WIDTH - 20)


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
