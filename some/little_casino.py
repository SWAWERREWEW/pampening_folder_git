from random import choice


money = 5_000_000
flow = 0
count_given_money = 0


while True:
    try:
        prises = [
            5_000, 1_000, 500,
            50, 25, 10, 5,
            2, 5, 2, 50, 10,
            5_000, 1_000, 500,
            50, 25, 10, 5,
            2, 5, 2, 50, 10,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
            -5_000, -1_000, -500,
            -50, -25, -10, -5,
            -1, -5, -1, -50, -10,
        ]


        answer = input("""Действие (нужно ввести число потом пробел и после пробела само значение)🚩
0 0 = Статус 💲🔍
1 x = крутить 💲💥
2 x = зароботок выбранного количество 💲➕
3 x = Перезапуск с выбранным количеством денег 💲♻
CTRL + C = выход ❌🚩
:""")
        events = (0, choice(prises)*int(answer[1:]) - int(answer[1:]), int(answer[1:]), (-1)*money + int(answer[1:]))
        num = int(answer[0])


        money += events[num]
        flow += money
       
        count_given_money += answer[:1].find("2")+1
       
        for _ in range(2): print()
        print(money, "💲💲💲", events[num], "📊")
        print("Получено", flow, "💲")
        print("Использовано заработков", count_given_money)
        for _ in range(2): print()
    except ValueError:
        print("Не удалось прочитать ответ❌🔍💬")

# Параллельное выполнение функций
from treading import Thread
def f1(): print(“loh”)
def f2():print(“genshin”)
potok1 = Thread(target=f1)
potok1.start()
potok2 = Thread(target=f2)
potok2.start()
