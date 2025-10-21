import pygame
pygame.init()

# Сценарии игры
scene1 = "menu"  # Меню игры начало
scene2 = "start"  # Игра началась
scene3 = "gameover"  # Игра закончилась
scene4 = "gamewin"  # Игра пройдена

# Статус игры.
game_status = scene1

# Ширина экрана
wid = 600

# Высота экрана
hei = 650

# Размер экрана для текста
size_title = 35

# Создание экрана
scr = pygame.display.set_mode((wid, hei))

# беги
run = True

# кадры в секунду
fps = 60

# Значение для синего квадрата
x_blue = wid // 2
y_blue = hei // 2
wid_blue = 25
hei_blue = 25
color_blue = "blue"
speed_blue = 0.15
parem_blue = {"hp": 100, "score": 0}

# Количество красных квадратов
count_red_squ = 10
damage_red = 2

# Количество жёлтых квадратов
count_yel_squ = 5
point_yellow = 10

# Шрифт
my_font = pygame.font.Font("_other_470/fonts/BitcountGridSingle_Cursive-Black.ttf", 30)

# Звуки
sounds = {"take_points": pygame.mixer.Sound("_other_470/sounds/take_points_sound.mp3"),
          "lose_hp": pygame.mixer.Sound("_other_470/sounds/lose_hp_sound.mp3"),
          "win": pygame.mixer.Sound("_other_470/sounds/win_sound.mp3")
          }

# Музыка
songs = {"menu": [pygame.mixer.Sound("_other_470/songs/menu_song.mp3"), (2*60 + 25 + 1) * fps],
         "gameplay": [pygame.mixer.Sound("_other_470/songs/gameplay_song.mp3"), (3*60 + 28 + 1) * fps],
         "gameover": [pygame.mixer.Sound("_other_470/songs/gameover_song.mp3"), (1*60 + 9 + 1) * fps],
         "off": [pygame.mixer.Sound("_other_470/songs/off.mp3"), fps]
         }

# Путь к активной музыке
song_play = songs["menu"]

# Название активной музыки
song_active = ""

# Время, которое прошло после начала музыки
song_time = 0