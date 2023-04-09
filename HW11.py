s = """Hello all.Here's pretty cold and hot. Choose yourself."""

list_s = s.split(".")  #формируем список разделяя по точке
del list_s[len(list_s) - 1]   #удаляем последний элемент списка, тк формируется пустой элемент в списке из за разделения по точке

list_s1 = []
indices_list = []
words_number_list = []

for value in list_s:  #пробегаемся по разделенному списку и разделяем еще раз по пробелу, формируя список двойной вложенности
    list_s1.append(value.split())


count_words = 0
for i in list_s1:
    for j in i:     #пробегаемся по листу и увеличиваем счетчик на 1, подсчитывая каждое слово в предложении
        count_words += 1
    words_number_list.append(count_words)   # добавляем подсчитанное количество слов в предложении в новый список
    count_words = 0
print(words_number_list)
