rec_height = int(input("Enter height of rectangular:"))
rec_width = int(input("Enter width of rectangular:"))
rec_symbols = input("Enter symbol to build rectangular with:")

for i in range(rec_height):                     #формируем строки
    create_new_line = ""
    for j in range(rec_width):                  #формируем столбцы
        create_new_line += rec_symbols          #для каждой новой строки, создаем новую стрингу которую
    print(create_new_line)                      #заполняем в соответствии с указанной шириной прямоугольника и выводим после окончания цикла





