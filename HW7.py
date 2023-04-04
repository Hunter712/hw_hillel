triangle_size = int(input("Enter size of triangle:"))

for i in range(triangle_size):                      #формирую строку
    fill_triangle = ""
    for j in range(triangle_size - i - 1):                  #заполняю строку пустым символом пока не дойду до побочной диагонали матрицы,
        fill_triangle += " "                                #-1 помогает избежать пустой строки когда i=0 на первой итерации
    for k in range(triangle_size - i - 1, triangle_size):   #заполняю строку * после достижения побочной диагонали матрицы
        fill_triangle += "*"
    print(fill_triangle)
