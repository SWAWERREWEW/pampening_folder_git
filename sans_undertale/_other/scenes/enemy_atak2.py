import pygame
pygame.init()

import _other.obj
import _other.cons

count_bones = 4

bones = [_other.obj.Plr_img(_other.obj.field_b.x, _other.obj.field_b.y, 150, 50, "_other/imgs/bone_horisontal.png", 2,
parem={"direction_y": "down"}) for b in range(count_bones)]

bones[0].x, bones[0].y = 0 + _other.obj.field_b.x, 0 + _other.obj.field_b.y
bones[1].x, bones[1].y = 150 + _other.obj.field_b.x, _other.obj.field_b.hei - 50 + _other.obj.field_b.y
bones[2].x, bones[2].y = 300 + _other.obj.field_b.x, 0 + _other.obj.field_b.y
bones[3].x, bones[3].y = 450 + _other.obj.field_b.x, _other.obj.field_b.hei - 50 + _other.obj.field_b.y

bones[1].parem["direction_y"] = "up"
bones[2].parem["direction_y"] = "down"

def enemy_atak2():
    _other.cons.scr.fill(pygame.Color("black"))

    _other.obj.draw_hp_soul()

    # Рисуем поле
    _other.cons.scr.blit(_other.obj.field_w.py_object, (_other.obj.field_w.x, _other.obj.field_w.y))
    _other.cons.scr.blit(_other.obj.field_b.py_object, (_other.obj.field_b.x, _other.obj.field_b.y))

    # Рисуем Санса
    _other.cons.scr.blit(_other.obj.sans.image, (_other.obj.sans.x, _other.obj.sans.y))

    _other.obj.draw_hp_sans()
    
    # Рисуем кости (препятствия)
    for b in range(len(bones)):
        _other.cons.scr.blit(bones[b].image, (bones[b].x, bones[b].y))
    
    # Движения для препятствий
    for bone in range(count_bones):
        _other.obj.move_bone_horisontal(bones[bone])

    # Отслеживание пересечения
    _other.obj.collide_bone_and_soul(bones)

    # Рисуем душу
    _other.cons.scr.blit(_other.obj.soul.image, (_other.obj.soul.x, _other.obj.soul.y))
    
    # Реализация движения души клавишами
    _other.obj.move(_other.obj.soul, _other.obj.field_b)

    # При проигрыше возвращаемся в блок меню
    if _other.obj.soul.parem["hp"] <= 0:
        _other.cons.time_atak = 0
        _other.cons.number_atak = "atak"
        _other.cons.scene = _other.cons.scenes["menu"]
    
    if _other.cons.time_atak >= 10 * _other.cons.fps:
        _other.cons.time_atak = 0
        _other.cons.number_atak = "atak3"
        _other.cons.scene = _other.cons.scenes["fight_act_items_mercy"]