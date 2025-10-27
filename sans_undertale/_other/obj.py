import pygame
pygame.init()

import _other.cons

# Универсальный класс для создания объектов с картинкой и хранения их характеристик
class Plr_img:
    def __init__(self, x: int, y: int, wid_plr: int, hei_plr: int, image=None, speed=None, parem=None):
        self.x, self.y = x, y
        self.wid = wid_plr
        self.hei = hei_plr
        self.speed = speed
        self.parem = parem
        if image: self.image = pygame.image.load(image).convert_alpha()

# Универсальный класс для создания квадратов
class Plr:
    def __init__(self, x: int, y: int, wid_plr: int, hei_plr: int, color: str, speed: float, parem: dict):
        self.x, self.y = x, y  # первоначальные координаты
        self.wid = wid_plr  # Ширина объекта
        self.hei = hei_plr  # Высота объекта
        self.color = color  # Цвет объекта
        self.speed = speed  # Скорость движения объекта
        py_object = pygame.Surface((self.wid, self.hei))  # Создание самого объекта
        self.py_object = py_object  # Сохранение самого объекта
        self.parem = parem  # Дополнительные параметры объекта в обычном словаре


# Поле
field_w = Plr(x=150, y=500, wid_plr=610, hei_plr=310, color="white", speed=0, parem={})
field_w.py_object.fill(pygame.Color(field_w.color))
field_b = Plr(x=(field_w.x+5), y=(field_w.y+5), wid_plr=(field_w.wid-10), hei_plr=(field_w.hei-10), color="black", speed=0, parem={})
field_b.py_object.fill(pygame.Color(field_b.color))

# Душа
soul = Plr_img(x=500, y=530, wid_plr=25, hei_plr=25, image="_other/imgs/soul.png", speed=3, parem={"hp": 92, "max_hp": 92})

def recreate_soul():
    global soul
    soul = Plr_img(x=500, y=530, wid_plr=25, hei_plr=25, image="_other/imgs/soul.png", speed=3, parem={"hp": 92, "max_hp": 92})

# Кость
bones = [Plr_img(x=field_b.x, y=(field_b.hei + field_b.y - 150), wid_plr=50, hei_plr=150,
image="_other/imgs/bone_vertical.png", speed=4, parem={"direction_x": "right"}) for i
in range(_other.cons.count_bones)]

bones[1].x = field_b.x + field_b.wid - bones[1].wid
bones[1].y = field_b.y


def recreate_field():
    global field_b
    global field_w
    global bones

    # Поле
    field_w = Plr(x=150, y=500, wid_plr=610, hei_plr=310, color="white", speed=0, parem={})
    field_w.py_object.fill(pygame.Color(field_w.color))
    field_b = Plr(x=(field_w.x+5), y=(field_w.y+5), wid_plr=(field_w.wid-10), hei_plr=(field_w.hei-10), color="black", speed=0, parem={})
    field_b.py_object.fill(pygame.Color(field_b.color))

    # Кость
    bones = [Plr_img(x=field_b.x, y=(field_b.hei + field_b.y - 150), wid_plr=50, hei_plr=150, image="_other/imgs/bone_vertical.png",
    speed=4, parem={"direction_x": "right"}) for i in range(_other.cons.count_bones)]

    bones[1].x = field_b.x + field_b.wid - bones[1].wid
    bones[1].y = field_b.y

# Санс
sans = Plr_img(300, 0, 300, 350, "_other/imgs/sans_boss.png", 0, {"hp": 100})

def recreate_sans():
    global sans
    sans = Plr_img(300, 0, 300, 350, "_other/imgs/sans_boss.png", 0, {"hp": 100})

# Функции для движения объектов
def move_up(cls, window, image_up=None, ind=None):
    if image_up and ind:
        cls.image = cls.parem["image_up"][ind]
    elif image_up and ind == None:
        cls.image = cls.parem["image_up"]
    cls.y -= cls.speed
    if cls.y <= window.y:
        cls.y = window.y

def move_left(cls, window, image_left=None, ind=None):
    if image_left and ind:
        cls.image = cls.parem["image_left"][ind]
    elif image_left and ind == None:
        cls.image = cls.parem["image_left"]
    cls.x -= cls.speed
    if cls.x < window.x:
        cls.x = window.x

def move_down(cls, window, image_down=None, ind=None):
    if image_down and ind != None:
        cls.image = cls.parem["image_down"][ind]
    elif image_down and ind == None:
        cls.image = cls.parem["image_down"]
    cls.y += cls.speed
    if cls.y > (window.hei + window.y - cls.hei):
        cls.y = window.hei + window.y - cls.hei

def move_right(cls, window, image_right=None, ind=None):
    if image_right and ind:
        cls.image = cls.parem["image_right"][ind]
    elif image_right and ind == None:
        cls.image = cls.parem["image_right"]
    cls.x += cls.speed
    if cls.x > (window.wid + window.x - cls.hei):
        cls.x = window.wid + window.x - cls.hei

def move(cls, window, image_up=None, image_right=None, image_left=None, image_down=None, ind=None):
    # Получаем информацию о нажатых клавишах
    keys = pygame.key.get_pressed()

    # Движение синего квадратика при нажатии клавиш w a s d
    if keys[pygame.K_w]:
        move_up(cls, window, image_up, ind)
    
    if keys[pygame.K_a]:
        move_left(cls, window, image_left, ind)

    if keys[pygame.K_s]:
        move_down(cls, window, image_down, ind)

    if keys[pygame.K_d]:
        move_right(cls, window, image_right, ind)

def move_bone_vertical(plr):
    if plr.parem["direction_x"] == "right":
        if (plr.x + plr.wid) < (field_b.wid + field_b.x):
            plr.x += plr.speed
        else:
            plr.parem["direction_x"] = "left"

    if plr.parem["direction_x"] == "left":
        if plr.x >= field_b.x:
            plr.x -= plr.speed
        else:
            plr.parem["direction_x"] = "right"

def move_bone_horisontal(plr):
    if plr.parem["direction_y"] == "down":
        if (plr.y + plr.hei) < (field_b.hei + field_b.y):
            plr.y += plr.speed
        else:
            plr.parem["direction_y"] = "up"

    if plr.parem["direction_y"] == "up":
        if plr.y >= field_b.y:
            plr.y -= plr.speed
        else:
            plr.parem["direction_y"] = "down"


def collide_bone_and_soul(lil):
    
    soul_rect = soul.image.get_rect(topleft=(soul.x, soul.y))
    bones_rect = [lil[i].image.get_rect(topleft=(lil[i].x, lil[i].y)) for i in range(len(lil))]

    for borect in range(len(lil)):
        if soul_rect.colliderect(bones_rect[borect]):
            soul.parem["hp"] -= 0.5

def play_music(name: str) -> None:
    if _other.cons.song_name == "megalovania" or _other.cons.time_song == 0:
        _other.cons.time_song += 1
        _other.cons.song_name = "megalovania"
        
        if _other.cons.time_song >= ((2*60 + 40) * _other.cons.fps):
            _other.cons.song_name = "off"
            _other.cons.time_song = 0

    if _other.cons.song_name != name:
        _other.cons.song_name = name        
        pygame.mixer.stop()
        _other.cons.song_py = _other.cons.songs[_other.cons.song_name]
        _other.cons.song_py.play()

def hp_line(hp_start: int, hp_now: int, x: int, y: int, color: str) -> None:
    line = pygame.Surface((5 * hp_start, 40))
    line.fill(pygame.Color("red"))
    _other.cons.scr.blit(line, (x, y))
    line = pygame.Surface((5 * hp_now, 40))
    line.fill(pygame.Color(color))
    _other.cons.scr.blit(line, (x, y))

def draw_hp_sans():
    # Рисуем ХП Санса
    def hp_line(hp_start: int, hp_now: int, x: int, y: int, color: str) -> None:
        line = pygame.Surface((2 * hp_start, 40))
        line.fill(pygame.Color("red"))
        _other.cons.scr.blit(line, (x, y))
        if hp_now > 0:
            line = pygame.Surface((2 * hp_now, 40))
            line.fill(pygame.Color(color))
            _other.cons.scr.blit(line, (x, y))
    
    hp_line(100, _other.obj.sans.parem["hp"],
    _other.obj.sans.wid, _other.obj.sans.y + _other.obj.sans.hei, "green")

    _other.cons.scr.blit(_other.cons.my_font.render(str(_other.obj.sans.parem["hp"]) + "/100 HP", False, "black"),
    (_other.obj.sans.x, _other.obj.sans.y + _other.obj.sans.hei) )

def draw_hp_soul():
    # Рисуем ХП души
    _other.obj.hp_line(92, _other.obj.soul.parem["hp"],
    _other.obj.field_w.x + (_other.obj.field_w.hei//4),
    _other.obj.field_w.y + _other.obj.field_w.hei + 30, "yellow")
    
    _other.cons.scr.blit(_other.cons.my_font.render(str(_other.obj.soul.parem["hp"]) + "/92 HP", False, "black"),
    (_other.obj.field_w.x + (_other.obj.field_w.hei//4), _other.obj.field_w.y + _other.obj.field_w.hei + 30))

def quit():
    _other.cons.message["hp_soul"] = str(_other.obj.soul.parem["hp"])
    _other.obj.recreate_field()
    _other.obj.recreate_soul()
    _other.obj.recreate_sans()
    _other.cons.number_atak = "atak"
    _other.cons.mercy_quit = 0
    _other.cons.time = 0
    _other.obj.play_music("off")