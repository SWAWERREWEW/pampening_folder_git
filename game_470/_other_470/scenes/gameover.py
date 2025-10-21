import pygame
pygame.init()

import _other_470.const
import _other_470.objects


def gameover():
    # Заполняем всё чёрным
    _other_470.const.scr.fill(pygame.Color("black"))

    _other_470.objects.music_play("gameover")

    _other_470.objects.button_restart((100, _other_470.const.hei // 2 + 50))
    _other_470.objects.button_menu((_other_470.const.wid - 100, 0))

    # Рисуем надпись проигрыша
    _other_470.const.scr.blit(_other_470.const.my_font.render(" game over ", False, "red"),
    (100, _other_470.const.hei // 2 - 100))

    # Рисуем надпись ХП
    _other_470.const.scr.blit(_other_470.const.my_font.render(" hp " +
    str(_other_470.objects.blue_squ.parem["hp"]), False,
    "red"), (100, _other_470.const.hei // 2 - 50))

    # Рисуем надпись очки
    _other_470.const.scr.blit(_other_470.const.my_font.render(" score " +
    str(_other_470.objects.blue_squ.parem["score"]), False,
    "red"), (100, _other_470.const.hei // 2 - 0))