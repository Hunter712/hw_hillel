country = ["USA", "Germany", "Canada"]
capital = ["Washington", "Berlin", "Ottawa"]
country_and_capital = {}

if len(country) == len(capital):    # check if country and capital lists have the same size
    for i in range(len(country)):
        country_and_capital[country[i]] = capital[i]    # filled the dict, used for cycle because lists can resize in the future
else:
    print("country and capital lists should have the same size")


for x, y in country_and_capital.items():    # output dict keys and values
    print(x, y, sep=": ")




