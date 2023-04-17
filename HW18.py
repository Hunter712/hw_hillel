testers_data = {
    1: {"Alex": ["write test design", "write test script", "review test script", "in office"]},
    2: {"Petro": ["write test script", "review test script", "not in office"]},
    3: {"Grisha": ["review test script", "not in office"]},
    4: {"Ivan": ["review test script", "in office"]},
    5: {"Goga": ["write test script", "in office"]},
    6: {"Zhora": ["write test script", "review test script", "in office"]},
}

list_with_testers_id = []
who_can_write_only_scripts = []
who_is_in_office_today = []
who_can_write_review_scripts_today = []

for x in testers_data:
    list_with_testers_id.append(x)

list_with_testers_id.sort()
print("All testers in a team " + str(list_with_testers_id))

for i in testers_data:
    for j in testers_data[i]:
        if "write test script" in testers_data[i][j] and "write test design" not in testers_data[i][j]:
            who_can_write_only_scripts.append(i)

who_can_write_only_scripts.sort()
print("Testers who can write only scripts in a team " + str(who_can_write_only_scripts))

for i in testers_data:
    for j in testers_data[i]:
        if "in office" in testers_data[i][j]:
            who_is_in_office_today.append(i)

who_is_in_office_today.sort()
print("Testers who is in office today " + str(who_is_in_office_today))

for i in testers_data:
    for j in testers_data[i]:
        if "write test script" in testers_data[i][j] and "review test script" in testers_data[i][j] and "in office" in testers_data[i][j]:
            who_can_write_review_scripts_today.append(i)

who_can_write_review_scripts_today.sort()
print("Testers who is in office today and can write and review scripts" + str(who_can_write_review_scripts_today))
