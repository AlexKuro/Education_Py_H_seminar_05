"""
Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 2021 конфета.
Играют два игрока делая ход друг после друга.
Первый ход определяется жеребьёвкой.
За один ход можно забрать не более чем 28 конфет.
Все конфеты оппонента достаются сделавшему последний ход.
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

a) Добавьте игру против бота

b) Подумайте как наделить бота ""интеллектом""
"""
import random


def player(rand):
    n = 0
    fl1 = True
    number = 0
    if rand == -1:
        n = 1
    elif rand == 1:
        n = 2
    while fl1:
        print(
            f"Сколько конфет возьмете игрок номер {n}, но неболее 28! -> ", end='')
        number = int(input())
        if number <= 28:
            fl1 = False
        else:
            print(
                f"Ввод неверный, не более 28. А Вы взяли {number}. Повторите ...")
    fl1 = True
    return number


def end_play(n, rand):
    pass


n = 100

print("\n ------  ИГРА ------")
print("----Игра с конфетами---\n")
print("Выбирите варианты игры:")
print("Я хочу играть с другом ------ нажмите цифру '1' ")
print("Я хочу играть с ботом ------- нажмите цифру '2' ")
print("Я хочу играть с умнум ботом - нажмите цифру '3' ")
num = int(input("Введите номер: "))
if num == 1 or num == 2 or num == 3:
    flag = True
    print(f"На столе конфет --> {n} !")
else:
    print("Ввод не верный!")
    flag = False

play1sum = play2sum = 0
play1 = play2 = rand = 0
fl = fl1 = fl2 = fl3 = fl4 = True

rand = [-1, 1]
pl = [0, 0, 0]
plsum = [0, 0, 0]
while flag:
    if num == 1:
        if fl:
            print("Начинаем...")
            rand = rand[random.randint(0, 1)]
            if rand == - 1:
                igr = 1
            else:
                igr = 2
            print(f"1..2..Жребий кинут. Ходит игрок под номером -> {igr}")
            fl = False
        while fl3:
            pl[rand] = player(rand)
            a = n - pl[rand]
            if a < 0:
                print(
                    f"Ой, тут столько нет конфет. На столе лежит {n} конфет!")
                print(f"Повторите ...")
            elif a >= 0:
                fl3 = False
        plsum[rand] += pl[rand]
        n -= pl[rand]
        rand *= -1
        fl3 = True
        print(f"На столе теперь {n} конфет!")

        if n == 0:
            if rand == 1:
                igr = 1
            else:
                igr = 2
            print(f"!!!Ура игрок под номером {igr} выйграл!!!")
            rand *= -1
            if rand == 1:
                igr = 1
            else:
                igr = 2
            print(
                f"Увы, игрок номер {igr} отдает конфеты в количестве {plsum[rand*-1]}!")
            flag = False

    elif num == 2:
        if fl:
            print("Начинаем...")
            rand = rand[random.randint(0, 1)]
            if rand == - 1:
                igr = '1'
            else:
                igr = 'бот'
            print(f"1..2..Жребий кинут. Ходит игрок -> {igr}")
            fl = False
        while fl3:
            if rand == -1:
                pl[rand] = player(rand)
                a = n - pl[rand]

                if a < 0:
                    print(
                        f"Ой, тут столько нет конфет. На столе лежит {n} конфет!")
                    print(f"Повторите ...")
                elif a >= 0:
                    fl3 = False
            elif rand == 1:
                pl[rand] = random.randint(1, 28)
                print(f"Сколько конфет возьмет бот -> {pl[rand]}")

                a = n - pl[rand]
                if a < 0:
                    pl[rand] = n
                    fl3 = False
                elif a >= 0:
                    fl3 = False

        plsum[rand] += pl[rand]
        n -= pl[rand]
        rand *= -1
        fl3 = True
        print(f"На столе теперь {n} конфет!")

        if n == 0:
            if rand == 1:
                igr = '1'
            else:
                igr = 'бот'
            print(f"!!!Ура игрок '{igr}' выйграл!!!")
            rand *= -1
            if rand == 1:
                igr = '1'
            else:
                igr = 'бот'
            print(
                f"Увы, игрок '{igr}' отдает конфеты в количестве {plsum[rand*-1]}!")
            flag = False

    elif num == 3:
        if fl:
            print("Начинаем...")
            rand = rand[random.randint(1, 1)]
            if rand == - 1:
                igr = '1'
            else:
                igr = 'бот'
            print(f"1..2..Жребий кинут. Ходит игрок -> {igr}")
            fl = False
        while fl3:
            if rand == -1:
                pl[rand] = player(rand)
                a = n - pl[rand]

                if a < 0:
                    print(
                        f"Ой, тут столько нет конфет. На столе лежит {n} конфет!")
                    print(f"Повторите ...")
                elif a >= 0:
                    fl3 = False
            elif rand == 1:
                c = random.randint(10, 28)
                while fl4:
                    if (n - c) % 2 == 1:
                        pl[rand] = c
                        fl4 = False
                    else:
                        c -= 1
                fl4 = True
                print(f"Сколько конфет возьмет бот -> {pl[rand]}")

                a = n - pl[rand]
                if a < 0:
                    pl[rand] = n
                    fl3 = False
                elif a >= 0:
                    fl3 = False

        plsum[rand] += pl[rand]
        n -= pl[rand]
        rand *= -1
        fl3 = True
        print(f"На столе теперь {n} конфет!")

        if n == 0:
            if rand == 1:
                igr = '1'
            else:
                igr = 'бот'
            print(f"!!!Ура игрок '{igr}' выйграл!!!")
            rand *= -1
            if rand == 1:
                igr = '1'
            else:
                igr = 'бот'
            print(
                f"Увы, игрок '{igr}' отдает конфеты в количестве {plsum[rand*-1]}!")
            flag = False