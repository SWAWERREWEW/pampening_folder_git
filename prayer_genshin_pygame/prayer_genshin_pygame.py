import pygame
import _other.cons
import _other.objectss
import _other.pictures.obj_pictures

pygame.init()

run = True

f = 0

clock = pygame.time.Clock()


while run:

    _other.cons.scr.fill(pygame.Color(_other.cons.active_color))



    # Надпись
    _other.cons.scr.blit(_other.cons.my_font.render(_other.cons.active_color, False,
    "black" if _other.cons.active_color != "black" else "white"), (400, 400))

    _other.cons.scr.blit(_other.pictures.obj_pictures.main_picture, (0, 0))

    # Кнопка
    _other.objectss.button_prayer_10()

    pygame.display.update()

    for event in pygame.event.get():
        if _other.cons.was_clicked:
            _other.cons.effect_button()

        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            exit()

    clock.tick(_other.cons.fps)
