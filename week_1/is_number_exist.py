input = [3, 5, 6, 1, 2, 4]


def is_number_exist(number, array):
    for element in array:
        if number == element:
            return True # N * 1 = N만큼

    return False

    return True


result = is_number_exist(3, input)
print(result)