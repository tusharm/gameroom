import arcade

MOVEMENT_SIZE = 5


class Sprite(arcade.Sprite):
    def __init__(self, image_name, center_x=0.0, center_y=0.0, scale=1.0, angle=0.0):
        super().__init__(f'images/{image_name}.png', center_x=center_x, center_y=center_y, scale=scale, angle=angle)

        self.key_aware = False
        self.key_rrotate = None
        self.key_lrotate = None
        self.key_left = None
        self.key_right = None
        self.key_down = None
        self.key_up = None

    def keys(self, up, down, right, left, lrotate, rrotate):
        self.key_aware = True

        self.key_up = up
        self.key_down = down
        self.key_right = right
        self.key_left = left
        self.key_lrotate = lrotate
        self.key_rrotate = rrotate

    def on_key_press(self, key: int, key_modifiers: int):
        if not self.key_aware:
            return

        # setting change_x/change_y is not working, so updating center directly
        if key == self.key_up:
            self.center_y += MOVEMENT_SIZE
        elif key == self.key_down:
            self.center_y -= MOVEMENT_SIZE
        elif key == self.key_left:
            self.center_x -= MOVEMENT_SIZE
        elif key == self.key_right:
            self.center_x += MOVEMENT_SIZE
        elif key == self.key_lrotate:
            self.turn_left()
        elif key == self.key_rrotate:
            self.turn_right()

    def on_key_release(self, key: int, key_modifiers: int):
        if not self.key_aware:
            return

        if key == self.key_up \
                or key == self.key_down \
                or key == self.key_left \
                or key == self.key_right \
                or key == self.key_lrotate \
                or key == self.key_rrotate:
            self.stop()
