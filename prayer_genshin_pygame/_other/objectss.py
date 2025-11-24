import pygame
import _other.cons

pygame.init()

is_clicked_button_prayer_10 = False

def five() -> int: return 5

lil_colors = ["green", "red", "blue", "yellow", "black", "white"]


def button_prayer_10():
    global lil_colors
    global is_clicked_button_prayer_10

    text = " Button "
    colors = ("black",  "white")
    colors2 = ("yellow", "black")

    text_py = _other.cons.my_font.render(text, False, colors[0], colors[1])

    coord = (_other.cons.wid-(_other.cons.wid//4), _other.cons.hei-100)

    text_rect = text_py.get_rect(topleft=coord)

    mouse = pygame.mouse.get_pos()

    if text_rect.collidepoint(mouse): text_py = _other.cons.my_font.render(text, False, colors2[0], colors2[1])
    else: text_py = _other.cons.my_font.render(text, False, colors[0], colors[1])

    if text_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
        text_py = _other.cons.my_font.render(text, False, colors2[0], colors2[1])
        is_clicked_button_prayer_10 = True
    else: is_clicked_button_prayer_10 = False

    _other.cons.scr.blit(text_py, coord)


def effect_button_prayer_10():
    global lil_colors

    from random import shuffle
    shuffle(lil_colors)
    _other.cons.active_color = lil_colors[0]