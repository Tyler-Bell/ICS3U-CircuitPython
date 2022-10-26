#!/usr/bin/env python3

# Created by Tyler Bell
# Created on Oct 2022
# This program is the "Space Aliens" Program on the PyBadge

import ugame
import stage

def game_scene():
    # his function is the main game game_scene

    # image banks for CircuitPython
    image_bank_background = stage.bank.from_bmp16("space_aiens_background.bmp")

    # set the background to image 0 in the  image bank
    #   and the size (10x8 tiles of size 16x16)
    background = stage.Grid(image_bank_background, 10, 8)

    #create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = scene.Stage(ugame.display, 60)
    # set the layers of all sprites, items show up in order
    game.layers = [background]
    # render all sprites
    #   most likely you will only render the background once per scene
    game.render_block()

    # respect forever, game loop
    while True:
        pass # just a place holder for now

if __name__ == "__main__":
    game_scene()
