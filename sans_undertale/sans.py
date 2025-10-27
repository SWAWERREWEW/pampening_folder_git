import pygame
import _other.cons
import _other.obj
import _other.scenes.fight_act_items_mercy
import _other.scenes.menu
import _other.scenes.enemy_atak
import _other.scenes.enemy_atak2
import _other.scenes.enemy_atak3
import _other.scenes.enemy_atak4
import _other.scenes.location
import _other.scenes.enemy_say
import _other.scenes.message_in_tablo

pygame.init()

while _other.cons.run:
    # Тормозим время
    clock = pygame.time.Clock()
    keys = pygame.key.get_pressed()
    
    if _other.cons.scene == _other.cons.scenes["menu"]:
        _other.scenes.menu.menu()

    elif _other.cons.scene == _other.cons.scenes["location"]:
        _other.scenes.location.location()

    elif _other.cons.scene == _other.cons.scenes["fight_act_items_mercy"]: 
        _other.scenes.fight_act_items_mercy.fight_act_items_mercy()
        
        _other.obj.play_music("megalovania")
    
    elif _other.cons.scene == _other.cons.scenes["you_eat"]:
        if _other.obj.sans.parem["hp"] <= 10:
            _other.scenes.message_in_tablo.message_in_tablo(" You eat Legendary Hero ",
            "enemy_ataks", " Your HP +45", " Last hit ", color3="red")
        elif _other.obj.soul.parem["hp"] == _other.obj.soul.parem["max_hp"]:
            _other.scenes.message_in_tablo.message_in_tablo(" You eat Legendary Hero ", "enemy_ataks",
            " Your HP +45", " Your HP is full")
        else:
            _other.scenes.message_in_tablo.message_in_tablo(" You eat Legendary Hero ", "enemy_ataks",
            " Your HP +45")
    
    elif _other.cons.scene == _other.cons.scenes["you_kill"]:
        _other.scenes.enemy_say.enemy_say(" AAAAAAAAAAAA ", "enemy_death")
    
    elif _other.cons.scene == _other.cons.scenes["enemy_death"]:
        _other.scenes.message_in_tablo.message_in_tablo(" You kill Sans ", "menu", color="red",
        enemy_have=False)
    
    elif _other.cons.scene == _other.cons.scenes["you_act"]:
        _other.scenes.fight_act_items_mercy.fight_act_items_mercy("act")

    elif _other.cons.scene == _other.cons.scenes["you_atak"]:
        _other.scenes.enemy_say.enemy_say(" ou shet ", "enemy_ataks")
    
    elif _other.cons.scene == _other.cons.scenes["enemy_ataks"]:
        if _other.cons.number_atak == "atak":
            _other.scenes.enemy_atak.enemy_atak()
        elif _other.cons.number_atak == "atak2":
            _other.scenes.enemy_atak2.enemy_atak2()
        elif _other.cons.number_atak == "atak3":
            _other.scenes.enemy_atak3.enemy_atak3()
        elif _other.cons.number_atak == "atak4":
            _other.scenes.enemy_atak4.enemy_atak4()

        _other.cons.time_atak += 1

        _other.obj.play_music("megalovania")
    
    elif _other.cons.scene == _other.cons.scenes["..."]:
        _other.scenes.enemy_say.enemy_say("...", "enemy_ataks")
    
    elif _other.cons.scene == _other.cons.scenes["you_mercy_enemy"]:
        _other.scenes.enemy_say.enemy_say(" Okey ", "you_mercy_enemy2")
    
    elif _other.cons.scene == _other.cons.scenes["you_mercy_enemy2"]:
        _other.scenes.enemy_say.enemy_say(" Sorryanchik ", "menu")

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            _other.cons.run = False
            pygame.quit()
            exit()
        if keys[pygame.K_a] and _other.cons.scene == "fight_act_items_mercy":
            _other.cons.focus -= 1
            if _other.cons.focus < 0:
                _other.cons.focus = len(_other.cons.names_buttons) - 1
        if keys[pygame.K_d] and _other.cons.scene == "fight_act_items_mercy":
            _other.cons.focus += 1
            if _other.cons.focus >= len(_other.cons.names_buttons):
                _other.cons.focus = 0

    # Установка значения кадров в секунду
    clock.tick(_other.cons.fps)