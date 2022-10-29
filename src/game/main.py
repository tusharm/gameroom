import random

import arcade

from lib.game import Game
from lib.sprite import Sprite


# create a game
game = Game()

# add a ship sprite
ship = Sprite('ship', center_x=game.width / 2, center_y=game.height / 2, scale=0.5)
ship.keys(
    up=arcade.key.UP,
    down=arcade.key.DOWN,
    right=arcade.key.RIGHT,
    left=arcade.key.LEFT,
    lrotate=arcade.key.Q,
    rrotate=arcade.key.W
)
game.add_sprite(ship)

# add a bunch of meteors randomly


# This must be the last call in the program
game.run()
