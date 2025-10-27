import pygame
pygame.init()

import _other.buttons
import _other.obj
import _other.cons

def menu():

    _other.cons.scr.fill(pygame.Color("black"))

    _other.obj.quit()

    _other.buttons.button_start()

    if _other.cons.message['win?']:
        _other.cons.scr.blit(_other.cons.my_font.render("YOU WIN",
        False, "yellow"), (100, 200))

        _other.cons.scr.blit(_other.cons.my_font.render("Your last HP: " + _other.cons.message["hp_soul"] + "/92 HP",
        False, "yellow"),
        (100, 250))