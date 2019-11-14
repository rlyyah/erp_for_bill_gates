""" Common module
implement commonly used functions here
"""

import random

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
