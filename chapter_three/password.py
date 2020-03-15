def ascending(number):
    x = str(number)
    z = 1
    for i in range(len(x) - 1):
        if x[i + 1] >= x[i]:
            z += 1
    if z == len(x):
        return True
    else:
        return False


def double_adjacent_digit_finder(element):
    if element[0] == element[1] and element[3] == element[4] and element[1] != element[2]:
        return True
    if element[1] == element[2] and element[4] == element[5] and element[3] != element[4]:
        return True
    if element[0] != element[1] and element[2] == element[3] and element[4] == element[5]:
        return True
    if element[0] == element[1] and element[2] == element[3] and element[4] != element[5]:
        return True
    if element[1] == element[2] and element[3] == element[4] and element[0] != element[5]:
        return True


def rv_four_digits_from_end(ele):
    if ele[0] != ele[1] and ele[2] == ele[3] and ele[4] == ele[5] and ele[2] == ele[5]:
        return True
    elif ele[5] != ele[4] and ele[3] == ele[2] and ele[1] == ele[0] and ele[3] == ele[0]:
        return True
    elif ele[1] == ele[2] and ele[3] == ele[4] and ele[1] == ele[4]:
        return True


def find_password():
    start = 372 ** 2
    end = (809 ** 2) + 1
    range_of_number = range(start, end)
    # Numbers going up
    list_of_ascending_numbers = list(filter(ascending, range_of_number))

    inter_list = [str(x) for x in list_of_ascending_numbers]
    double_adjacent_digit_list = list(filter(double_adjacent_digit_finder, inter_list))

    regular_set = set(double_adjacent_digit_list)
    no_double_list = list(regular_set)
    no_double_list.sort()
    four_digits_to_remove_list = list(filter(rv_four_digits_from_end, no_double_list))
    list_free_from_bad_four_digits = [x for x in no_double_list if x not in four_digits_to_remove_list]
    return list_free_from_bad_four_digits


ans = len(find_password())
print()
print('Holly guacamole I have {} combinations to check '.format(ans))
print()

