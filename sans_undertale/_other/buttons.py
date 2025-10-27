import pygame
pygame.init()

import _other.cons
import _other.obj

def button_start():
    text_start = _other.cons.my_font.render(" start ", False, "black", "yellow")
    
    text_start_rect = text_start.get_rect(topleft=(_other.cons.wid//2-100, _other.cons.hei//2))

    mouse = pygame.mouse.get_pos()

    keys = pygame.key.get_pressed()

    if text_start_rect.collidepoint(mouse):
        text_start = _other.cons.my_font.render(" start ", False, "black", "green")
    else:
        text_start = _other.cons.my_font.render(" start ", False, "black", "yellow")
    
    # Нажатие
    if text_start_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0] or keys[pygame.K_SPACE]:
        text_start = _other.cons.my_font.render(" start ", False, "black", "green")
        _other.cons.scr.blit(text_start, (_other.cons.wid//2-100, _other.cons.hei//2))
        _other.cons.scene = _other.cons.scenes["location"]
        _other.cons.message["win?"] = False
    
    _other.cons.scr.blit(text_start, (_other.cons.wid//2-100, _other.cons.hei//2))


def button_fight():

    my_font = pygame.font.Font("_other/fonts/BitcountGridSingle_Cursive-Black.ttf", 45)

    text_fight = my_font.render(" FIGHT ", False, "black", "yellow")

    coord_text_fight = (50,
                        _other.obj.field_w.y + _other.obj.field_w.hei + 100)

    text_fight_rect = text_fight.get_rect(topleft=(coord_text_fight))

    mouse = pygame.mouse.get_pos()

    keys = pygame.key.get_pressed()

    if text_fight_rect.collidepoint(mouse) or _other.cons.names_buttons[_other.cons.focus] == "fight":
        text_fight = my_font.render(" FIGHT ", False, "black", "green")
    else:
        text_fight = my_font.render(" FIGHT ", False, "black", "yellow")
    
    # При нажатии
    if (text_fight_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0] or
    (keys[pygame.K_z] and _other.cons.names_buttons[_other.cons.focus] == "fight")):
        text_fight = my_font.render(" FIGHT ", False, "black", "green")
        _other.cons.scr.blit(text_fight, coord_text_fight)
        _other.obj.sans.parem["hp"] -= 30
        _other.cons.scene = _other.cons.scenes["you_atak"]

    _other.cons.scr.blit(text_fight, coord_text_fight)


def button_act():
    my_font = pygame.font.Font("_other/fonts/BitcountGridSingle_Cursive-Black.ttf", 45)

    text_act = my_font.render("  ACT  ", False, "black", "yellow")

    coord_text_act = (250,
                        _other.obj.field_w.y + _other.obj.field_w.hei + 100)

    text_act_rect = text_act.get_rect(topleft=(coord_text_act))

    mouse = pygame.mouse.get_pos()

    keys = pygame.key.get_pressed()

    if text_act_rect.collidepoint(mouse) or _other.cons.names_buttons[_other.cons.focus] == "act":
        text_act = my_font.render("  ACT  ", False, "black", "green")
    else:
        text_act = my_font.render("  ACT  ", False, "black", "yellow")
    
    # При нажатии
    if (text_act_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0] or
        (keys[pygame.K_z] and _other.cons.names_buttons[_other.cons.focus] == "act")):
        text_act = my_font.render("  ACT  ", False, "black", "green")
        _other.cons.scr.blit(text_act, coord_text_act)
        _other.obj.soul.parem["hp"] += 5.5
        if _other.obj.soul.parem["hp"] > _other.obj.soul.parem["max_hp"]:
            _other.obj.soul.parem["hp"] = _other.obj.soul.parem["max_hp"]
        _other.cons.scene = _other.cons.scenes["you_act"]

    _other.cons.scr.blit(text_act, coord_text_act)


def button_items():
    my_font = pygame.font.Font("_other/fonts/BitcountGridSingle_Cursive-Black.ttf", 45)

    text_items = my_font.render(" ITEMS ", False, "black", "yellow")

    coord_text_items = (450,
                        _other.obj.field_w.y + _other.obj.field_w.hei + 100)

    text_items_rect = text_items.get_rect(topleft=(coord_text_items))

    mouse = pygame.mouse.get_pos()

    keys = pygame.key.get_pressed()

    if text_items_rect.collidepoint(mouse) or _other.cons.names_buttons[_other.cons.focus] == "items":
        text_items = my_font.render(" ITEMS ", False, "black", "green")
    else:
        text_items = my_font.render(" ITEMS ", False, "black", "yellow")
    
    # При нажатии
    if (text_items_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0] or
        (keys[pygame.K_z] and _other.cons.names_buttons[_other.cons.focus] == "items")):
        text_items = my_font.render(" ITEMS ", False, "black", "green")
        _other.cons.scr.blit(text_items, coord_text_items)
        _other.obj.soul.parem["hp"] += 45
        if _other.obj.soul.parem["hp"] > _other.obj.soul.parem["max_hp"]:
            _other.obj.soul.parem["hp"] = _other.obj.soul.parem["max_hp"]
        _other.cons.scene = _other.cons.scenes["you_eat"]

    _other.cons.scr.blit(text_items, coord_text_items)


def button_mercy():
    my_font = pygame.font.Font("_other/fonts/BitcountGridSingle_Cursive-Black.ttf", 45)

    text = my_font.render(" MERCY ", False, "black", "yellow")

    coord_text = (650,
                 _other.obj.field_w.y + _other.obj.field_w.hei + 100)

    text_rect = text.get_rect(topleft=(coord_text))

    mouse = pygame.mouse.get_pos()

    keys = pygame.key.get_pressed()

    if text_rect.collidepoint(mouse) or _other.cons.names_buttons[_other.cons.focus] == "mercy":
        text = my_font.render(" MERCY ", False, "black", "green")
    else:
        text = my_font.render(" MERCY ", False, "black", "yellow")
    
    # При нажатии
    if (text_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0] or
        (keys[pygame.K_z] and _other.cons.names_buttons[_other.cons.focus] == "mercy")):
        text = my_font.render(" MERCY ", False, "black", "green")
        _other.cons.scr.blit(text, coord_text)
        _other.cons.scene = _other.cons.scenes["..."]
        _other.cons.mercy_quit += 1

    _other.cons.scr.blit(text, coord_text)