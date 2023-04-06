n = int(input("Enter n:"))

for k in range(1, n + 1):                #формирую столбцы в количестве n
    line = (n - k) * "  "                 #формирую пустые символы в начале строки на убывание, для формирования трехугольника
    for i in range(1, k):                #формирую строку от 1 до n
        line += str(i) + " "

    for j in range(k, 0, -1):            #формирую строку от n до 1
        if j == 1:                       #в конце каждой строки убираю спейс
            line += str(j)
        else:
            line += str(j) + " "
    print(line)
