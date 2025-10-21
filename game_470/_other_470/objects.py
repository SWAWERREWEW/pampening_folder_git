import pygame
pygame.init()
from random import randint
import _other_470.const

# Инициализируем все модули pygame
pygame.init()


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


# Функции для движения объектов
def move_up(py_object):
    if _other_470.const.size_title <= (py_object.y - py_object.hei * py_object.speed):
        py_object.y -= py_object.hei * py_object.speed
def move_left(py_object):
    if 0 <= (py_object.x - py_object.wid * py_object.speed):
        py_object.x -= py_object.wid * py_object.speed
def move_down(py_object):
    if (py_object.y + py_object.hei * py_object.speed) <= (_other_470.const.hei - py_object.hei):
        py_object.y += py_object.hei * py_object.speed
def move_right(py_object):
    if (py_object.x + py_object.wid * py_object.speed) <= (_other_470.const.wid - py_object.wid):
        py_object.x += py_object.wid * py_object.speed


# Функция для создания списка случайных координат
def rdc(wid_p: int, hei_p: int) -> list:
    """Возвращает список из двух случайных координат в диапазоне от размеров текстового поля до размеров экрана
    минус размер объекта, для которого нужно подобрать случайные координаты"""
    return [randint(0, (_other_470.const.wid - wid_p)), randint(_other_470.const.size_title,
    (_other_470.const.hei - hei_p))]


# Сохранённые данные о синем квадрате
save_blue = {"x": _other_470.const.wid // 2, "y": _other_470.const.hei // 2, "parem": {"hp": 100, "score": 0}}

# Создание синего квадрата. В параметрах второе значение здоровья
blue_squ = Plr(_other_470.const.x_blue, _other_470.const.y_blue, _other_470.const.wid_blue, _other_470.const.hei_blue,
_other_470.const.color_blue, _other_470.const.speed_blue,
{"hp": _other_470.const.parem_blue["hp"], "score": _other_470.const.parem_blue["score"]})
# Разукрашивание квадратика в синий цвет
blue_squ.py_object.fill(blue_squ.color)


def move_blue_squ():
    # Получаем информацию о нажатых клавишах
    keys = pygame.key.get_pressed()

    # Движение синего квадратика при нажатии клавиш w a s d
    if keys[pygame.K_w]:
        move_up(blue_squ)
    if keys[pygame.K_a]:
        move_left(blue_squ)
    if keys[pygame.K_s]:
        move_down(blue_squ)
    if keys[pygame.K_d]:
        move_right(blue_squ)

# Список созданных красных квадратов
lil_red_squ = [Plr(rdc(25, 25)[0], rdc(25, 25)[1], 25, 25,
"red", 0.1, {"direction_x": "right", "direction_y": "down"}) for i_red
in range(_other_470.const.count_red_squ)]

# Сохранённые данные о красных квадратах
save_red = {"x": [rdc(25, 25)[0] for ii in range(_other_470.const.count_red_squ)],
"y": [rdc(25, 25)[1] for iii in range(_other_470.const.count_red_squ)],
"count": _other_470.const.count_red_squ,
"direction_x": [lil_red_squ[ii].parem["direction_x"] for ii in range(_other_470.const.count_red_squ)],
"direction_y": [lil_red_squ[ii].parem["direction_y"] for ii in range(_other_470.const.count_red_squ)]
}

# Разукрашивание всех красных квадратов
for squ_i in range(_other_470.const.count_red_squ):
    lil_red_squ[squ_i].py_object.fill(lil_red_squ[squ_i].color)

# Движение всех красных квадратов
def move_red_squ():
    # Самостоятельное движение каждого красного квадратика
    for ind in range(_other_470.const.count_red_squ):
        red_squ = lil_red_squ[ind]
        if red_squ.parem["direction_x"] == "right":
            # Если вектор движения в право движемся в право
            if (red_squ.x + red_squ.wid * red_squ.speed) <= (_other_470.const.wid - red_squ.wid):
                # Если не врезались в экран, движемся
                move_right(red_squ)  # Движемся
            else:  # Если врезались в экран, то меняем вектор движения на противоположный, а дальше аналогия
                red_squ.parem["direction_x"] = "left"
        if red_squ.parem["direction_x"] == "left":
            if 0 <= (red_squ.x - red_squ.wid * red_squ.speed):
                move_left(red_squ)
            else:
                red_squ.parem["direction_x"] = "right"
        if red_squ.parem["direction_y"] == "down":
            if (red_squ.y + red_squ.hei * red_squ.speed) <= (_other_470.const.hei - red_squ.hei):
                move_down(red_squ)
            else:
                red_squ.parem["direction_y"] = "up"
        if red_squ.parem["direction_y"] == "up":
            if _other_470.const.size_title <= (red_squ.y - red_squ.hei * red_squ.speed):
                move_up(red_squ)
            else:
                red_squ.parem["direction_y"] = "down"


# Создание жёлтых квадратов
lil_yel_squ = [Plr(rdc(25, 25)[0], rdc(25, 25)[1],
15, 15, "yellow", 0, {"give_score": 10})
for i_yellow in range(_other_470.const.count_yel_squ)]

save_yel = {"x": [rdc(25, 25)[0] for ii in range(_other_470.const.count_yel_squ)],
"y": [rdc(25, 25)[1] for ii in range(_other_470.const.count_yel_squ)],
"count": _other_470.const.count_yel_squ
}

# Разукрашивание жёлтых квадратов
for ind_yel in range(_other_470.const.count_yel_squ):
    lil_yel_squ[ind_yel].py_object.fill(lil_yel_squ[ind_yel].color)

# Создание пересечения синего и красного квадрата и поведение игры после этого
def collide_blue_and_red():
    # Получаем хитбоксы синего квадрата
    blue_squ_rect = blue_squ.py_object.get_rect(topleft=(blue_squ.x, blue_squ.y))

    # Создание списка хитбоксов красных квадратов
    lil_red_squ_rect = [lil_red_squ[i_rect].py_object.get_rect(topleft=(lil_red_squ[i_rect].x,
    lil_red_squ[i_rect].y)) for i_rect in range(_other_470.const.count_red_squ)]

    # Перебираем список красных квадратов и отслеживаем пересечение с синим квадратом
    for i in range(len(lil_red_squ_rect)):
        if blue_squ_rect.colliderect(lil_red_squ_rect[i]):
            # Отнимаем здоровье
            blue_squ.parem["hp"] -= _other_470.const.damage_red
            _other_470.const.sounds["lose_hp"].play()
            red = lil_red_squ[i]
            # Отталкивание синего квадратика
            # if lil_red_squ[i].parem["direction_x"] == "right" and ((blue_squ.x + blue_squ.speed) < const.wid):
            #     blue_squ.x += blue_squ.speed

            if ((blue_squ.x + blue_squ.wid // 2) <= (red.x + red.wid // 2)) and ((blue_squ.x - blue_squ.wid // 2) >= 0):
                blue_squ.x -= blue_squ.wid // 2

            if ((blue_squ.x + blue_squ.wid//2) > (red.x + red.wid // 2) and
            ((blue_squ.x + blue_squ.wid + blue_squ.wid) < _other_470.const.wid)):
                blue_squ.x += blue_squ.wid // 2

            if (((blue_squ.y + blue_squ.hei // 2) <= (red.y + red.hei // 2)) and
                    ((blue_squ.y - blue_squ.hei//2) >= _other_470.const.size_title)):
                blue_squ.y -= blue_squ.hei // 2

            if ((blue_squ.y + blue_squ.hei//2) > (red.y + red.hei // 2) and
            ((blue_squ.y + blue_squ.hei + blue_squ.hei//2) < _other_470.const.hei)):
                blue_squ.y += blue_squ.hei//2


# Создание пересечения синего и красного квадрата и поведение игры после этого
def collide_blue_and_yel():
    # Получаем хитбоксы синего квадрата
    blue_squ_rect = blue_squ.py_object.get_rect(topleft=(blue_squ.x, blue_squ.y))

    # Создание хитбоксов жёлтых квадратов
    lil_yel_squ_rect = [lil_yel_squ[i_yel_rect].py_object.get_rect(topleft=(lil_yel_squ[i_yel_rect].x,
    lil_yel_squ[i_yel_rect].y)) for i_yel_rect in range(_other_470.const.count_yel_squ)]

    # Перебираем список жёлтых квадратов и отслеживаем их пересечение с синим квадратом
    for i in range(len(lil_yel_squ_rect)):
        if blue_squ_rect.colliderect(lil_yel_squ_rect[i]):
            # Добавляем очки синему квадрату
            blue_squ.parem["score"] += _other_470.const.point_yellow

            _other_470.const.sounds["take_points"].play()

            # Пересоздаём тот жёлтый квадрат, с которым произошло пересечение
            lil_yel_squ[i] = Plr(rdc(25, 25)[0], rdc(25, 25)[1], 15, 15,
            "yellow", 0, {"give_score": 10})
            # Пересоздаём его хитбокс
            lil_yel_squ_rect[i] = lil_yel_squ[i].py_object.get_rect(topleft=(lil_yel_squ[i].x,
            lil_yel_squ[i].y))
            # И закрашиваем
            lil_yel_squ[i].py_object.fill(lil_yel_squ[i].color)


def hp_line(hp_start: int, hp_now: int, x: int, y: int) -> None:
    line = pygame.Surface((2 * hp_start, 30))
    line.fill(pygame.Color("red"))
    _other_470.const.scr.blit(line, (x, y))
    if hp_now >= 0:
        line = pygame.Surface((2 * hp_now, 30))
        line.fill(pygame.Color("green"))
        _other_470.const.scr.blit(line, (x, y))


def music_play(name):
    _other_470.const.song_time += 1
    if _other_470.const.song_time >= _other_470.const.songs[name][1]:
        _other_470.const.song_time = 0
        name_active = name
        name = "off"
        if _other_470.const.song_active != name:
            _other_470.const.song_active = name
            pygame.mixer.stop()
            _other_470.const.song_play = _other_470.const.songs[_other_470.const.song_active][0]
            _other_470.const.song_play.play()
            if _other_470.const.game_status == _other_470.const.scene4:
                _other_470.const.sounds["win"].play()
        
        name = name_active
        if _other_470.const.song_active != name:
            _other_470.const.song_active = name
            pygame.mixer.stop()
            _other_470.const.song_play = _other_470.const.songs[_other_470.const.song_active][0]
            _other_470.const.song_play.play()
            if _other_470.const.game_status == _other_470.const.scene4:
                _other_470.const.sounds["win"].play()


    if _other_470.const.song_active != name:
        _other_470.const.song_active = name
        pygame.mixer.stop()
        _other_470.const.song_play = _other_470.const.songs[_other_470.const.song_active][0]
        _other_470.const.song_play.play()
        if _other_470.const.game_status == _other_470.const.scene4:
            _other_470.const.sounds["win"].play()


def button_start(coord):
    # Собираем информацию о курсоре
    mouse = pygame.mouse.get_pos()

    # Создаём надпись Start
    text_start = _other_470.const.my_font.render(" Start ", False, "green", "blue")

    # Создаём хитбокс надписи Start
    text_start_rect = text_start.get_rect(topleft=coord)

    # При наведении курсора на Start меняем цвет
    if text_start_rect.collidepoint(mouse):
        text_start = _other_470.const.my_font.render(" Start ", False, "blue", "green")
    else:
        text_start = _other_470.const.my_font.render(' Start ', False, "green", "blue")

    # coord = (100, const.hei // 2 - 50)

    # Рисуем надпись Start
    _other_470.const.scr.blit(text_start, coord)

    # При наведении и нажатии курсора на Start
    if text_start_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
        # Меняем статус игры
        _other_470.const.game_status = _other_470.const.scene2

    # Собираем информацию о нажатых клавишах
    keys = pygame.key.get_pressed()

    # Если нажат пробел
    if keys[pygame.K_SPACE]:
        # Меняем цвет надписи
        text_start = _other_470.const.my_font.render(" Start ", False, "blue", "green")

        # Рисуем надпись Start
        _other_470.const.scr.blit(text_start, coord)

        # Меняем статус игры началась
        _other_470.const.game_status = _other_470.const.scene2


def button_load(coord):
    global blue_squ, lil_red_squ, lil_yel_squ
    # Создаём надпись загрузить
    text_load = _other_470.const.my_font.render(" load ", False, "black", "yellow")

    # coord_button_load = (100, const.hei // 2 + 50)

    # Создаём хитбокс для надписи загрузить
    text_load_rect = text_load.get_rect(topleft=coord)

    # Получаем информацию о нажатых клавишах
    keys = pygame.key.get_pressed()

    # Получаем информацию о курсоре
    mouse = pygame.mouse.get_pos()

    # Меняем цвет надписи загрузить при наведении
    if text_load_rect.collidepoint(mouse):
        text_load = _other_470.const.my_font.render(" load ", False, "black", "green")

    # При нажатии курсора или кнопка l на надпись загрузить
    if text_load_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0] or keys[pygame.K_l]:
        # Меняем цвет надписи загрузить
        text_load = _other_470.const.my_font.render(" load ", False, "black", "green")

        # Список созданных красных квадратов
        lil_red_squ = [Plr(save_red["x"][ii], save_red["y"][ii], 25, 25,
        "red", 0.1, {"direction_x": save_red["direction_x"][ii],
        "direction_y": save_red["direction_y"][ii]}) for ii in range(_other_470.const.count_red_squ)]

        # Разукрашивание всех красных квадратов
        for squ_i in range(_other_470.const.count_red_squ):
            lil_red_squ[squ_i].py_object.fill(lil_red_squ[squ_i].color)

        # Создание жёлтых квадратов
        lil_yel_squ = [Plr(save_yel["x"][i_yellow], save_yel['y'][i_yellow],
                           15, 15, "yellow", 0, {"give_score": 10})
                       for i_yellow in range(_other_470.const.count_yel_squ)]

        # Разукрашивание жёлтых квадратов
        for ind_yel in range(_other_470.const.count_yel_squ):
            lil_yel_squ[ind_yel].py_object.fill(lil_yel_squ[ind_yel].color)

        blue_squ = Plr(save_blue["x"], save_blue["y"], _other_470.const.wid_blue,
        _other_470.const.hei_blue, _other_470.const.color_blue,
        _other_470.const.speed_blue,{"hp": save_blue["parem"]["hp"], "score": save_blue["parem"]["score"]})
        blue_squ.py_object.fill(blue_squ.color)

        _other_470.const.game_status = _other_470.const.scene2

    # Рисуем надпись загрузить
    _other_470.const.scr.blit(text_load, coord)


def button_save(coord):
    global save_blue, save_red, save_yel
    # Получаем информацию о нажатых клавишах
    keys = pygame.key.get_pressed()

    # Получаем информацию о курсоре
    mouse = pygame.mouse.get_pos()

    # Создаём надпись сохранить
    text_save = _other_470.const.my_font.render(" save ", False, "black", "yellow")

    # coord_button_save = (300, const.hei // 2 + 50)

    # Создаём hitbox надписи сохранить
    text_save_rect = text_save.get_rect(topleft=coord)

    # При наведении меняем цвет надписи сохранить
    if text_save_rect.collidepoint(mouse):
        text_save = _other_470.const.my_font.render(" save ", False, "black", "green")

    # При нажатии на надпись сохранить или при нажатии кнопки s
    if text_save_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0] or keys[pygame.K_s]:
        save_blue = {"x": blue_squ.x, "y": blue_squ.y, "parem": {"hp": blue_squ.parem["hp"],
        "score": blue_squ.parem["score"]}}

        save_red = {"x": [lil_red_squ[ii].x for ii in range(_other_470.const.count_red_squ)],
        "y": [lil_red_squ[ii].y for ii in range(_other_470.const.count_red_squ)],
        "count": _other_470.const.count_red_squ,
        "direction_x": [lil_red_squ[ii].parem["direction_x"] for ii in range(_other_470.const.count_red_squ)],
        "direction_y": [lil_red_squ[ii].parem["direction_y"] for ii in range(_other_470.const.count_red_squ)]
        }
        save_yel = {"x": [lil_yel_squ[ii].x for ii in range(_other_470.const.count_yel_squ)],
        "y": [lil_yel_squ[ii].y for ii in range(_other_470.const.count_yel_squ)],
        "count": _other_470.const.count_yel_squ}

    # Рисуем надпись сохранить
    _other_470.const.scr.blit(text_save, coord)


def button_menu(coord):
    # Текст выхода в меню
    text_menu = _other_470.const.my_font.render(" Menu ", False, "black", "yellow")

    # coord_button_menu = (const.wid - 100, 0)

    # Создание хитбокса для текста выхода в меню
    text_menu_rect = text_menu.get_rect(topleft=coord)

    # Получаем информацию о курсоре
    mouse = pygame.mouse.get_pos()

    # При наведении курсора меняем цвет текста выхода в меню
    if text_menu_rect.collidepoint(mouse):
        text_menu = _other_470.const.my_font.render(" Menu ", False, "black", "green")

    # Рисуем надпись выхода в меню
    _other_470.const.scr.blit(text_menu, coord)

    # Получаем информацию о нажатых клавишах
    keys = pygame.key.get_pressed()

    # При нажатии на текст выхода в меню
    if text_menu_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0] or keys[pygame.K_m]:
        _other_470.const.game_status = _other_470.const.scene1


def button_restart(coord):
    global blue_squ, lil_red_squ, lil_yel_squ

    # Получаем информацию о курсоре
    mouse = pygame.mouse.get_pos()

    # Создаём надпись Restart
    text_restart = _other_470.const.my_font.render(" Restart ", False, "green", "blue")

    # coord_button_restart = (100, const.hei // 2)

    # Создаём хитбокс надписи Restart
    text_restart_rect = text_restart.get_rect(topleft=coord)

    # При наведении курсора на Restart меняем цвет
    if text_restart_rect.collidepoint(mouse):
        text_restart = _other_470.const.my_font.render(" Restart ", False, "blue", "green")
    else:
        text_restart = _other_470.const.my_font.render(' Restart ', False, "green", "blue")

    # Собираем информацию о нажатых клавишах
    keys = pygame.key.get_pressed()

    # При наведении и нажатии курсора на Restart или при нажатии на пробел
    if text_restart_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0] or keys[pygame.K_r]:
        # Возвращаем здоровье
        blue_squ.parem["hp"] = 100

        # Забираем накопленные и несохранённые очки
        blue_squ.parem["score"] = 0

        # Обновляем статус игры началась
        _other_470.const.game_status = _other_470.const.scene2

        # Пересоздаём синий квадрат
        blue_squ = Plr(_other_470.const.x_blue, _other_470.const.y_blue, _other_470.const.wid_blue,
        _other_470.const.hei_blue, _other_470.const.color_blue, _other_470.const.speed_blue,
        {"hp": _other_470.const.parem_blue["hp"], "score": _other_470.const.parem_blue["score"]})

        # Разукрашивание
        blue_squ.py_object.fill(blue_squ.color)

        # Пересоздаём список красных квадратов
        lil_red_squ = [Plr(rdc(25, 25)[0], rdc(25, 25)[1],
       25, 25, "red", 0.1,
       {"direction_x": "right", "direction_y": "down"}) for i
        in range(_other_470.const.count_red_squ)]

        # Снова разукрашиваем пересозданные красные квадраты
        for squ_i in range(_other_470.const.count_red_squ):
            lil_red_squ[squ_i].py_object.fill(lil_red_squ[squ_i].color)

        # Пересоздаём список жёлтых квадратов
        lil_yel_squ = [Plr(rdc(25, 25)[0], rdc(25, 25)[1],
       15, 15, "yellow", 0, {"give_score": 10})
        for i_yellow in range(_other_470.const.count_yel_squ)]

        # Разукрашивание жёлтых квадратов
        for ind_yel in range(_other_470.const.count_yel_squ):
            lil_yel_squ[ind_yel].py_object.fill(lil_yel_squ[ind_yel].color)

    # Рисуем надпись Restart
    _other_470.const.scr.blit(text_restart, coord)