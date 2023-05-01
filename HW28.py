import re

split_sentences_pattern = r"([A-Z].*?\!)|([A-Z].*?\?)|([A-Z].*?\.)"  # разбил текст по строкам где строка начинается с большой буквы, заканчивается знаком . ? !
receive_first_word_in_sentence_pattern = r"^[A-Z]\w+"  # вытаскиваю первое слово в предложении

txt = """Happy New Year! Wish you good luck.
Please write me how are you doing? Goodbye...
"""

splitted_sentences = re.findall(split_sentences_pattern, txt)
result_string = ""

for in_list in splitted_sentences:
    for in_tuple in in_list:
        if in_tuple:
            first_word_in_sentence = re.findall(receive_first_word_in_sentence_pattern, in_tuple)
            if in_tuple == in_list[0]:
                result_string += first_word_in_sentence[0] + " "
            else:
                result_string += first_word_in_sentence[0].lower() + " "

result_string = result_string[:-1] + "."

print(result_string)
