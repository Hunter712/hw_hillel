cats = ["Murzik", "Barsik", "Pantera"]

print('{0}, {1}, {2}'.format(cats[0], cats[1], cats[2]))    # 1 way to output list elements

print('{first_elem}, {sec_elem}, {third_elem}'.format(
      first_elem=cats[0], sec_elem=cats[1], third_elem=cats[2]))    # 2 way to output list elements

print(', '.join(cats))  # 3 way to output list elements

print(*cats, sep=", ")  # 4 way to output list elements

output_str = ""
for i in range(len(cats)):          # 5 way to output list elements
    output_str += cats[i]
    if i != len(cats) - 1:  # created if condition, to avoid extra ", " at the end of the string
        output_str += ", "
print(output_str)

