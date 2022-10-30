import random

import arcade

from lib.game import Game
from lib.sprite import Sprite

# create a game
game = Game()

# add a ship sprite
ship = Sprite('ship', center_x=game.width / 2, center_y=game.height / 2, scale=0.5, initial_bearing=90)
ship.keys(
    forward=arcade.key.UP,
    backward=arcade.key.DOWN,
    lrotate=arcade.key.LEFT,
    rrotate=arcade.key.RIGHT
)
game.add_sprite(ship)

# add a bunch of meteors randomly
meteor = Sprite('meteor', center_x=game.width / 2, center_y=(2. / 3.) * game.height)
game.add_sprite(meteor)

# This must be the last call in the program
game.run()
