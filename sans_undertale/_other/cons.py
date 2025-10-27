import pygame

pygame.init()

wid = 1000
hei = 1000
scr = pygame.display.set_mode((wid, hei))
run = True
fps = 120

# Шрифт
my_font = pygame.font.Font("_other/fonts/BitcountGridSingle_Cursive-Black.ttf", 30)

scenes = {"menu": "menu",
        "fight_act_items_mercy": "fight_act_items_mercy",
        "enemy_ataks": "enemy_ataks",
        "location": "location",
        "you_mercy_enemy": "you_mercy_enemy",
        "you_mercy_enemy2": "you_mercy_enemy2",
        "...": "...",
        "you_eat": "you_eat",
        "you_act": "you_act",
        "you_atak": "you_atak",
        "you_kill": "you_kill",
        "enemy_death": "enemy_death"}

scene = scenes["menu"]

count_bones = 2

songs = {"megalovania": pygame.mixer.Sound("_other/songs/Megalovania.mp3"),
         "off": pygame.mixer.Sound("_other/songs/off.mp3")}
song_py = songs["megalovania"]
song_name = ""

time_atak = 0

message = {"win?": False, "hp_soul": ""}

time_song = 0

number_atak = "atak"

names_buttons = ["fight", "act", "items", "mercy"]
focus = 0

mercy_quit = 0