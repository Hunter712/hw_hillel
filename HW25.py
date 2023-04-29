def call_counter(file_name):
    def read_number():
        with open(file_name, "r") as file:
            call_number = file.read()
            if call_number == "":
                return 0
            else:
                return int(call_number)

    def write_number(call_number):
        with open(file_name, "w") as file:
            file.write(str(call_number))

    def inner(function):
        def wrapper(a, b):
            call_add_number = read_number()
            function(a, b)
            call_add_number += 1
            result = f"Function 'add' was called {call_add_number} times"
            write_number(call_add_number)
            return result
        return wrapper

    return inner


@call_counter('data.txt')
def add(a, b):
    return a + b


print(add(4, 6))
print(add(4, 6))
print(add(4, 6))
