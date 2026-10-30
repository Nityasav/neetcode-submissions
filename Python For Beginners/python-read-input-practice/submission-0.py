def add_two_numbers() -> int:
    number_string = input()
    string_list = number_string.split(",")
    y=0
    for x in string_list:
        y += int(x)
    return y 


# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
