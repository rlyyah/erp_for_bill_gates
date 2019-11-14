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


def clear_terminal():
    print("\033c")