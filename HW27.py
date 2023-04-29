def gen(m, n):
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            yield pow(j, i)


numbers = gen(3, 4)

for i in numbers:
    print(i)
