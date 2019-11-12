""" Common module
implement commonly used functions here
"""

import random

# FUNCTIONS TO CREATE ID
# variables for generating random id
numbers = '0123456789'
letters = 'abcdefghijklmnoprstuwxyz'
sings = "!#$%&'()*+,-./:_<=>?@][`^{|}~"
id_index = 0


# creates id
def create_id():
    elem_id1 = ''.join(random.sample(numbers, 2))
    elem_id2 = ''.join(random.sample(letters, 2))
    elem_id3 = ''.join(random.sample(sings, 2))
    elem_id4 = ''.join(random.sample(letters, 2)).upper()
    id = elem_id1 + elem_id2 + elem_id3 + elem_id4
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

    generated = ''
    id_table = [line[id_index] for line in table]
    generated = create_id()
    if id in id_table:
        generate_random(table)
    else:
        return generated


    # your code

    
