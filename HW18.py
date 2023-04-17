testers_data = {
    1: {"in office": ["write test design", "write test script", "review test script"]},
    2: {"not in office": ["write test script", "review test script"]},
    3: {"not in office": ["review test script"]},
    4: {"in office": ["review test script"]},
    5: {"in office": ["write test script"]},
    6: {"in office": ["write test script", "review test script"]},
}

who_can_write_only_scripts = []
who_is_in_office_today = []
who_can_write_review_scripts_today = []

list_with_testers_id = sorted(list(testers_data.keys()))
print("All testers in a team " + str(list_with_testers_id))

for user_id, person_data in testers_data.items():
    for list_with_skills in person_data.values():
        if "write test script" in list_with_skills and "write test design" not in list_with_skills:
            who_can_write_only_scripts.append(user_id)

who_can_write_only_scripts.sort()
print("Testers who can write only scripts in a team " + str(who_can_write_only_scripts))

for user_id, person_data in testers_data.items():
    for list_with_skills in person_data.keys():
        if "in office" == list_with_skills:
            who_is_in_office_today.append(user_id)

who_is_in_office_today.sort()
print("Testers who is in office today " + str(who_is_in_office_today))

for user_id, person_data in testers_data.items():
    for is_here, list_with_skills in person_data.items():
        if "write test script" in list_with_skills and "review test script" in list_with_skills and "in office" == is_here:
            who_can_write_review_scripts_today.append(user_id)

who_can_write_review_scripts_today.sort()
print("Testers who is in office today and can write and review scripts" + str(who_can_write_review_scripts_today))
