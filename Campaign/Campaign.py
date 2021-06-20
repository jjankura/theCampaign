import random
import arcade


SPRITE_SCALING = 1.5
SPRITE_SCALING_BOX = 0.175
HOUSE_SCALE = 0.12

SCREEN_WIDTH = 1300
SCREEN_HEIGHT = 800
SCREEN_TITLE = "The Campaign"

MOVEMENT_SPEED = 2
PURPLE_SPEED = 0.3

LEFT_VIEWPORT_MARGIN = SCREEN_WIDTH / 2
RIGHT_VIEWPORT_MARGIN = SCREEN_WIDTH / 2
BOTTOM_VIEWPORT_MARGIN = SCREEN_HEIGHT / 2
TOP_VIEWPORT_MARGIN = SCREEN_HEIGHT / 2

PURPLE_POP = 30
GREEN_POP = 15

# ----------------------------------------------------------------------------------------------


class GameView(arcade.View):
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
        self.viper_sprite_list = None
        self.wall_list = None
        self.purple_snake_list = None
        self.green_snake_list = None
        self.house_list = None

        # Set up the player info
        self.player_sprite = None
        self.viper_sprite = None
        self.psnake = None
        self.gsnake = None
        self.cityHall = None
        self.house = None

        # Sets score to 0
        self.pscore = 0
        self.gscore = 0
        self.viper_pscore = 0
        self.viper_gscore = 0

        # Used to keep track of our scrolling
        self.view_bottom = 0
        self.view_left = 0

        # Set the background color
        arcade.set_background_color(arcade.color.DODGER_BLUE)

        self.left_boundary = None
        self.right_boundary = None
        self.top_boundary = None
        self.bottom_boundary = None

        self.background = None

        self.viper_destination = None

        self.path = None

    def setupIsland(self):
        """ Set up the game and initialize the variables. """

        self.background = arcade.load_texture("images/campaign.png")

        # Sprite lists
        self.wall_list = arcade.SpriteList()
        self.purple_snake_list = arcade.SpriteList()
        self.green_snake_list = arcade.SpriteList()
        self.player_sprite_list = arcade.SpriteList()
        self.viper_sprite_list = arcade.SpriteList()
        self.house_list = arcade.SpriteList()

        # Used to keep track of our scrolling
        self.view_bottom = 0
        self.view_left = 0

        # self.player_sprite = Player()
        self.player_sprite = arcade.Sprite("images/Sssam.png", SPRITE_SCALING)
        self.player_sprite.center_x = 1120
        self.player_sprite.center_y = 255
        self.player_sprite_list.append(self.player_sprite)

        self.viper_sprite = arcade.Sprite("images/Viper.png", SPRITE_SCALING)
        self.viper_sprite.center_x = 360
        self.viper_sprite.center_y = 270
        self.viper_sprite.change_x = random.random()
        self.viper_sprite.change_y = random.random()
        self.viper_sprite_list.append(self.viper_sprite)

        self.cityHall = arcade.Sprite("images/cityhall.png", SPRITE_SCALING_BOX)
        self.cityHall.center_x = 335
        self.cityHall.center_y = 350
        self.house_list.append(self.cityHall)

        for i in range(PURPLE_POP):
            self.psnake = arcade.Sprite("images/PurpleSnake.png", SPRITE_SCALING)
            # Position the snake
            self.psnake.center_x = random.randrange(110, 820)
            self.psnake.center_y = random.randrange(120, 710)
            # Add the snake to the lists
            self.purple_snake_list.append(self.psnake)

        for i in range(GREEN_POP - 5):
            self.gsnake = arcade.Sprite("images/GreenSnake.png", SPRITE_SCALING)
            # Position the snake
            self.gsnake.center_x = random.randrange(830, 1000)
            self.gsnake.center_y = random.randrange(300, 710)
            # Add the snake to the lists
            self.green_snake_list.append(self.gsnake)

        for i in range(GREEN_POP - 10):
            self.gsnake = arcade.Sprite("images/GreenSnake.png", SPRITE_SCALING)
            # Position the snake
            self.gsnake.center_x = random.randrange(830, 1000)
            self.gsnake.center_y = random.randrange(120, 300)
            # Add the snake to the lists
            self.green_snake_list.append(self.gsnake)

        self.house = arcade.Sprite("images/house.png", HOUSE_SCALE)
        self.house.center_x = 550
        self.house.center_y = 300
        self.house_list.append(self.house)

        self.house = arcade.Sprite("images/house.png", HOUSE_SCALE)
        self.house.center_x = 550
        self.house.center_y = 420
        self.house_list.append(self.house)

        self.house = arcade.Sprite("images/house.png", HOUSE_SCALE)
        self.house.center_x = 550
        self.house.center_y = 540
        self.house_list.append(self.house)

        self.house = arcade.Sprite("images/house.png", HOUSE_SCALE)
        self.house.center_x = 550
        self.house.center_y = 660
        self.house_list.append(self.house)

        self.house = arcade.Sprite("images/house.png", HOUSE_SCALE)
        self.house.center_x = 350
        self.house.center_y = 640
        self.house_list.append(self.house)

        self.house = arcade.Sprite("images/house.png", HOUSE_SCALE)
        self.house.center_x = 655
        self.house.center_y = 300
        self.house_list.append(self.house)

        self.house = arcade.Sprite("images/house.png", HOUSE_SCALE)
        self.house.center_x = 655
        self.house.center_y = 420
        self.house_list.append(self.house)

        self.house = arcade.Sprite("images/house.png", HOUSE_SCALE)
        self.house.center_x = 655
        self.house.center_y = 540
        self.house_list.append(self.house)

        self.house = arcade.Sprite("images/house.png", HOUSE_SCALE)
        self.house.center_x = 655
        self.house.center_y = 660
        self.house_list.append(self.house)

        self.house = arcade.Sprite("images/house.png", HOUSE_SCALE)
        self.house.center_x = 755
        self.house.center_y = 540
        self.house_list.append(self.house)

        self.house = arcade.Sprite("images/house.png", HOUSE_SCALE)
        self.house.center_x = 1060
        self.house.center_y = 540
        self.house_list.append(self.house)

        self.house = arcade.Sprite("images/house.png", HOUSE_SCALE)
        self.house.center_x = 1060
        self.house.center_y = 400
        self.house_list.append(self.house)

        self.house = arcade.Sprite("images/house.png", HOUSE_SCALE)
        self.house.center_x = 1060
        self.house.center_y = 660
        self.house_list.append(self.house)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        # Draw all the sprites.
        self.wall_list.draw()
        self.house_list.draw()
        self.player_sprite_list.draw()
        self.viper_sprite_list.draw()
        self.purple_snake_list.draw()
        self.green_snake_list.draw()
        self.scoreboard()

    def on_update(self, delta_time):
        """ Movement and game logic """
        self.player_sprite_list.update()
        self.viper_sprite_list.update()
        self.purple_snake_list.update()
        self.green_snake_list.update()

        # Moving Viper
        self.viper_sprite.center_x += self.viper_sprite.change_x
        self.viper_sprite.center_y += self.viper_sprite.change_y

        # If Viper out-of-bounds, then 'bounce'
        if self.viper_sprite.left < 100:
            self.viper_sprite.change_x *= -1

        if self.viper_sprite.right > 1150:
            self.viper_sprite.change_x *= -1

        if self.viper_sprite.bottom < 110:
            self.viper_sprite.change_y *= -1

        if self.viper_sprite.top > 735:
            self.viper_sprite.change_y *= -1

        # If Sssam out-of-bounds, stop
        if self.player_sprite.left < 100:
            self.player_sprite.change_x = 0

        if self.player_sprite.right > 1150:
            self.player_sprite.change_x = 0

        if self.player_sprite.bottom < 110:
            self.player_sprite.change_y = 0

        if self.player_sprite.top > 735:
            self.player_sprite.change_y = 0

        # Check if Sssam hits house
        house_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.house_list)
        if len(house_hit_list) > 0:
            self.player_sprite.change_x *= -1
            self.player_sprite.change_y *= -1

        # Check if Viper hits house
        viper_house_hit_list = arcade.check_for_collision_with_list(self.viper_sprite, self.house_list)
        if len(viper_house_hit_list) > 0:
            self.viper_sprite.change_x *= -1
            self.viper_sprite.change_y *= -1

        # Check if psnake hits house
        """for self.psnake in self.purple_snake_list:
            psnake_house_hit_list = arcade.check_for_collision_with_list(self.psnake, self.house_list)
            if len(psnake_house_hit_list) > 0:
                self.psnake.change_x *= -1
                self.psnake.change_y *= -1"""

        # Call follow_viper() for all of the psnakes in the purple_snake_list
        for self.psnake in self.purple_snake_list:
            self.follow_viper(self.psnake)

        # Sssam collision with purple snakes
        purple_snake_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.purple_snake_list)
        for psnake in purple_snake_hit_list:
            psnake.remove_from_sprite_lists()
            self.pscore += 1

        # Sssam collision with green snakes
        green_snake_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.green_snake_list)
        for gsnake in green_snake_hit_list:
            gsnake.remove_from_sprite_lists()
            self.gscore += 1

        # Viper collision with purple snakes
        purple_snake_hit_list = arcade.check_for_collision_with_list(self.viper_sprite, self.purple_snake_list)
        for psnake in purple_snake_hit_list:
            psnake.remove_from_sprite_lists()
            self.viper_pscore += 1

        # Viper collision with green snakes
        green_snake_hit_list = arcade.check_for_collision_with_list(self.viper_sprite, self.green_snake_list)
        for gsnake in green_snake_hit_list:
            gsnake.remove_from_sprite_lists()
            self.viper_gscore += 1

        changed = False

        # Scroll left
        self.left_boundary = self.view_left + LEFT_VIEWPORT_MARGIN
        if self.player_sprite.left < self.left_boundary:
            self.view_left -= self.left_boundary - self.player_sprite.left
            changed = True

        # Scroll right
        self.right_boundary = self.view_left + SCREEN_WIDTH - RIGHT_VIEWPORT_MARGIN
        if self.player_sprite.right > self.right_boundary:
            self.view_left += self.player_sprite.right - self.right_boundary
            changed = True

        # Scroll up
        self.top_boundary = self.view_bottom + SCREEN_HEIGHT - TOP_VIEWPORT_MARGIN
        if self.player_sprite.top > self.top_boundary:
            self.view_bottom += self.player_sprite.top - self.top_boundary
            changed = True

        # Scroll down
        self.bottom_boundary = self.view_bottom + BOTTOM_VIEWPORT_MARGIN
        if self.player_sprite.bottom < self.bottom_boundary:
            self.view_bottom -= self.bottom_boundary - self.player_sprite.bottom
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

        # End game when either Sssam or Viper get a majority of 23
        if self.pscore + self.gscore == 23:
            view = GameOverWinView()
            self.window.show_view(view)
        if self.viper_pscore + self.viper_gscore == 23:
            view = GameOverLoseView()
            self.window.show_view(view)

        self.scoreboard()

    def follow_viper(self, psnake):

        if psnake.center_y < self.viper_sprite.center_y:
            psnake.center_y += min(PURPLE_SPEED, self.viper_sprite.center_y - psnake.center_y)
        elif psnake.center_y > self.viper_sprite.center_y:
            psnake.center_y -= min(PURPLE_SPEED, psnake.center_y - self.viper_sprite.center_y)

        if psnake.center_x < self.viper_sprite.center_x:
            psnake.center_x += min(PURPLE_SPEED, self.viper_sprite.center_x - psnake.center_x)
        elif psnake.center_x > self.viper_sprite.center_x:
            psnake.center_x -= min(PURPLE_SPEED, psnake.center_x - self.viper_sprite.center_x)

    def scoreboard(self):

        # Sssam scoreboard
        arcade.draw_rectangle_filled(self.right_boundary + 420, self.bottom_boundary - 360, 500, 120,
                                     arcade.csscolor.BLACK)

        # Draw pscore scoreboard
        output = f"Purple Votes: {self.pscore}"
        arcade.draw_text(output, self.right_boundary + 200, self.bottom_boundary - 405, arcade.color.MEDIUM_PURPLE, 25)

        # Draw gscore scoreboard
        output = f"Green Votes: {self.gscore}"
        arcade.draw_text(output, self.right_boundary + 200, self.bottom_boundary - 350, arcade.color.GREEN, 25)

        # Draw total scoreboard
        output = f"Total Votes: {self.pscore + self.gscore}"
        arcade.draw_text(output, self.right_boundary + 450, self.bottom_boundary - 405, arcade.color.WHITE, 25)

        arcade.draw_rectangle_filled(self.right_boundary + 428, self.bottom_boundary - 275, 110, 50,
                                     arcade.csscolor.GREEN)
        output = "Sssam"
        arcade.draw_text(output, self.right_boundary + 380, self.bottom_boundary - 290, arcade.color.WHITE, 25)

        # Viper scoreboard
        arcade.draw_rectangle_filled(self.right_boundary - 375, self.bottom_boundary - 360, 500, 120,
                                     arcade.csscolor.BLACK)

        # Draw pscore scoreboard
        output = f"Purple Votes: {self.viper_pscore}"
        arcade.draw_text(output, self.right_boundary - 595, self.bottom_boundary - 405, arcade.color.MEDIUM_PURPLE, 25)

        # Draw gscore scoreboard
        output = f"Green Votes: {self.viper_gscore}"
        arcade.draw_text(output, self.right_boundary - 595, self.bottom_boundary - 350, arcade.color.GREEN, 25)

        # Draw total scoreboard
        output = f"Total Votes: {self.viper_pscore + self.viper_gscore}"
        arcade.draw_text(output, self.right_boundary - 345, self.bottom_boundary - 405, arcade.color.WHITE, 25)

        arcade.draw_rectangle_filled(self.right_boundary - 380, self.bottom_boundary - 275, 100, 50,
                                     arcade.csscolor.MEDIUM_PURPLE)
        output = "Viper"
        arcade.draw_text(output, self.right_boundary - 415, self.bottom_boundary - 290, arcade.color.WHITE, 25)

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


class TitleView(arcade.View):

    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture("images/TITLE.png")

    def on_show(self):
        """Runs once we switch to this view"""
        arcade.set_background_color(arcade.csscolor.DARK_SLATE_BLUE)
        # Reset viewpoint back to 0,0
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

    def on_draw(self):
        """Draw this view"""

        arcade.start_render()

        self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT)

        """arcade.draw_text("Welcome to the Island of Python", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 50,
                         arcade.color.WHITE, font_size=50, anchor_x='center')
        arcade.draw_text("~ We're having an election for mayor!", 300, SCREEN_HEIGHT / 2-75, arcade.color.WHITE,
                         font_size=20, anchor_x='left')
        arcade.draw_text("~ The Island of Python is comprised of two different snakes: purple and green", 300,
                         SCREEN_HEIGHT / 2-105, arcade.color.WHITE, font_size=20, anchor_x='left')
        arcade.draw_text("~ You, a green snake named Sssam, have been nominated to run", 300, SCREEN_HEIGHT / 2-135,
                         arcade.color.WHITE, font_size=20, anchor_x='left')
        arcade.draw_text("~ You fear that it will be more difficult to win against the current purple mayor, Viper",
                         300, SCREEN_HEIGHT / 2-165, arcade.color.WHITE, font_size=20, anchor_x='left')
        arcade.draw_text("~ After all, purple snakes run the Island...", 300, SCREEN_HEIGHT / 2-195, arcade.color.WHITE,
                         font_size=20, anchor_x='left')
        arcade.draw_text('Click to advance', SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2-250, arcade.color.WHITE, font_size=20,
                         anchor_x='center')"""

    def on_mouse_press(self, _x, _y, button, _modifiers):
        """If the user presses the mouse button, start the game"""
        instruct = InstructionView()
        self.window.show_view(instruct)

# ----------------------------------------------------------------------------------------------


class InstructionView(arcade.View):

    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture("images/INSTRUCTIONS.png")

    def on_show(self):
        """Runs once we switch to this view"""
        arcade.set_background_color(arcade.csscolor.SEA_GREEN)
        # Reset viewpoint back to 0,0
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

    def on_draw(self):
        """Draw this view"""
        arcade.start_render()
        self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT)
        """arcade.draw_text("INSTRUCTIONS", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 50,
                         arcade.color.WHITE, font_size=50, anchor_x='center')
        arcade.draw_text("~ You will be competing to wins votes against the incumbent, Viper  ", 300,
                         SCREEN_HEIGHT / 2 - 75, arcade.color.WHITE, font_size=20, anchor_x='left')
        arcade.draw_text("~ Naturally, the purple snakes will favor Viper and want to give them their vote", 300,
                         SCREEN_HEIGHT / 2 - 105, arcade.color.WHITE, font_size=20, anchor_x='left')
        arcade.draw_text("~ Your job is to gain the majority of votes before all the votes are cast", 300,
                         SCREEN_HEIGHT / 2 - 135, arcade.color.WHITE, font_size=20, anchor_x='left')
        arcade.draw_text("~ Use your keyboard arrows to move Sssam", 300,
                         SCREEN_HEIGHT / 2 - 165, arcade.color.WHITE, font_size=20, anchor_x='left')
        arcade.draw_text("~ Good luck!",
                         300, SCREEN_HEIGHT / 2 - 195, arcade.color.WHITE, font_size=20, anchor_x='left')
        arcade.draw_text('Click to Start the Election', SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 250, arcade.color.WHITE,
                         font_size=20, anchor_x='center')"""

    def on_mouse_press(self, _x, _y, button, _modifiers):
        """If the user presses the mouse button, start the game"""
        game_view = GameView()
        game_view.setupIsland()
        self.window.show_view(game_view)


# ----------------------------------------------------------------------------------------------

class GameOverWinView(arcade.View):

    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture("images/WINNER.png")

    def on_show(self):
        """Runs once we switch to this view"""
        arcade.set_background_color(arcade.csscolor.GREEN)
        # Reset viewpoint back to 0,0
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

    def on_draw(self):
        """Draw this view"""
        arcade.start_render()
        self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT)
        """arcade.draw_text("Game Over! You've Won the Election!", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 50,
                         arcade.color.WHITE, font_size=50, anchor_x='center')
        arcade.draw_text("You received at least 23 votes!", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 105,
                         arcade.color.WHITE, font_size=40, anchor_x='center')"""

    def on_mouse_press(self, _x, _y, button, _modifiers):
        """If the user presses the mouse button, close the game"""
        arcade.close_window()
# ----------------------------------------------------------------------------------------------


class GameOverLoseView(arcade.View):

    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture("images/LOSER.png")

    def on_show(self):
        """Runs once we switch to this view"""
        arcade.set_background_color(arcade.csscolor.MEDIUM_PURPLE)
        # Reset viewpoint back to 0,0
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

    def on_draw(self):
        """Draw this view"""
        arcade.start_render()
        self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT)
        """arcade.draw_text("Game Over! You've Lost the Election!", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 50,
                         arcade.color.WHITE, font_size=50, anchor_x='center')
        arcade.draw_text("Viper won the election with 23 votes", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 105,
                         arcade.color.WHITE, font_size=40, anchor_x='center')"""

    def on_mouse_press(self, _x, _y, button, _modifiers):
        """If the user presses the mouse button, close the game"""
        arcade.close_window()

# ----------------------------------------------------------------------------------------------


def main():
    """ Main method """
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = TitleView()
    window.show_view(start_view)
    arcade.run()

# ----------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()
