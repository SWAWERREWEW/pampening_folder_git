import pygame
pygame.init()

import _other.cons
import _other.obj
import _other.buttons
import _other.scenes.message_in_tablo

focus_line = 0
get_pressed = 0

def fight_act_items_mercy(lines=None):
    global focus_line
    global get_pressed

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
    if lines is None:
        if _other.obj.sans.parem["hp"] <= 10:
            _other.cons.scr.blit(_other.cons.my_font.render(" Last hit ", False, "red"), (_other.obj.field_b.x, _other.obj.field_b.y + 10))
        else:
            _other.cons.scr.blit(_other.cons.my_font.render(" Sans fight with you.", False, "white"), (_other.obj.field_b.x, _other.obj.field_b.y + 10))

        _other.buttons.button_fight()

        _other.buttons.button_items()

        _other.buttons.button_act()

        _other.buttons.button_mercy()

    elif lines == "act":

        buttons_lines = [" Quit ", " Do nothing ", " Nothing "]

        if focus_line >= len(buttons_lines):
            focus_line = 0

        for indl, draw_but in enumerate(buttons_lines):
            _other.cons.scr.blit(_other.cons.my_font.render(draw_but, False, "white"),
            (_other.obj.field_b.x, _other.obj.field_b.y + 10 + 30 * indl))
            if focus_line == indl:
                _other.cons.scr.blit(_other.cons.my_font.render(draw_but, False, "yellow"),
                (_other.obj.field_b.x, _other.obj.field_b.y + 10 + 30 * indl))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_s] or keys[pygame.K_d]:
            get_pressed += 1
            if get_pressed == 25:
                get_pressed = 0
                focus_line += 1
                if focus_line >= len(buttons_lines):
                    focus_line = 0

        if keys[pygame.K_w] or keys[pygame.K_a]:
            get_pressed += 1
            if get_pressed == 25:
                get_pressed = 0
                focus_line -= 1
                if focus_line < 0:
                    focus_line = len(buttons_lines) - 1

        if keys[pygame.K_z]:
            get_pressed += 1
            if get_pressed == 25:
                get_pressed = 0
                if buttons_lines[focus_line] == " Quit ":
                    _other.obj.quit()
                    _other.cons.scene = _other.cons.scenes["location"]
                if buttons_lines[focus_line] == " Do nothing ":
                    _other.cons.scene = _other.cons.scenes["enemy_ataks"]

        if keys[pygame.K_x]:
            _other.cons.scene = _other.cons.scenes["fight_act_items_mercy"]



    _other.obj.draw_hp_sans()

    if _other.obj.sans.parem["hp"] <= 0:
        _other.cons.scene = _other.cons.scenes["you_kill"]
        _other.cons.message["win?"] = True
    
    elif _other.cons.mercy_quit >= 4:
        _other.cons.scene = _other.cons.scenes["you_mercy_enemy"]
        _other.cons.message["win?"] = True

    