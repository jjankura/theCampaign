import arcade

SPRITE_SCALING = 3.0
SPRITE_SCALING_BOX = 0.175

SCREEN_WIDTH = 1300
SCREEN_HEIGHT = 800
SCREEN_TITLE = "The Campaign"

MOVEMENT_SPEED = 3

# Constants used to scale our sprites from their original size
CHARACTER_SCALING = 1.5

# Index of textures, first element faces left, second faces right
TEXTURE_LEFT = 0
TEXTURE_RIGHT = 1

LEFT_VIEWPORT_MARGIN = SCREEN_WIDTH / 2
RIGHT_VIEWPORT_MARGIN = SCREEN_WIDTH / 2
BOTTOM_VIEWPORT_MARGIN = SCREEN_HEIGHT / 2
TOP_VIEWPORT_MARGIN = SCREEN_HEIGHT / 2

# ----------------------------------------------------------------------------------------------


class Player(arcade.Sprite):

    def __init__(self):
        super().__init__()

        self.scale = SPRITE_SCALING
        self.textures = []

        # Load a left facing texture and a right facing texture.
        # flipped_horizontally=True will mirror the image we load.
        texture = arcade.load_texture(":resources:images/GreenSnake.png")
        self.textures.append(texture)
        texture = arcade.load_texture(":resources:images/GreenSnake.png", flipped_horizontally=True)
        self.textures.append(texture)

        # By default, face right.
        self.texture = texture

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Figure out if we should face left or right
        if self.change_x < 0:
            self.texture = self.textures[TEXTURE_LEFT]
        elif self.change_x > 0:
            self.texture = self.textures[TEXTURE_RIGHT]

# ----------------------------------------------------------------------------------------------


class MyGameView(arcade.View):
    """
    Main application class.
    """

    def __init__(self):
        """
        Initializer
        """

        # Call the parent class initializer
        super().__init__()

        # Variables that will hold sprite lists
        self.player_sprite_list = None
        self.wall_list = None

        # Set up the player info
        self.player_sprite = None

        # Used to keep track of our scrolling
        self.view_bottom = 0
        self.view_left = 0

        # Set the background color
        arcade.set_background_color(arcade.color.DODGER_BLUE)

        self.background = None

    def setup(self):
        """ Set up the game and initialize the variables. """

        self.background = arcade.load_texture("images/campaign.png")

        # Sprite lists
        self.player_sprite_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        # Used to keep track of our scrolling
        self.view_bottom = 0
        self.view_left = 0

        # Set up the player
        image_source = "images/GreenSnake.png"

        # self.player_sprite = Player()
        self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
        self.player_sprite.center_x = 1075
        self.player_sprite.center_y = 255
        self.player_sprite_list.append(self.player_sprite)

        wall = arcade.Sprite("images/cityhall.png", SPRITE_SCALING_BOX)
        wall.center_x = 338
        wall.center_y = 350
        self.wall_list.append(wall)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        # Draw all the sprites.
        self.player_sprite_list.draw()
        self.wall_list.draw()

    def on_update(self, delta_time):
        """ Movement and game logic """
        self.player_sprite_list.update()

        changed = False

        # Scroll left
        left_boundary = self.view_left + LEFT_VIEWPORT_MARGIN
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left
            changed = True

        # Scroll right
        right_boundary = self.view_left + SCREEN_WIDTH - RIGHT_VIEWPORT_MARGIN
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary
            changed = True

        # Scroll up
        top_boundary = self.view_bottom + SCREEN_HEIGHT - TOP_VIEWPORT_MARGIN
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary
            changed = True

        # Scroll down
        bottom_boundary = self.view_bottom + BOTTOM_VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom
            changed = True

        if changed:
            # Only scroll to integers. Otherwise we end up with pixels that
            # don't line up on the screen
            self.view_bottom = int(self.view_bottom)
            self.view_left = int(self.view_left)

            # Do the scrolling
            arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom)

    def on_key_press(self, key, modifiers):
        """ Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED

        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

# ----------------------------------------------------------------------------------------------


class InstructionView(arcade.View):

    def on_show(self):
        """Runs once we switch to this view"""
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)
        # Reset viewpoint back to 0,0
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

    def on_draw(self):
        """Draw this view"""
        arcade.start_render()
        arcade.draw_text("Welcome to the Island of Python", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 50, arcade.color.WHITE, font_size=50, anchor_x='center')
        arcade.draw_text("~ We're having an election for mayor!", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2-75, arcade.color.WHITE, font_size=20, anchor_x='center')
        arcade.draw_text("~ You, Sssam, have been nominated by your friend Alecsss to run", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2-105, arcade.color.WHITE, font_size=20, anchor_x='center')
        arcade.draw_text("~ You aren't sure if you want to run because you know how difficult it will be to win as a green snake", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2-135, arcade.color.WHITE, font_size=20, anchor_x='center')
        arcade.draw_text("~ After all, purple snakes run the Island...", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2-165, arcade.color.WHITE, font_size=20, anchor_x='center')

        arcade.draw_text('Click to advance', SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2-250, arcade.color.WHITE, font_size=20, anchor_x='center')

    def on_mouse_press(self, _x, _y, button, _modifiers):
        """If the user presses the mouse button, start the game"""
        game_view = MyGameView()
        game_view.setup()
        self.window.show_view(game_view)

# ----------------------------------------------------------------------------------------------


class GameOverView(arcade.View):
    """Display when game is over"""

# ----------------------------------------------------------------------------------------------


def main():
    """ Main method """
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = InstructionView()
    window.show_view(start_view)
    arcade.run()


if __name__ == "__main__":
    main()
