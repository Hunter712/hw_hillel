users = [{'name': 'Luarvik L. Luarvik', 'age': 17}, {'name': 'Olaf Andvarafors', 'age': 18},
         {'name': 'Brun Du Barnstokr', 'age': 19}]

list_with_users_with_age_more_than_18 = []


for dict_with_info in users:
    if dict_with_info["age"] >= 18:
        list_with_users_with_age_more_than_18.append(dict_with_info["name"])

print("Users with age >= 18 " + str(list_with_users_with_age_more_than_18))
