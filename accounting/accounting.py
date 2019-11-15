""" Accounting module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * month (number): Month of the transaction
    * day (number): Day of the transaction
    * year (number): Year of the transaction
    * type (string): in = income, out = outflow
    * amount (int): amount of transaction in USD
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common

DATA_TABLE_STRUCTURE = ['id', 'month', 'day', 'year', 'type[in = income, out = outflow]', 'amount']


def choose():
    FILE_PATH = 'accounting/items.csv'
    table = data_manager.get_table_from_file(FILE_PATH)
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1":
        show_table(table)
    elif option == "2":
        data_manager.write_table_to_file(FILE_PATH, add(table))
    elif option == "3":
        ui.print_table(table, DATA_TABLE_STRUCTURE)
        to_be_removed = ui.get_inputs(['index'], 'remove')
        data_manager.write_table_to_file(FILE_PATH, remove(table, find_id(table, to_be_removed)))
    elif option == "4":
        ui.print_table(table, DATA_TABLE_STRUCTURE)
        to_be_updated = ui.get_inputs(['index'], 'update')
        data_manager.write_table_to_file(FILE_PATH, update(table, find_id(table, to_be_updated)))
    elif option == "5":
        table = data_manager.get_table_from_file(FILE_PATH)
        ui.print_result(which_year_max(table), "Max profits year")
    elif option == "6":
        table = data_manager.get_table_from_file(FILE_PATH)
        year = ui.get_inputs(['year'], 'which year?')
        ui.print_result(avg_amount(table, year[0]),'avg year')
    elif option == "0":
        return False
    else:
        raise KeyError("There is no such option.")
    return True


def handle_menu():
    options = ["Show Table",
               "Add",
               "Remove",
               "Update",
               "Which year max",
               "Average amount"]

    ui.print_menu("Accounting Module", options, "Back to main menu")


def find_id(table, index):
    INDEX_POSITION = 0
    id_ = table[int(index[0])-1][INDEX_POSITION]
    return id_

def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    is_running = True
    while is_running:
        handle_menu()
        try:
            is_running = choose()
        except KeyError as err:
            ui.print_error_message(str(err))
    # DONE


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """
    ui.print_table(table, DATA_TABLE_STRUCTURE)
    # your code


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """
    data_table_structure = ['month','day','year','type[in = income, out = outflow]','amount']
    line = [common.create_id()]
    new_input = ui.get_inputs(data_table_structure, 'Accounting')
    for el in new_input:
        line.append(el)
    table.append(line)
    # your code

    return table


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """
    ID_POSITION = 0
    for index, record in enumerate(table):
        if record[ID_POSITION] == id_:
            table.pop(index)
    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table (list): list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """
    ID_POSITION = 0
    data_table_structure = ['month', 'day', 'year', 'type[in = income, out = outflow]', 'amount']
    new_input = ui.get_inputs(data_table_structure, 'Accounting')
    for record in table:
        if record[ID_POSITION] == id_:
            for num, col in enumerate(new_input):
                record[num+1] = col
    return table


# special functions:
# ------------------

def which_year_max(table):
    """
    Question: Which year has the highest profit? (profit = in - out)

    Args:
        table (list): data table to work on

    Returns:
        number
    """
    AMOUNT_POSITION = 5
    TYPE_POSITION = 4
    YEAR_POSITION = 3

    year_dict = {}
    for record in table:
        if record[YEAR_POSITION] in year_dict:
            if record[TYPE_POSITION] == 'in':
                year_dict[record[YEAR_POSITION]] += int(record[AMOUNT_POSITION])
            else:
                year_dict[record[YEAR_POSITION]] -= int(record[AMOUNT_POSITION])
        else:
            if record[TYPE_POSITION] == 'in':
                year_dict[record[YEAR_POSITION]] = int(record[AMOUNT_POSITION])
            else:
                year_dict[record[YEAR_POSITION]] = -int(record[AMOUNT_POSITION])
    year_max = 0
    which_year = ''
    for el in year_dict.keys():
        if year_dict[el] > year_max:
            year_max = year_dict[el]
            which_year = el

    return which_year

    # your code


def avg_amount(table, year):
    """
    Question: What is the average (per item) profit in a given year? [(profit)/(items count)]

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        number
    """
    AMOUNT_POSITION = 5
    TYPE_POSITION = 4
    YEAR_POSITION = 3

    year_profit = 0
    year_count = 0

    for record in table:
        if record[YEAR_POSITION] == year:
            if record[TYPE_POSITION] == 'in':
                year_profit += int(record[AMOUNT_POSITION])
            else:
                year_profit -= int(record[AMOUNT_POSITION])
        year_count += 1
    return float(year_profit/year_count)

    # your code
