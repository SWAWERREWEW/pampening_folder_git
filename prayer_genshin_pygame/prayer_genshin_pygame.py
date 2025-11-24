import pygame
import _other.cons
import _other.objectss

pygame.init()

run = True

f = 0

clock = pygame.time.Clock()


while run:

    _other.cons.scr.fill(pygame.Color(_other.cons.active_color))

    # Надпись
    _other.cons.scr.blit(_other.cons.my_font.render(_other.cons.active_color, False,
    "black" if _other.cons.active_color != "black" else "white"), (400, 400))

    # Кнопка
    _other.objectss.button_prayer_10()

    pygame.display.update()

    for event in pygame.event.get():
        if _other.objectss.is_clicked_button_prayer_10: _other.objectss.effect_button_prayer_10()
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            exit()

    clock.tick(_other.cons.fps)