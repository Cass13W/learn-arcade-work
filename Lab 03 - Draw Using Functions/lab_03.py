import arcade


def draw_table():
    """draw the table"""
    arcade.draw_lrtb_rectangle_filled(0, 800, 350, 0, arcade.color.BULGARIAN_ROSE)


def draw_outside(x, y):
    """draw the sky and grass"""
    # window sky
    arcade.draw_lrtb_rectangle_filled(x, 100 + x, 560 + y, 400 + y, arcade.color.GLAUCOUS)

    # window grass
    arcade.draw_lrtb_rectangle_filled(x, 100 + x, 450 + y, 390 + y, arcade.color.JAPANESE_INDIGO)


def draw_cloud(x, y):
    """draw a cloud"""
    # cloud
    arcade.draw_lrtb_rectangle_filled(x, 50 + x, 100 + y, 90 + y, arcade.color.WHITE)

    arcade.draw_circle_filled(x, 510, 20, arcade.color.WHITE)

    arcade.draw_circle_filled(55 + x, 510, 15, arcade.color.WHITE)

    arcade.draw_circle_filled(25 + x, 520, 30, arcade.color.WHITE)


def draw_window(x, y):
    """draw the window frame"""
    # window section 1
    arcade.draw_lrtb_rectangle_filled(x, 110 + x, 485 + y, 475 + y, arcade.color.LICORICE)

    # window section 2
    arcade.draw_lrtb_rectangle_filled(50 + x, 60 + x, 570 + y, 390 + y, arcade.color.LICORICE)

    # window section left
    arcade.draw_lrtb_rectangle_filled(x, 10 + x, 570 + y, 390 + y, arcade.color.LICORICE)

    # window section right
    arcade.draw_lrtb_rectangle_filled(100 + x, 110 + x, 570 + y, 390 + y, arcade.color.LICORICE)

    # window section top
    arcade.draw_lrtb_rectangle_filled(x, 110 + x, 570 + y, 560 + y, arcade.color.LICORICE)

    # window section bottom
    arcade.draw_lrtb_rectangle_filled(x, 110 + x, 390 + y, 380 + y, arcade.color.LICORICE)


def draw_hidden(x, y):
    """draw a rectangle to hide the cloud moving between windows"""
    arcade.draw_lrtb_rectangle_filled(150 + x, 345 + x, 570 + y, 380 + y, arcade.color.BEAVER)


def draw_orange(x, y):
    """draw an orange"""
    # orange shadow
    arcade.draw_lrtb_rectangle_filled(x, 250 + x, 170 + y, 100 + y, arcade.color.LICORICE)

    # orange
    arcade.draw_circle_filled(x, 300 + y, 200, arcade.color.BURNT_ORANGE)

    # orange highlight
    arcade.draw_circle_filled(20 + x, 340 + y, 150, arcade.color.CADMIUM_ORANGE)

    # stem shadow
    arcade.draw_lrtb_rectangle_filled(x, 40 + x, 470 + y, 450 + y, arcade.color.BURNT_ORANGE)

    # stem
    arcade.draw_lrtb_rectangle_filled(x, 20 + x, 520 + y, 450 + y, arcade.color.BULGARIAN_ROSE)

    # stem highlight
    arcade.draw_lrtb_rectangle_filled(x, 10 + x, 520 + y, 450 + y, arcade.color.FALU_RED)


def draw_slice(x, y):
    """draw orange slice"""
    # orange slice shadow
    arcade.draw_lrtb_rectangle_filled(150 + x, 500 + x, 80 + y, 50 + y, arcade.color.LICORICE)

    # orange slice
    arcade.draw_parabola_filled(x, 500 + y, 300 + x, -300, arcade.color.BURNT_ORANGE)

    # orange slice inside
    arcade.draw_parabola_filled(20 + x, 480 + y, 280 + x, -280, arcade.color.FLAVESCENT)

    # orange slice section 1
    arcade.draw_triangle_filled(155 + x, 70 + y, 155 + x, 200 + y, 230 + x, 100 + y, arcade.color.CADMIUM_ORANGE)

    # orange slice section 2
    arcade.draw_triangle_filled(145 + x, 70 + y, 145 + x, 200 + y, 75 + x, 100 + y, arcade.color.CADMIUM_ORANGE)

    # orange slice section 3
    arcade.draw_triangle_filled(60 + x, 110 + y, 30 + x, 200 + y, 130 + x, 200 + y, arcade.color.CADMIUM_ORANGE)

    # orange slice section 4
    arcade.draw_triangle_filled(240 + x, 110 + y, 270 + x, 200 + y, 170 + x, 200 + y, arcade.color.CADMIUM_ORANGE)


def on_draw(delta_time):
    """ draw everything """
    arcade.start_render()

    # table
    draw_table()

    # outside
    draw_outside(50, 0)

    draw_outside(350, 0)

    draw_outside(650, 0)

    # cloud
    draw_cloud(on_draw.cloud1_x, 420)

    on_draw.cloud1_x = (on_draw.cloud1_x + 0.5) % 800

    # windows
    draw_window(40, 0)

    draw_window(650, 0)

    draw_window(345, 0)

    # hidden layer
    draw_hidden(0, 0)

    draw_hidden(305, 0)

    draw_hidden(-305, 0)

    draw_hidden(610, 0)

    # orange
    draw_orange(250, 20)

    # orange slice
    draw_slice(450, 0)

    arcade.finish_render()


on_draw.cloud1_x = 0


def main():
    arcade.open_window(800, 600, "Orange w/ Functions")

    arcade.set_background_color(arcade.color.BEAVER)

    arcade.schedule(on_draw, 1 / 60)

    arcade.finish_render()

    arcade.run()


main()
