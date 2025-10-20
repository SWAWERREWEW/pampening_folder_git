import pygame
import _other.cons

pygame.init()

def five() -> int:
    return 5

def button_prayer_10():


    text = " ewoppwpoweewrwer "
    colors = ("black",  "white")
    colors2 = ("yellow", "grey")

    text_py = _other.cons.my_font.render(text, False, colors[0], colors[1])

    coord = (0, 0)

    text_rect = text_py.get_rect(topleft=coord)

    mouse = pygame.mouse.get_pos()

    keys = pygame.key.get_pressed()

    if text_rect.collidepoint(mouse):
        text_py = _other.cons.my_font.render(text, False, colors2[0], colors2[1])
    else:
        text_py = _other.cons.my_font.render(text, False, colors[0], colors[1])

    _other.cons.scr.blit(text_py, coord)
