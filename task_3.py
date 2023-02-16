""" 
3. Создайте программу для игры в ""Крестики-нолики"". 
"""

import random


def show(lis):
    print()
    print("      ", end='')
    for i in range(len(lis)):
        for j in range(0, 3):
            print(lis[i][j], end='  ')
        print("\n      ", end='')
    print()


def addendum_0(lis, st):
    for i in range(len(lis)):
        for j in range(len(lis)):
            if lis[i][j] == st:
                lis[i][j] = '0'
    return lis


def addendum_x(lis, st):
    for i in range(len(lis)):
        for j in range(len(lis)):
            if lis[i][j] == st:
                lis[i][j] = 'x'
    return lis


def v1(lis):
    fl = [True, True, True]
    num = 0
    for i in range(len(fl)):

        if fl[0]:
            for i in range(len(lis)):
                if lis[0][i] == 'x':
                    fl[0] = False

        if fl[1]:
            for i in range(len(lis)):
                if lis[1][i] == 'x':
                    fl[1] = False

        if fl[2]:
            for i in range(len(lis)):
                if lis[2][i] == 'x':
                    fl[2] = False

    if fl[0]:
        f = True
        for i in range(len(lis)):
            if f:
                if lis[0][i] != '0' and lis[0].count('0') == 0:
                    num = random.randint(1, 3)
                    f = False
                elif lis[0][i] != '0' and lis[0].count('0') > 0:
                    num = i+1
                    f = False
    elif fl[1]:
        f = True
        for i in range(len(lis)):
            if f:
                if lis[1][i] != '0' and lis[1].count('0') == 0:
                    num = random.randint(4, 6)
                    f = False
                elif lis[1][i] != '0' and lis[1].count('0') > 0:
                    num = i+4
                    f = False
    elif fl[2]:
        f = True
        for i in range(len(lis)):
            if f:
                if lis[2][i] != '0' and lis[2].count('0') == 0:
                    num = random.randint(7, 9)
                    f = False
                elif lis[2][i] != '0' and lis[2].count('0') > 0:
                    num = i+7
                    f = False
    return num


def v2(lis):
    fl = [True, True, True]
    num = 0
    for i in range(len(fl)):

        if fl[0]:
            for i in range(len(lis)):  # 0-0 1-0 2-0  0-1 1-1 2-1  0-2 1-2 2-2
                if lis[i][0] == 'x':
                    fl[0] = False

        if fl[1]:
            for i in range(len(lis)):
                if lis[i][1] == 'x':
                    fl[1] = False

        if fl[2]:
            for i in range(len(lis)):
                if lis[i][2] == 'x':
                    fl[2] = False

    ar_count = []
    for i in range(len(lis)):  # 0-0 0-1 0-2
        ar_count.append(lis[i][0])
    ar_count1 = []
    for i in range(len(lis)):  # 0-0 0-1 0-2
        ar_count1.append(lis[i][1])
    ar_count2 = []
    for i in range(len(lis)):  # 0-0 0-1 0-2
        ar_count2.append(lis[i][2])

    if fl[0]:
        f = True
        for i in range(len(lis)):  # 1-4-7
            if f:
                if lis[i][0] != '0' and ar_count.count('0') == 0:
                    num = ar_count[random.randint(0, 2)]
                    f = False
                elif lis[i][0] != '0' and ar_count.count('0') > 0:
                    num = ar_count[i]
                    f = False

    elif fl[1]:
        f = True
        for i in range(len(lis)):  # 2-5-8
            if f:
                if lis[i][1] != '0' and ar_count1.count('0') == 0:
                    num = ar_count1[random.randint(0, 2)]
                    f = False
                elif lis[i][1] != '0' and ar_count1.count('0') > 0:
                    num = ar_count1[i]
                    f = False
    elif fl[2]:
        f = True
        for i in range(len(lis)):  # 3-6-9
            if f:
                if lis[i][2] != '0' and ar_count2.count('0') == 0:
                    num = ar_count2[random.randint(0, 2)]
                    f = False
                elif lis[i][2] != '0' and ar_count2.count('0') > 0:
                    num = ar_count2[i]
                    f = False
    return num


def check(lis, st='x'):
    flag = False
    for liss in lis:
        if liss == [st, st, st]:
            flag = True
        elif liss == [st, st, st]:
            flag = True
        elif liss == [st, st, st]:
            flag = True

    for i in range(len(lis)):  # 0-0 1-0 2-0  0-1 1-1 2-1  0-2 1-2 2-2
        check = 0
        for j in range(len(lis)):
            if lis[j][i] == st:
                check += 1
            if check == 3:
                flag = True

    check = i = j = 0
    for i in range(len(lis)):  # 0-0 1-1 2-2
        if lis[i][i] == st:
            check += 1
        if check == 3:
            flag = True
    check = i = 0
    j = 3
    for i in range(len(lis)):  # 0-2 1-1 2-0
        j -= 1
        if lis[i][j] == st:
            check += 1
        if check == 3:
            flag = True

    return flag


print("\n------  ИГРА ------")
print("--Крестики-Нолики--")

lis = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

flag = flag_x = flag_0 = fl = False
show(lis)

while not flag:
    a = input("Введите номер, куда поставить 'x': ")
    b1 = ''
    b2 = ''
    lis = addendum_x(lis, a)[:]
    flag_x = check(lis, 'x')
    show(lis)

    print("Ход бота:")

    if not fl:
        x = random.randint(0, 1)
        fl = True

    if x == 0:
        b = str(v1(lis))
        if b == '0':
            b = str(v2(lis))
    elif x == 1:
        b = str(v2(lis))
        if b == '0':
            b = str(v1(lis))

    addendum_0(lis, b)
    flag_0 = check(lis, '0')

    if v1(lis) == 0 and v2(lis) == 0:
        flag = True

    show(lis)
    flag = flag_x or flag_0


if flag_x:
    print("Ура, Вы выйграли!!!\n")
elif flag_0:
    print("Бот выйграл. Увы, Вы проиграли!\n")
else:
    print("Победила дружба, ничья!\n")
