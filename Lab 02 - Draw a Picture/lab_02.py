import arcade

arcade.open_window(800, 600, "Orange")

arcade.set_background_color(arcade.color.BEAVER)

arcade.start_render()

# table
arcade.draw_lrtb_rectangle_filled(0, 800, 350, 0, arcade.color.BULGARIAN_ROSE)


# window
arcade.draw_lrtb_rectangle_filled(600, 730, 580, 380, arcade.color.LICORICE)

# window sky
arcade.draw_lrtb_rectangle_filled(610, 720, 570, 390, arcade.color.GLAUCOUS)

# window grass
arcade.draw_lrtb_rectangle_filled(610, 720, 450, 390, arcade.color.JAPANESE_INDIGO)

# window section 1
arcade.draw_lrtb_rectangle_filled(610, 720, 485, 475, arcade.color.LICORICE)

# window section 2
arcade.draw_lrtb_rectangle_filled(660, 670, 570, 390, arcade.color.LICORICE)


# orange shadow
arcade.draw_lrtb_rectangle_filled(0, 250, 170, 100, arcade.color.LICORICE)

# orange
arcade.draw_circle_filled(250, 300, 200, arcade.color.BURNT_ORANGE)

# orange highlight
arcade.draw_circle_filled(275, 340, 150, arcade.color.CADMIUM_ORANGE)

# stem shadow
arcade.draw_lrtb_rectangle_filled(220, 260, 470, 450, arcade.color.BURNT_ORANGE)

# stem
arcade.draw_lrtb_rectangle_filled(240, 260, 520, 450, arcade.color.BULGARIAN_ROSE)

# stem highlight
arcade.draw_lrtb_rectangle_filled(250, 260, 520, 450, arcade.color.FALU_RED)


# orange slice shadow
arcade.draw_lrtb_rectangle_filled(350, 550, 80, 50, arcade.color.LICORICE)

# orange slice
arcade.draw_parabola_filled(400, 500, 700, -300, arcade.color.BURNT_ORANGE)

# orange slice inside
arcade.draw_parabola_filled(420, 480, 680, -280, arcade.color.FLAVESCENT)

# orange slice section 1
arcade.draw_triangle_filled(545, 70, 545, 200, 470, 100, arcade.color.CADMIUM_ORANGE)

# orange slice section 2
arcade.draw_triangle_filled(555, 70, 555, 200, 630, 100, arcade.color.CADMIUM_ORANGE)

# orange slice section 3
arcade.draw_triangle_filled(460, 110, 535, 200, 430, 200, arcade.color.CADMIUM_ORANGE)

# orange slice section 4
arcade.draw_triangle_filled(640, 110, 670, 200, 565, 200, arcade.color.CADMIUM_ORANGE)


arcade.finish_render()

arcade.run()
