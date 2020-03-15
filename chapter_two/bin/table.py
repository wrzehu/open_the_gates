def table_creator_from_dictionary(data_dict, title_dict={'Hash Value': ['Name', 'Datetime', 'Description']}):
    """
    Input: Dictionary to print and dictionary provides name of the columns
    Prints table base on pass dictionary
    """
    intermediate_dict = dict(title_dict, **data_dict)

    for key in intermediate_dict:
        top_down_of_cell(intermediate_dict)
        content_of_cell(intermediate_dict, key)
    top_down_of_cell(intermediate_dict)


def top_down_of_cell(some_dict):
    """
     Prints top or down of the cell based on dict size
    """
    cells_size_list = cell_size(some_dict)

    print('+', end='')
    table_len = cells_size_list[0] + 4
    print('-' * table_len + '+', end='')
    for i in range(1, 4):
        table_len = cells_size_list[i] + 4
        print('-' * table_len + '+', end='')
    print()


def content_of_cell(some_dict, key):
    """
    Prints the concent of the cell based on values from dictionary
    """
    cells_size_list = cell_size(some_dict)
    size_of_full_table = len(cells_size_list) - 1

    # Appends empty string to list for preventing not fully printed table
    while True:
        if size_of_full_table == len(some_dict[key]):
            break
        else:
            some_dict[key].append(' ')

    key_deference = cells_size_list[0] - len(key)
    i = 1
    print('|  ', end='')
    print(key + ' ' * key_deference + '  |  ', end='')
    for value in some_dict[key]:
        value_deference = cells_size_list[i] - len(value)
        print('{}'.format(value) + ' ' * value_deference + '  |  ', end='')
        i += 1
    print()


def cell_size(some_dict):
    """
    Base on length of keys and values of dictionary prepares size of the cells per column
    Returns size of biggest words in column to list.
    """
    cells_size_list = [0, 0, 0, 0]
    key_len = 0

    for keys, values in some_dict.items():
        i = 1
        if len(keys) > key_len:
            key_len = len(keys)
            cells_size_list[0] = key_len
        for value in values:
            value_len = cells_size_list[i]
            if len(value) > value_len:
                cells_size_list[i] = len(value)
                i += 1
    return cells_size_list
