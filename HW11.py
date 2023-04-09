s = "Hello all. Here's pretty cold and hot. Choose yourself. asd asd asd."

list_s = s.split()          #формируем список из строки
indices_list = []
words_number_list = []

for index, value in enumerate(list_s):      #идем по списку, проверяем есть ли в слове точка, фиксируем индекс слова в списке и добавляем в новый список
    if "." in value:
        indices_list.append(index)

count_words = 0
for index, value in enumerate(list_s):     #пробегаемся по оригинальной строке
    if index in indices_list:              #проверяем совпадает ли индекс оригинальной строки с индексом с точкой
        count_words += 1                   #увеличиваю еще раз на 1 что бы счетчик учитывал слово с точкой
        words_number_list.append(count_words)   #добавляем подсчитанное количество слов в предложении в новый список
        count_words = 0                     #обнуляем счетчик что бы переиспользовать для подсчета остальных слов в предложении
    else:
        count_words += 1                   #увеличиваем счетчик на 1 если мы еще не дошли до индекса с точкой
print(words_number_list)

