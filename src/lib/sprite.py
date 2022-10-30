import math

import arcade

MOVEMENT_SIZE = 5.0


class Sprite(arcade.Sprite):
    def __init__(self, image_name, center_x=0.0, center_y=0.0, scale=1.0, initial_bearing=90):
        """
        Creates a sprite from an image file
        Args:
            image_name: Name of the image in the `images` folder, excluding the extension (assumes png format)
            center_x:
            center_y:
            scale:
            initial_bearing: the direction pointed to by the image (in degrees)
        """
        super().__init__(f'images/{image_name}.png', center_x=center_x, center_y=center_y, scale=scale)

        self.initial_bearing = math.radians(initial_bearing)
        self._interactive = False
        self.key_pressed = None

        self.key_rrotate = None
        self.key_lrotate = None
        self.key_forward = None
        self.key_backward = None

    @property
    def interactive(self):
        return self._interactive

    def keys(self, forward=None, backward=None, lrotate=None, rrotate=None):
        self._interactive = True

        self.key_forward = forward
        self.key_backward = backward
        self.key_lrotate = lrotate
        self.key_rrotate = rrotate

    def on_key_press(self, key: int, key_modifiers: int):
        if not self._interactive:
            return

        self.key_pressed = key

    def on_key_release(self, key: int, key_modifiers: int):
        if not self._interactive:
            return

        self.key_pressed = None

    def on_update(self, delta_time: float = 1 / 60):
        if not self.key_pressed:
            self.stop()
        else:
            # setting change_x/change_y is not working, so updating center directly
            if self.key_pressed == self.key_forward:
                self._move(speed=MOVEMENT_SIZE)
            elif self.key_pressed == self.key_backward:
                self._move(speed=-MOVEMENT_SIZE)
            elif self.key_pressed == self.key_lrotate:
                self.turn_left(theta=5)
            elif self.key_pressed == self.key_rrotate:
                self.turn_right(theta=5)

    def _move(self, speed: float):
        self.center_x += math.cos(self.initial_bearing + self.radians) * speed
        self.center_y += math.sin(self.initial_bearing + self.radians) * speed
