import pygame
pygame.init()

import _other_470.const
import _other_470.objects


def gamestart():
    _other_470.objects.music_play("gameplay")

    # Создаём отслеживание пересечений синего квадрата с красным
    _other_470.objects.collide_blue_and_red()

    # Создаём отслеживание пересечений синего квадрата с жёлтым
    _other_470.objects.collide_blue_and_yel()

    # Создаём движение синего квадрата
    _other_470.objects.move_blue_squ()

    # Создаём движение красного квадрата
    _other_470.objects.move_red_squ()

    # Всё заполняется черным цветом
    _other_470.const.scr.fill(pygame.Color('black'))

    # Рисуем жёлтые квадраты
    for ind_draw_yel in range(_other_470.const.count_yel_squ):
        _other_470.const.scr.blit(_other_470.objects.lil_yel_squ[ind_draw_yel].py_object,
        (_other_470.objects.lil_yel_squ[ind_draw_yel].x,
        _other_470.objects.lil_yel_squ[ind_draw_yel].y))

    # Рисуем красные квадраты
    for ind_draw in range(_other_470.const.count_red_squ):
        _other_470.const.scr.blit(_other_470.objects.lil_red_squ[ind_draw].py_object,
        (_other_470.objects.lil_red_squ[ind_draw].x,
        _other_470.objects.lil_red_squ[ind_draw].y))

    # Рисуем линию здоровья
    _other_470.objects.hp_line(_other_470.const.parem_blue["hp"],
    _other_470.objects.blue_squ.parem["hp"], 0, 0)

    # Рисуем текстовую надпись. Здоровье и очки.
    _other_470.const.scr.blit(_other_470.const.my_font.render((" hp " +
    str(_other_470.objects.blue_squ.parem["hp"]) + "        score " +
    str(_other_470.objects.blue_squ.parem["score"])), False,
    "blue"), (0, 0))

    _other_470.objects.button_menu((_other_470.const.wid - 100, 0))

    # Рисуем синий квадрат
    _other_470.const.scr.blit(_other_470.objects.blue_squ.py_object, (_other_470.objects.blue_squ.x,
    _other_470.objects.blue_squ.y))

    # Если здоровье закончилось, то игра завершается
    if _other_470.objects.blue_squ.parem["hp"] <= 0:
        # Статус игры закончилась
        _other_470.const.game_status = _other_470.const.scene3

    # Если будет накоплено 470 очков
    if _other_470.objects.blue_squ.parem["score"] >= 470:
        # Статус игры пройдена
        _other_470.const.game_status = _other_470.const.scene4
