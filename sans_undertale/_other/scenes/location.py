import pygame
pygame.init()

import _other.cons
import _other.obj

wid_location, hei_location = 1000, 558

#
window_location = _other.obj.Plr_img(0, 250 + (hei_location//2 + 65) + 1, 1010, 215)

sans_in_location = None

path_image = "_other/imgs/sans_imgs/"

lil_left = [
        pygame.image.load(path_image + "plr_left_1.png").convert_alpha(),
        pygame.image.load(path_image + "plr_left_2.png").convert_alpha(),
        pygame.image.load(path_image + "plr_left_3.png").convert_alpha(),
        pygame.image.load(path_image + "plr_left_4.png").convert_alpha()
    ]

lil_up = [
        pygame.image.load(path_image + "plr_up_1.png").convert_alpha(),
        pygame.image.load(path_image + "plr_up_2.png").convert_alpha(),
        pygame.image.load(path_image + "plr_up_3.png").convert_alpha(),
        pygame.image.load(path_image + "plr_up_4.png").convert_alpha()
    ]

lil_right = [
        pygame.image.load(path_image + "plr_right_1.png").convert_alpha(),
        pygame.image.load(path_image + "plr_right_2.png").convert_alpha(),
        pygame.image.load(path_image + "plr_right_3.png").convert_alpha(),
        pygame.image.load(path_image + "plr_right_4.png").convert_alpha()
    ]

lil_down = [
        pygame.image.load(path_image + "plr_down_1.png").convert_alpha(),
        pygame.image.load(path_image + "plr_down_2.png").convert_alpha(),
        pygame.image.load(path_image + "plr_down_3.png").convert_alpha(),
        pygame.image.load(path_image + "plr_down_4.png").convert_alpha()
    ]

ind_loc = 0

locations = ["_other/imgs/last_coridor.png",
"_other/imgs/location_skirk.png",
"_other/imgs/location_forest.png",
"_other/imgs/location_neo_fnf.png"]

respawn = True
# Для проигрывания анимации передвижения Санса
c = 0
i = c//10

function_pass = False

def location():
    global locations
    global respawn
    global sans_in_location
    global c
    global i
    global lil_left
    global lil_up
    global lil_right
    global lil_down
    global ind_loc

    _other.cons.scr.fill(pygame.Color("black"))

    image_location = locations[ind_loc]
    
    if respawn:
        sans_in_location = _other.obj.Plr_img(46, 250 + (hei_location//2 + 65), 46, 56,
        "_other/imgs/sans_imgs/plr_down_1.png", 5,
        {"image_left": lil_left,
        "image_up": lil_up,
        "image_right": lil_right,
        "image_down": lil_down
        })
        respawn = False

    _other.cons.scr.blit(pygame.image.load(image_location), (0, 250))

    _other.cons.scr.blit(sans_in_location.image, (sans_in_location.x, sans_in_location.y))

    if c == 30:
        c = 0
    else:
        c += 1

    i = c//10

    _other.obj.move(cls=sans_in_location, window=window_location,
    image_left=sans_in_location.parem["image_left"],
    image_right=sans_in_location.parem["image_right"],
    image_up=sans_in_location.parem["image_up"],
    image_down=sans_in_location.parem["image_down"],
    ind=i
    )

    keys = pygame.key.get_pressed()

    _other.cons.scr.blit(_other.cons.my_font.render(" Press F to fight ", False, "yellow", "black"), (0, 0))

    if sans_in_location.x >= (window_location.wid - sans_in_location.wid - 10):
        sans_in_location.x = sans_in_location.wid
        ind_loc += 1
        if ind_loc >= len(locations):
            ind_loc = 0

    if sans_in_location.x <= 0:
        sans_in_location.x = window_location.wid - sans_in_location.wid - 20
        ind_loc -= 1
        if ind_loc < 0:
            ind_loc = len(locations)-1

    # if ind_loc == 3:
    #     pygame.time.Clock().tick(_other.cons.fps)

    if keys[pygame.K_f]:
        _other.cons.scene = _other.cons.scenes["fight_act_items_mercy"]
        respawn = True






















