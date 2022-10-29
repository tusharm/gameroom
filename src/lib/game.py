import arcade
import random

from lib.sprite import Sprite

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "My Awesome Game"


class Game(arcade.Window):
    def __init__(self, title=SCREEN_TITLE, width=SCREEN_WIDTH, height=SCREEN_HEIGHT):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

        self.sprites = arcade.SpriteList()

    def on_draw(self):
        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        self.sprites.draw()

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        self.sprites.on_update()

    def on_key_press(self, key, key_modifiers):
        for s in self.sprites:
            if getattr(s, "key_aware", None):
                s.on_key_press(key, key_modifiers)

    def on_key_release(self, key, key_modifiers):
        for s in self.sprites:
            if getattr(s, "key_aware", None):
                s.on_key_release(key, key_modifiers)

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass

    def add_sprite(self, sprite: Sprite):
        self.sprites.append(sprite)

    def run_every_seconds(self, fn, interval_in_secs: float):
        def scheduled_fn(delta_time: float):
            fn(self)

        arcade.schedule(scheduled_fn, interval_in_secs)

    def run(self):
        arcade.run()
