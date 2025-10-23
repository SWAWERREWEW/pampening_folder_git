import pygame
import _other.cons
import _other.objectss

pygame.init()

run = True

f = 0

clock = pygame.time.Clock()


while run:

    _other.cons.scr.fill(pygame.Color("green"))

    _other.cons.scr.blit(_other.cons.my_font.render(str(_other.cons.test_parem), False, "black"), (400, 400))

    _other.objectss.button_prayer_10()

    pygame.display.update()

    for event in pygame.event.get():
        if _other.objectss.is_clicked_button_prayer_10: _other.objectss.effect_button_prayer_10()
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            exit()

    clock.tick(_other.cons.fps)