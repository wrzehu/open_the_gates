from chapter_two.bin.table import table_creator_from_dictionary
from chapter_two.bin.data_etl import DataDictStorage

data = DataDictStorage()


def introduction():
    print('Welcome to your task organizer')
    print('If you want add task type add')
    print('If you want remove task type rv')
    print('If you want update task type upd')
    print('If you want exit task type ex')
    print('If you want display tasks type all')
    print('If you want filter tasks type f')
    print()
    print()

    while True:
        ans = str(input('Choose what do you want to do(type here ->) : '))
        ans.lower()
        if ans in ['add', 'rv', 'upd', 'all', 'ex', 'f']:
            break
        else:
            print('Value provided by you was wrong choose one from add, rv, upd, all, ex, f')
            print()
    if ans == 'add':
        add()

    if ans == 'ex':
        exit()
    if ans == 'rv':
        remove()
    if ans == 'upd':
        update()
    if ans == 'all':
        all()
    if ans == 'f':
        select_filter()


def exit():
    pass


def add():
    print()
    list_of_data = [input('What\'s the name of the task : '), input('What\'s the datetime of the task : '),
                    input('What\'s the description of the task : ')]
    print('Hash Value of this task is ' + str(data.get_has_value()))
    data.add_data(list_of_data)
    next_step()


def remove():
    print()
    while True:
        try:
            hash_value = input('Provide hash value of task you want to remove : ')
            hash_value = int(hash_value)
            break
        except ValueError:
            print()
            print('You have to pass a number(1,2.,3 ,..)')

    data.delete_data(hash_value)
    print('Task number {} was successfully removed from task list '.format(hash_value))
    next_step()


def update():
    print()
    while True:
        try:
            hash_value = input('Pass hash value of task you want to update : ')
            hash_value = int(hash_value)
            break
        except ValueError:
            print()
            print('You have to pass a number(1,2.,3 ,..)')

    print()
    print('If you don\' want to update this value just press enter')
    list_of_changes = [str(input('Name to update : ')), str(input('Datetime to update : ')),
                       str(input('Description to update : '))]
    print()
    data.update_data(hash_value, list_of_changes)
    print('You successfully updated task number {}'.format(hash_value))
    next_step()


def all():
    data_dict = data.get_all()
    dict_with_string_keys = {str(k): data_dict[k] for k in data_dict}
    table_creator_from_dictionary(dict_with_string_keys)
    next_step()


def select_filter():
    print()
    print('If you don\' want to filter by this value just press enter')
    name = str(input('Filter by name : '))
    date = str(input('Filter by datetime : '))
    desc = str(input('Description to update : '))
    name_list = data.filter_per_name(name)
    date_list = data.filter_per_datetime(date)
    desc_list = data.filter_per_description(desc)
    ans = 0
    keys = []
    if len(name_list):
        ans += 1
    if len(date_list):
        ans += 1
    if len(desc_list):
        ans += 1

    if ans == 1:
        keys = name_list + date_list + desc_list
    else:
        keys = filter_helper_and(name_list, date_list, desc_list)

    data_dict = data.get_filtered_dict(keys)
    table_creator_from_dictionary(data_dict)
    next_step()



def filter_helper_and(l1, l2, l3):
    """
    Provides and condition
    """
    ans = set()
    for l in l1:
        if l in l2:
            ans.add(l)
    for l in l1:
        if l in l3:
            ans.add(l)
    for l in l2:
        if l in l3:
            ans.add(l)
    return list(ans)


def next_step():
    print()
    while True:
        ans = str(input('Choose your next step(type here ->) : '))
        ans.lower()
        if ans in ['add', 'rv', 'upd', 'all', 'ex', 'f']:
            break
        else:
            print('Value provided by you was wrong choose one from add, rv, upd, all, ex, f')
            print()
    if ans == 'add':
        add()

    if ans == 'ex':
        exit()
    if ans == 'rv':
        remove()
    if ans == 'upd':
        update()
    if ans == 'all':
        all()
    if ans == 'f':
        select_filter()


