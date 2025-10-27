import pygame
pygame.init()

import _other.cons
import _other.obj

def enemy_atak():

    _other.cons.scr.fill(pygame.Color("black"))

    _other.obj.draw_hp_soul()

    # Рисуем поле
    _other.cons.scr.blit(_other.obj.field_w.py_object, (_other.obj.field_w.x, _other.obj.field_w.y))
    _other.cons.scr.blit(_other.obj.field_b.py_object, (_other.obj.field_b.x, _other.obj.field_b.y))
    
    # Рисуем Санса
    _other.cons.scr.blit(_other.obj.sans.image, (_other.obj.sans.x, _other.obj.sans.y))

    _other.obj.draw_hp_sans()
    
    # Рисуем кости (препятствия)
    _other.cons.scr.blit(_other.obj.bones[0].image, (_other.obj.bones[0].x, _other.obj.bones[0].y))
    _other.cons.scr.blit(_other.obj.bones[1].image, (_other.obj.bones[1].x, _other.obj.bones[1].y))
    
    # Движения для препятствий
    for bone in range(_other.cons.count_bones):
        _other.obj.move_bone_vertical(_other.obj.bones[bone])
    
    # Рисуем душу
    _other.cons.scr.blit(_other.obj.soul.image, (_other.obj.soul.x, _other.obj.soul.y))
    
    # Реализация движения души клавишами
    _other.obj.move(_other.obj.soul, _other.obj.field_b)

    # Отслеживание пересечения
    _other.obj.collide_bone_and_soul(_other.obj.bones)

    # При проигрыше возвращаемся в блок меню
    if _other.obj.soul.parem["hp"] <= 0:
        _other.cons.time_atak = 0
        _other.cons.scene = _other.cons.scenes["menu"]
    
    if _other.cons.time_atak >= 10 * _other.cons.fps:
        _other.cons.time_atak = 0
        _other.cons.number_atak = "atak2"
        _other.cons.scene = _other.cons.scenes["fight_act_items_mercy"]