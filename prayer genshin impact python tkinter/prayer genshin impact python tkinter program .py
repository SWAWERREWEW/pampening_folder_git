from tkinter import *
from tkinter import ttk
from random import shuffle

root = Tk()
root.geometry("1000x600+300+100")
root.title("praier genshin impact")

window = ttk.Label(root)
window.grid()

imageWindow = PhotoImage(file="main window genshin impact .png")
imageWindow10_1 = PhotoImage(file="genshin impact 10 1 .png")
imageWindow10_2 = PhotoImage(file="genshin impact 10 2 .png")
imageWindow10_3 = PhotoImage(file="genshin impact 10 3 .png")
imageWindow10_4 = PhotoImage(file="genshin impact 10 4 .png")

imageWindow1_1 = PhotoImage(file="genshin impact 1 1 .png")
imageWindow1_2 = PhotoImage(file="genshin impact 1 2 .png")
imageWindow1_3 = PhotoImage(file="genshin impact 1 3 .png")
imageWindow1_4 = PhotoImage(file="genshin impact 1 4 .png")
imageWindow1_5 = PhotoImage(file="genshin impact 1 5 .png")
imageWindow1_6 = PhotoImage(file="genshin impact 1 6 .png")
imageWindow1_7 = PhotoImage(file="genshin impact 1 7 .png")
imageWindow1_8 = PhotoImage(file="genshin impact 1 8 .png")
imageWindow1_9 = PhotoImage(file="genshin impact 1 9 .png")
imageWindow1_10 = PhotoImage(file="genshin impact 1 10 .png")
imageWindow1_11 = PhotoImage(file="genshin impact 1 11 .png")

window["image"] = imageWindow




def genshin10(*args):
    random_genshin = [1, 2, 3, 4]
    shuffle(random_genshin)
    if off_or_on == 0:
        if random_genshin[0] == 1:
            window["image"] = imageWindow10_1
            button_genshin_1["state"] = "disabled"
            button_genshin_10["state"] = "disabled"
        elif random_genshin[0] == 2:
            window["image"] = imageWindow10_2
            button_genshin_1["state"] = "disabled"
            button_genshin_10["state"] = "disabled"
        elif random_genshin[0] == 3:
            window["image"] = imageWindow10_3
            button_genshin_1["state"] = "disabled"
            button_genshin_10["state"] = "disabled"
        elif random_genshin[0] == 4:
            window["image"] = imageWindow10_4
            button_genshin_1["state"] = "disabled"
            button_genshin_10["state"] = "disabled"
        else:
            print("...")
    elif off_or_on == 1:
        if random_genshin[0] == 1:
            window["image"] = imageWindow10_1
        elif random_genshin[0] == 2:
            window["image"] = imageWindow10_2
        elif random_genshin[0] == 3:
            window["image"] = imageWindow10_3
        elif random_genshin[0] == 4:
            window["image"] = imageWindow10_4
        else:
            print("...")
    # print(str(random_genshin[0]) + "num item from 10")


def genshin1(*args):
    random_genshin = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    shuffle(random_genshin)
    if off_or_on == 0:
        if random_genshin[0] == 1:
            window["image"] = imageWindow1_1
            button_genshin_1["state"] = "disabled"
            button_genshin_10["state"] = "disabled"
            # print("выпала Фишль - ")
        elif random_genshin[0] == 2:
            window["image"] = imageWindow1_2
            button_genshin_1["state"] = "disabled"
            button_genshin_10["state"] = "disabled"
        elif random_genshin[0] == 3:
            window["image"] = imageWindow1_3
            button_genshin_1["state"] = "disabled"
            button_genshin_10["state"] = "disabled"
        elif random_genshin[0] == 4:
            window["image"] = imageWindow1_4
            button_genshin_1["state"] = "disabled"
            button_genshin_10["state"] = "disabled"
        elif random_genshin[0] == 5:
            window["image"] = imageWindow1_5
            button_genshin_1["state"] = "disabled"
            button_genshin_10["state"] = "disabled"
        elif random_genshin[0] == 6:
            window["image"] = imageWindow1_6
            button_genshin_1["state"] = "disabled"
            button_genshin_10["state"] = "disabled"
        elif random_genshin[0] == 7:
            window["image"] = imageWindow1_7
            button_genshin_1["state"] = "disabled"
            button_genshin_10["state"] = "disabled"
        elif random_genshin[0] == 8:
            window["image"] = imageWindow1_8
            button_genshin_1["state"] = "disabled"
            button_genshin_10["state"] = "disabled"
        elif random_genshin[0] == 9:
            window["image"] = imageWindow1_9
            button_genshin_1["state"] = "disabled"
            button_genshin_10["state"] = "disabled"
        elif random_genshin[0] == 10:
            window["image"] = imageWindow1_10
            button_genshin_1["state"] = "disabled"
            button_genshin_10["state"] = "disabled"
        elif random_genshin[0] == 11:
            window["image"] = imageWindow1_11
            button_genshin_1["state"] = "disabled"
            button_genshin_10["state"] = "disabled"
        else:
            print("...")
    elif off_or_on == 1:
        if random_genshin[0] == 1:
            window["image"] = imageWindow1_1
            # print("выпала Фишль - ")
        elif random_genshin[0] == 2:
            window["image"] = imageWindow1_2
        elif random_genshin[0] == 3:
            window["image"] = imageWindow1_3
        elif random_genshin[0] == 4:
            window["image"] = imageWindow1_4
        elif random_genshin[0] == 5:
            window["image"] = imageWindow1_5
        elif random_genshin[0] == 6:
            window["image"] = imageWindow1_6
        elif random_genshin[0] == 7:
            window["image"] = imageWindow1_7
        elif random_genshin[0] == 8:
            window["image"] = imageWindow1_8
        elif random_genshin[0] == 9:
            window["image"] = imageWindow1_9
        elif random_genshin[0] == 10:
            window["image"] = imageWindow1_10
        elif random_genshin[0] == 11:
            window["image"] = imageWindow1_11
        else:
            print("...")
    # print(str(random_genshin[0]) + "num item from 1")


def ok_command(*args):
    window["image"] = imageWindow
    button_genshin_10["state"] = "!disabled"
    button_genshin_1["state"] = "!disabled"




button_genshin_10 = ttk.Button(root, text="""  Помолиться 10 раз  
                x10""", command=genshin10)
button_genshin_10.place(x=825, y=510)



button_genshin_1 = ttk.Button(root, text="""  Помолиться 1 раз  
                x1""", command=genshin1)
button_genshin_1.place(x=630, y=510)


button_ok = ttk.Button(root, text="ok", command=ok_command)
button_ok.place(x=0, y=570)

off_or_on = 0


def expet_command():
    global off_or_on
    if off_or_on == 0:
        off_or_on = 1
    elif off_or_on == 1:
        off_or_on = 0
    """
    переключает режим вечных молитв без остановки
    если не желается каждый раз нажимать на ок
    если режим выключен то кнопку можно
    нажать только один раз и чтоб снова можно
    было нажать нужно нажать кнопку ок
    :return: 0 или 1
    0 - режим выключен
    1 - режим включен
    """


my_items = []

button_expet = ttk.Button(root, text="  expet  ", command=expet_command)
button_expet.place(x=100, y=570)

root.mainloop()