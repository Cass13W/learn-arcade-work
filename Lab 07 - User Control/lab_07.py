import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 3


class Car:
    def __init__(self, position_x, position_y, width, height, color):
        self.position_x = position_x
        self.position_y = position_y
        self.width = width
        self.height = height
        self.color = color

    def draw(self):
        # draw the car body
        arcade.draw_rectangle_filled(self.position_x, self.position_y, 35, 13, arcade.color.AUBURN)
        arcade.draw_ellipse_filled(self.position_x, self.position_y + 5, 25, 18, arcade.color.AUBURN)

        # draw the wheels
        arcade.draw_circle_filled(self.position_x - 15, self.position_y - 5, 5, arcade.color.BLACK)
        arcade.draw_circle_filled(self.position_x + 15, self.position_y - 5, 5, arcade.color.BLACK)
        arcade.draw_circle_filled(self.position_x - 15, self.position_y - 5, 2, arcade.color.ALICE_BLUE)
        arcade.draw_circle_filled(self.position_x + 15, self.position_y - 5, 2, arcade.color.ALICE_BLUE)

        # draw the door
        arcade.draw_line(self.position_x, self.position_y - 5, self.position_x, self.position_y + 5, arcade.color.BLACK)

        # draw the window
        arcade.draw_rectangle_filled(self.position_x + 6, self.position_y + 8, 10, 5, arcade.color.BEAU_BLUE)

        arcade.draw_rectangle_filled(self.position_x,
                                     self.position_y,
                                     self.width,
                                     self.height,
                                     self.color)


class Car2:
    def __init__(self, position_x, position_y, change_x, change_y, width, height, color, car_crash_player, car_crash):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.width = width
        self.height = height
        self.color = color
        self.car_crash_player = car_crash_player
        self.car_crash = car_crash

    def draw(self):
        # draw the car body
        arcade.draw_rectangle_filled(self.position_x, self.position_y, 35, 13, arcade.color.BLEU_DE_FRANCE)
        arcade.draw_ellipse_filled(self.position_x, self.position_y + 5, 25, 18, arcade.color.BLEU_DE_FRANCE)

        # draw the wheels
        arcade.draw_circle_filled(self.position_x - 15, self.position_y - 5, 5, arcade.color.BLACK)
        arcade.draw_circle_filled(self.position_x + 15, self.position_y - 5, 5, arcade.color.BLACK)
        arcade.draw_circle_filled(self.position_x - 15, self.position_y - 5, 2, arcade.color.ALICE_BLUE)
        arcade.draw_circle_filled(self.position_x + 15, self.position_y - 5, 2, arcade.color.ALICE_BLUE)

        # draw the door
        arcade.draw_line(self.position_x, self.position_y - 5, self.position_x, self.position_y + 5, arcade.color.BLACK)

        # draw the window
        arcade.draw_rectangle_filled(self.position_x + 6, self.position_y + 8, 10, 5, arcade.color.BEAU_BLUE)

        arcade.draw_rectangle_filled(self.position_x,
                                     self.position_y,
                                     self.width,
                                     self.height,
                                     self.color)

    def update(self):
        # Move car2
        self.position_y += self.change_y
        self.position_x += self.change_x

        # prevent it from moving off-screen
        if self.position_x < 0:
            self.position_x = 1
            if not self.car_crash_player or not self.car_crash_player.playing:
                self.car_crash_player = arcade.play_sound(self.car_crash)

        if self.position_x > SCREEN_WIDTH:
            self.position_x = 800
            if not self.car_crash_player or not self.car_crash_player.playing:
                self.car_crash_player = arcade.play_sound(self.car_crash)

        if self.position_y < 0:
            self.position_y = 1
            if not self.car_crash_player or not self.car_crash_player.playing:
                self.car_crash_player = arcade.play_sound(self.car_crash)

        if self.position_y > SCREEN_HEIGHT:
            self.position_y = 600
            if not self.car_crash_player or not self.car_crash_player.playing:
                self.car_crash_player = arcade.play_sound(self.car_crash)


class MyGame(arcade.Window):
    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # make the mouse invisible
        self.set_mouse_visible(False)

        # load sounds
        self.engine_rev = arcade.load_sound("engine_rev.wav")
        self.engine_rev_player = None
        self.car_crash = arcade.load_sound("car_crash.wav")
        self.car_crash_player = None

        # draw the background
        arcade.set_background_color(arcade.color.AVOCADO)

        self.car = Car(100, 100, 1, 1, arcade.color.RED)
        self.car2 = Car2(100, 100, 0, 0, 1, 1, arcade.color.BLUE, self.car_crash_player, self.car_crash)

    def on_mouse_motion(self, x, y, dx, dy):
        # update the position
        self.car.position_x = x
        self.car.position_y = y

    # if the mouse leaves the screen, play a sound
    def on_mouse_leave(self, x: int, y: int):
        if not self.car_crash_player or not self.car_crash_player.playing:
            self.car_crash_player = arcade.play_sound(self.car_crash)

    def on_draw(self):
        arcade.start_render()

        # draw the stands
        arcade.draw_rectangle_filled(400, 500, 300, 130, arcade.color.ALICE_BLUE)

        # draw the seats
        arcade.draw_line(250, 510, 550, 510, arcade.color.ARSENIC, 2)
        arcade.draw_line(250, 530, 550, 530, arcade.color.ARSENIC, 2)
        arcade.draw_line(250, 550, 550, 550, arcade.color.ARSENIC, 2)

        # draw the track
        arcade.draw_ellipse_outline(400, 300, 650, 400, arcade.color.ARSENIC, 65)
        arcade.draw_ellipse_outline(400, 300, 600, 340, arcade.color.ALICE_BLUE, 2)

        # draw the cars
        self.car.draw()
        self.car2.draw()

    # make the engine rev
    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_LEFT:
            if not self.engine_rev_player or not self.engine_rev_player.playing:
                self.engine_rev_player = arcade.play_sound(self.engine_rev)

    def update(self, delta_time):
        self.car2.update()

    # control the blue car using the arrow keys
    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.car2.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.car2.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.car2.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.car2.change_y = -MOVEMENT_SPEED

    # stop movement
    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.car2.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.car2.change_y = 0


def main():
    window = MyGame(800, 600, "Racecar")
    arcade.run()


main()
