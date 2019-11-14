""" Common module
implement commonly used functions here
"""

import random
import ui
import string
import data_manager

# FUNCTIONS TO CREATE ID
# variables for generating random id
numbers = '0123456789'
letters = 'abcdefghijklmnoprstuwxyz'
sign = ("#&")
id_index = 0


# creates id
def create_id():
    elem_id1 = ''.join(random.choice(letters))
    elem_id2 = ''.join(random.choice(letters)).upper()
    elem_id3 = ''.join(random.sample(numbers, 2))
    elem_id4 = ''.join(random.choice(letters)).upper()
    elem_id5 = ''.join(random.choice(letters))
    id = elem_id1 + elem_id2 + elem_id3 + elem_id4 + elem_id5 + sign
    return id

def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation:
         - at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letter
         - it must be unique in the table (first value in every row is the id)

    Args:
        table (list): Data table to work on. First columns containing the keys.

    Returns:
        string: Random and unique string
    """

    generated_id = ''
    id_table = [line[id_index] for line in table]
    generated_id = create_id()
    if id in id_table:
        generate_random(table)
    else:
        return generated_id


# OTHER HELPING FUNCTIONS:


# takes input (line number) and finds ID of line number
def convert_input_to_id(table, line_number):
    """Function takes number of line provided by user
    and returns unique id of item in this line.
    Returns id as string"""
    list_of_id = [line[id_index] for line in table]
    for i, id in enumerate(list_of_id, 1):
        if i == int(line_number):
            return list_of_id[i-1]



def collect_ids(table):
    ids = []
    for row in table:
        ids.append(row[0])
    return ids


def sort_list_in_asc(list):

    N = len(list)
    iteration = 1
    while iteration < N:
        j = 0
        while j <= (N - 2):
            if list[j] > list[j + 1]:
                temp = list[j + 1]
                list[j + 1] = list[j]
                list[j] = temp
                j += 1
            else:
                j += 1
        iteration += 1


def common_update(table, id_, file_name, header_list):
    new_items = []
    ids = collect_ids(table)
    if id_[0] in ids:
        new_items.append(id_[0])
        new_elements = ui.get_inputs(header_list, "Please add the items")
        for item in new_elements:
            new_items.append(item)
        for i in range(len(table)):
            if table[i][0] == id_[0]:
                table[i] = new_items
    else:
        ui.print_error_message("There is no such option.")
    return table


def common_add(table, header_list):
    random_id = generate_random(table)
    inputs = ui.get_inputs(header_list, "Please add the items")
    inputs.insert(0, random_id)
    table.append(inputs)
    return table


def common_show_table(table, header_list):
    return ui.print_table(table, header_list)


def common_remove(table, id_, file_name):
    ids = collect_ids(table)
    if id_[0] in ids:
        for i in range(len(table)):
            if table[i][0] == id_[0]:
                table.pop(i)
                break
    else:
        ui.print_error_message("There is no such option.")
    return table


def common_write_to_file(table, file_name):
    return data_manager.write_table_to_file(file_name, table)


def get_crm_table():
    table = data_manager.get_table_from_file("crm/customers.csv")
    return table


def get_sales_table():
    table = data_manager.get_table_from_file("sales/sales.csv")
    return table
