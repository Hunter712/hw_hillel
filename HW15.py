lst = [-1, 0, 1, 2, 11, 12, 13, 16, 17, 18, 19]
MIN_NUMBER = -1
MAX_NUMBER = 11

sum_of_numbers = 0
product_of_numbers = 1
list_with_elements_from_range = []

for i in lst:
    if MIN_NUMBER <= i <= MAX_NUMBER:
        list_with_elements_from_range.append(i)

if len(list_with_elements_from_range) == 0:
    print(f"no elements in range: sum = {0} product = {0}")
else:
    for i in list_with_elements_from_range:
        sum_of_numbers += i
        product_of_numbers *= i
    print(f"sum = {sum_of_numbers} product = {product_of_numbers}")
