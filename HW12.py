s = "aab qq c badcc a qqqqqaqqqqaa tpara ada"

list_s = s.split()          #формируем список из строки
title_str = ""
for i in list_s:
    if i.count("a") == 2:               #идем по списку и проверяем на количество символов "a" в каждом элементе списка
        title_str += i.title() + " "    #меняем для каждой подходящей строки первую букву на большую и формируем итоговую строку-заголовок

print(title_str)

