palindrome = str(input("Enter palindrome:"))

palindrome = palindrome.lower()
palindrome = palindrome.strip()
str_lenght = len(palindrome)

if palindrome[int(str_lenght/2)::-1] in palindrome:         # делюстроку на пополам, срезом вырезаю вторую половину
    print(True)                                           # строки и сразу сортирую ее наоборот, потом с помощью оператора in делаю поиск по строке, если полиндром то мой
else:                                                       # срез влюбом случае будет присутствовать в начале первой половины строки
    print(False)

palindrome_reversed_copy = "".join(reversed(palindrome))    #выполняем обратную сортировку всей строки
if palindrome_reversed_copy == palindrome:                  #сравниваем оригинальную строку с отсортированной
    print(True)
else:
    print(False)
