import pygame
pygame.init()

import _other.obj
import _other.cons

get_pressed_z = 0

def enemy_say(message, cont):
    global get_pressed_z

    _other.obj.recreate_field()
    _other.obj.soul.x = _other.obj.field_b.x + _other.obj.field_b.wid//2
    _other.obj.soul.y = _other.obj.field_b.y + _other.obj.field_b.hei//2

    _other.cons.scr.fill(pygame.Color("black"))

    _other.obj.draw_hp_soul()

    # Рисуем поле
    _other.cons.scr.blit(_other.obj.field_w.py_object, (_other.obj.field_w.x, _other.obj.field_w.y))
    _other.cons.scr.blit(_other.obj.field_b.py_object, (_other.obj.field_b.x, _other.obj.field_b.y))
    
    # Рисуем Санса
    _other.cons.scr.blit(_other.obj.sans.image, (_other.obj.sans.x, _other.obj.sans.y))

    _other.cons.scr.blit(_other.cons.my_font.render(message, False, "black", "white"), (_other.obj.sans.x + _other.obj.sans.wid + 10, _other.obj.sans.hei//2))

    _other.obj.draw_hp_sans()

    keys = pygame.key.get_pressed()

    mouse = pygame.mouse.get_pos()

    if keys[pygame.K_z] or (((_other.cons.scr).get_rect(topleft=(0, 0))).collidepoint(mouse) and pygame.mouse.get_pressed()[0]):
        get_pressed_z += 1
    
    if get_pressed_z == 20:
        get_pressed_z = 0
        _other.cons.scene = _other.cons.scenes[cont]