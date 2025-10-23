import pygame
import _other.cons

pygame.init()

is_clicked_button_prayer_10 = False

def five() -> int: return 5


def button_prayer_10():
    global is_clicked_button_prayer_10
    text = " ewoppwpoweewrwer "
    colors = ("black",  "white")
    colors2 = ("yellow", "black")

    text_py = _other.cons.my_font.render(text, False, colors[0], colors[1])

    coord = (0, 0)

    text_rect = text_py.get_rect(topleft=coord)

    mouse = pygame.mouse.get_pos()

    keys = pygame.key.get_pressed()

    if text_rect.collidepoint(mouse):
        text_py = _other.cons.my_font.render(text, False, colors2[0], colors2[1])
    else:
        text_py = _other.cons.my_font.render(text, False, colors[0], colors[1])

    if text_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
        text_py = _other.cons.my_font.render(text, False, colors2[0], colors2[1])
        is_clicked_button_prayer_10 = True
    else: is_clicked_button_prayer_10 = False


    _other.cons.scr.blit(text_py, coord)


def effect_button_prayer_10(): _other.cons.test_parem += 1