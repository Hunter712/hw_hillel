lst = [11, 12, 13, 16, 17, 18, 19]
MIN_NUMBER = 14
MAX_NUMBER = 15

print(lst)

sum_of_numbers = 0
product_of_numbers = 1

for i in lst:
    if MIN_NUMBER < i <= MAX_NUMBER:
        sum_of_numbers += i
        product_of_numbers *= i

if sum_of_numbers != 0:
    print(f"sum = {sum_of_numbers} product = {product_of_numbers}")
else:
    print("sum = 0 product = 0")

