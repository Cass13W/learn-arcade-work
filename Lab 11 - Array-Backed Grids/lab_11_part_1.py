import arcade

ROW_COUNT = 10
COLUMN_COUNT = 10
WIDTH = 20
HEIGHT = 20
MARGIN = 5
SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN


class MyGame(arcade.Window):

    def __init__(self, width, height):
        """
        Set up the application.
        """
        super().__init__(width, height)
        self.grid = []
        for row in range(ROW_COUNT):
            # Add an empty array
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(0)

        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):

        arcade.start_render()

        # Draw the grid
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                # Figure out what color to draw the box
                if self.grid[row][column] == 1:
                    color = arcade.color.GREEN
                else:
                    color = arcade.color.WHITE

                # figure out where the box is
                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2

                # Draw the box
                arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)

    def on_mouse_press(self, x, y, button, modifiers):

        # Change the x/y screen coordinates to grid coordinates
        column = x // (WIDTH + MARGIN)
        row = y // (HEIGHT + MARGIN)

        print(f"Click coordinates: ({x}, {y}). Grid coordinates: ({row}, {column})")

        # Make sure we are on-grid.
        if row < ROW_COUNT and column < COLUMN_COUNT:

            # Flip the location between 1 and 0.
            if self.grid[row][column] == 0:
                self.grid[row][column] = 1

            else:
                self.grid[row][column] = 0

            # call test_n_set to select adjacent squares
            self.test_n_set(row, column)

    def test_n_set(self, x, y):
        # Change the color of the selected square
        self.grid[x][y] = 1 - self.grid[x][y]

        # Define the coordinates for the shape
        plus_sign_coords = [  # selected square
            (x, y),
            # top
            (x - 1, y),
            # bottom
            (x + 1, y),
            # left
            (x, y - 1),
            # right
            (x, y + 1)]

        # change colors after a square is selected based on the available space on the grid
        for x_coord, y_coord in plus_sign_coords:
            if 0 <= x_coord < ROW_COUNT and 0 <= y_coord < COLUMN_COUNT:
                self.grid[x_coord][y_coord] = 1 - self.grid[x_coord][y_coord]


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()
