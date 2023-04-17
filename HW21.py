string_with_data_in_file = ""

with open("users.txt", "r") as file:
    string_with_data_in_file = file.read()

list_with_data_in_file = string_with_data_in_file.split("\n")  # разбил каждую новую строку файла по элементам списка
list_with_all_data = []

for i in list_with_data_in_file:
    sub_list_with_data_in_file = i.split(";")  # формирую подсписок что бы вытянуть отдельно имя, возраст и телефон
    dict_with_parced_data = {}

    if "" != sub_list_with_data_in_file[0]:  # проверяю есть ли имя в строке, так же помогает избежать index out of range ексепшина
        dict_with_parced_data["name"] = sub_list_with_data_in_file[0].strip()     # формирую словарь с именем

        if sub_list_with_data_in_file[1].isdigit():
            dict_with_parced_data["age"] = int(sub_list_with_data_in_file[1])  # формирую словарь с возрастом
        else:
            dict_with_parced_data["age"] = None

        if "" != sub_list_with_data_in_file[2]:
            stripped_phones = []
            for i in sub_list_with_data_in_file[2].split(","):  # формирую словарь со списком номеров и заодно убераю пробелы по бокам
                stripped_phones.append(i.strip())
            dict_with_parced_data["phones"] = stripped_phones
        else:
            dict_with_parced_data["phones"] = []
        list_with_all_data.append(dict_with_parced_data)

with open("users_out.json", "w") as file:
    file.write(str(list_with_all_data))

output_str = ""
for sub_dict in list_with_all_data:
    if sub_dict['age'] is None:
        output_str += f"{sub_dict['name']};{''}; {','.join(sub_dict['phones'])}\n"
    else:
        output_str += f"{sub_dict['name']}; {sub_dict['age']}; {','.join(sub_dict['phones'])}\n"

with open("users_out.txt", "w") as file:
    file.write(output_str)

