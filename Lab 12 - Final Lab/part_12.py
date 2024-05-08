import arcade

# constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 6
JUMP_SPEED = 15
GRAVITY = 0.8
ANIMATION_SPEED = .06
NUMBER_OF_SPIKES = 3
# width of each sprite in the sprite sheet
DESIRED_LENGTH = 63


class Player(arcade.Sprite):
    def __init__(self):
        super().__init__()
        # texture and sprite sheet from https://benvictus.itch.io/pixel-dogs?download
        self.texture = arcade.load_texture("Dog_White_Brown_Run.png")
        self.textures = []

        # Load individual textures from sprite sheet
        for i in range(8):
            texture = arcade.load_texture("Dog_White_Brown_Run.png", x=i * DESIRED_LENGTH, y=0, width=DESIRED_LENGTH,
                                          height=52)
            self.textures.append(texture)

        self.scale = 2
        self.set_texture(0)
        self.center_x = SCREEN_WIDTH / 2
        self.center_y = SCREEN_HEIGHT / 2
        self.change_x = 0
        self.change_y = 0
        self.jumping = False
        self.frame = 0
        self.animation_timer = 0

    # update the animation for the dog
    def update_animation(self, delta_time: float):
        # animate the sprite
        self.animation_timer += delta_time
        if self.animation_timer >= ANIMATION_SPEED:
            self.frame += 1
            if self.frame >= 8:
                self.frame = 0
            self.set_texture(self.frame)
            self.animation_timer = 0


class Floor(arcade.Sprite):
    def __init__(self, image, scale):
        super().__init__(image, scale)
        self.center_y = 50

    def update(self):
        self.center_x += MOVEMENT_SPEED
        if self.center_x >= 800:
            self.center_x = 0


class Background(arcade.Sprite):
    def __init__(self, image, scale):
        super().__init__(image, scale)
        self.center_x = 400
        self.center_y = 300

    def update(self):
        self.center_x += 1
        if self.center_x >= 800:
            self.center_x = 0


class Spike(arcade.Sprite):
    def __init__(self, image, scale):
        super().__init__(image, scale)
        self.center_x = 0
        self.center_y = 0

    def update(self):
        self.center_x += MOVEMENT_SPEED
        if self.center_x >= 800:
            self.center_x = 0


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.player = None
        self.floor_list = None
        self.physics_engine = None
        self.background = None
        self.background_list = None
        self.game_over = False
        self.spike_list = []

        # load start screen image
        # start screen drawn by Cassie Witt :)
        self.start = arcade.load_texture("start.jpg")
        self.show_start = True

        # load game over screen
        # game over screen also made by Cassie Witt
        self.done = arcade.load_texture("game_over.jpg")
        self.show_done = False

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        self.platform_list = None

        self.score = 0

        self.physics_engine = None

        # load sounds
        # sound downloaded from https://ansimuz.itch.io/adventure-music-collection-pack-1
        self.music = arcade.load_sound("hurry_up_and_run.wav")
        self.music_player = None
        self.music_started = False

        # timer for increasing score
        self.score_timer = 0

    def setup(self):
        self.player = Player()
        self.score = 0
        self.floor_list = arcade.SpriteList()
        self.background_list = arcade.SpriteList()
        self.spike_list = arcade.SpriteList()

        # add floor sprites
        floor_spacing = 90
        for i in range(10):
            # ground sprite downloaded from https://mariaparragames.itch.io/free-retro-city-assetpack
            floor = Floor("city_ground.png", 2)
            floor.center_x = i * floor_spacing
            self.floor_list.append(floor)

        # add background
        background_spacing = 800
        for i in range(2):
            # background downloaded from https://free-game-assets.itch.io/free-city-backgrounds-pixel-art
            background = Background("background.png", 0.4)
            background.center_x = i * background_spacing
            self.background_list.append(background)

        # add spikes
        for i in range(3):
            # spike downloaded from https://mariaparragames.itch.io/free-retro-city-assetpack
            spike = Spike("city_spike.png", 3)
            spike.center_x = 0
            spike.center_y = 120
            self.spike_list.append(spike)

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player, self.floor_list, gravity_constant=GRAVITY)

    def on_draw(self):
        arcade.start_render()

        # if the game has started and isn't over yet
        if not self.show_start and not self.game_over:
            self.background_list.draw()
            self.player.draw()
            self.floor_list.draw()
            self.spike_list.draw()

            # Put the text on the screen.
            output = f"Score: {self.score}"
            arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

        # start screen
        if self.show_start:
            arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT,
                                          self.start)

        # game over screen
        if self.game_over:
            arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT,
                                          self.done)
            final_score = f"Final Score: {self.final_score}"
            arcade.draw_text(final_score, 550, 550, arcade.color.WHITE, 24)

    def on_update(self, delta_time):
        # if the game has started and hasn't ended
        if not self.game_over and not self.show_start:
            self.physics_engine.update()

            # move background
            for background in self.background_list:
                background.update()
                if background.center_x >= 800:
                    background.center_x = -200

            # check if player stopped jumping
            if self.player.center_y <= 130:
                self.player.jumping = False
                self.player.change_y = 0

            self.player.update_animation(delta_time)
            self.player.update()
            self.floor_list.update()

            # update score for how long the layer survives
            self.score_timer += delta_time
            if self.score_timer >= 0.5:
                self.score += 1
                self.score_timer = 0

            # update spikes and check for game over requirements
            for spike in self.spike_list:
                spike.update()
                if arcade.check_for_collision(self.player, spike):
                    self.game_over = True
                    self.final_score = self.score
                    if self.music_player:
                        arcade.stop_sound(self.music_player)

    def on_key_press(self, key, modifiers):
        # when up or space is pressed, remove the start screen and play music
        if self.show_start:
            if key == arcade.key.UP or key == arcade.key.SPACE:
                self.show_start = False
                self.setup()
                if not self.music_started:
                    self.music_player = arcade.play_sound(self.music, looping=True)
                    self.music_started = True
        # make the player jump if up or space is pressed
        else:
            if key == arcade.key.UP or key == arcade.key.SPACE:
                if not self.player.jumping:
                    self.player.change_y = JUMP_SPEED
                    self.player.jumping = True


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Bathtime!")
    game.setup()
    arcade.run()


main()
