import sys

min_width = int(input("Enter minimal width:"))
max_width = int(input("Enter maximal width:"))

if min_width > max_width:
    print("minimal width more than maximal width")
    sys.exit()

if (max_width - min_width) % 2 != 0:
    print("Number not a multiple of 2")
    sys.exit()

width_calc = int((max_width - min_width)/2) + 1

for k in range(1, width_calc):                #формирую столбцы для первой половины кристалла
    if k == 1:
        if min_width != 1:
            line = (width_calc - k) * " " + min_width * "*"     #формирую первую строку кристалла с учетом минимальной ширины
        else:
            line = (width_calc - 1) * " " + min_width * "*"
    else:
        line = (width_calc - k) * " " + "*"             #формирую пустые символы в начале строки, в конце добавляю *, для формирования первой половины трехугольника

    if min_width != 1:
        for i in range(1, k):                #заполняю пробелами первую половину трехугольника
            line += " "
    else:
        for i in range(1, k - 1):                #заполняю пробелами первую половину трехугольника
            line += " "

    if min_width > 1:
        line += (min_width - 2) * " "        #заполняю пробелами средину кристалла
    else:
        line += min_width * " "

    if min_width != 1:
        for i in range(k, 1, -1):                #заполняю пробелами вторую половину трехугольника
            line += " "
    else:
        for i in range(k - 1, 1, -1):                #заполняю пробелами вторую половину трехугольника
            line += " "

    if k != 1:                          #если первая строка то не вывожу лишний *, если не первая то вывожу в конце строки * для формирования кристалла
        print(line + "*")
    else:
        print(line)

for k in range(width_calc, 0, -1):                #формирую столбцы для второй половины кристалла
    if k == 1:
        if min_width != 1:
            line = (width_calc - k) * " " + min_width * "*"          #формирую первую строку кристалла с учетом минимальной ширины
        else:
            line = (width_calc - 1) * " " + min_width * "*"
    else:
        line = (width_calc - k) * " " + "*"               #формирую пустые символы в начале строки, в конце добавляю *, для формирования второй половины трехугольника

    if min_width != 1:
        for i in range(k, 1, -1):                #заполняю пробелами первую половину трехугольника
            line += " "
    else:
        for i in range(k - 1, 1, -1):                #заполняю пробелами первую половину трехугольника
            line += " "

    if min_width > 1:
        line += (min_width - 2) * " "        #заполняю пробелами средину кристалла
    else:
        line += min_width * " "

    if min_width != 1:
        for i in range(1, k):                #заполняю пробелами вторую половину трехугольника
            line += " "
    else:
        for i in range(1, k - 1):                #заполняю пробелами вторую половину трехугольника
            line += " "

    if k != 1:                              #если первая строка то не вывожу лишний *, если не первая то вывожу в конце строки * для формирования кристалла
        print(line + "*")
    else:
        print(line)

