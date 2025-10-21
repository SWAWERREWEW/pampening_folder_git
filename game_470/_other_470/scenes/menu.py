import pygame
pygame.init()

import _other_470.const
import _other_470.objects


def menu():
    # Заполняем всё чёрным
    _other_470.const.scr.fill(pygame.Color("black"))

    _other_470.objects.music_play("menu")

    _other_470.objects.button_restart((100, _other_470.const.hei // 2))
    _other_470.objects.button_start((100, _other_470.const.hei // 2 - 50))
    _other_470.objects.button_load((100, _other_470.const.hei // 2 + 50))
    _other_470.objects.button_save((300, _other_470.const.hei // 2 + 50))

    # Рисуем надпись названия игры
    _other_470.const.scr.blit(_other_470.const.my_font.render(" Game 470 ", False, "yellow"),
    (100, _other_470.const.hei // 2 - 100))

    # Рисуем надпись ХП
    _other_470.const.scr.blit(_other_470.const.my_font.render(" hp " +
    str(_other_470.objects.save_blue["parem"]["hp"]), False, "green"),
    (100, _other_470.const.hei // 2 + 100))

    # Рисуем надпись очки
    _other_470.const.scr.blit(_other_470.const.my_font.render(" score " +
    str(_other_470.objects.save_blue["parem"]["score"]), False, "yellow"),
    (100, _other_470.const.hei // 2 + 150))