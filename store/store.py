""" Store module
Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game
    * manufacturer (string)
    * price (number): Price in dollars
    * in_stock (number)
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common
import sys


# general variables for store
file_name = 'store/games.csv'
table = data_manager.get_table_from_file(file_name)
id_index = 0
title_index = 1
manuf_index = 2
price_index = 3
stock_index = 4
manufacturer = ''


# variables for menu
OPTION = ['0', '1', '2', '3', '4', '5', '6']
title = "Store menu:"
options = ["Show table",
           "Add record",
           "Remove record",
           "Update data",
           "Counts by manufacturers",
           "The average amount of games of a manufacturer"]
exit_message = "Back to main menu"


# variables for function show in store:
title_list = ['Id', 'Title', 'Manufacturer', 'Price', 'In stock']


# variables for store function remove and update
id_ = ''
details_update_list_labels = 'Number of category: '
detail_update_title = """Please provide number of category you want to update:
1 - Title, 2 - Manufacturer, 3 - Price, 4 - In stock"""


# helpful functions for store only
# choosing option in menu
def choose():
    """ Function gets input from user
    and starts options from module.
    No arg
    Returns nothing"""
    inputs = ui.get_inputs(['Enter a number: '], '')
    option = inputs[0]
    if option == "1":
        show_table(table)
    elif option == "2":
        add(table)
    elif option == "3":
        remove(table, id_)
    elif option == "4":
        update(table, id_)
    elif option == "5":
        ui.print_result(get_counts_by_manufacturers(table), 'Kinds of game of each manufacturer: ')
    elif option == "6":
        ui.print_result(get_average_by_manufacturerERP(table, manufacturer),
                        'Average amount of games in stock of a manufacturer: ')
    elif option == '0':
        sys.exit(0)
    while option not in OPTION:
        raise KeyError
        #menu_control()


# Main store module
# starts module store
def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.
    Returns:
        None
    """

    while True:
        ui.print_menu(title, options, exit_message)
        try:
            choose()
        except ValueError:
            break
        except KeyError:
            ui.print_error_message('There is no such option')


# shows all data in table
def show_table(table):
    """
    Display a table
    Args:
        table (list): list of lists to be displayed.
    Returns:
        None
    """
    table = data_manager.get_table_from_file(file_name)
    ui.print_table(table, title_list)


# adds record to table
def add(table):
    """
    Asks user for input and adds it into the table.
    Args:
        table (list): table to add new record to
    Returns:
        list: Table with a new record
    """

    module_headers = ["Title: ", "Manufacturer: ", "Price: ", "In stock: "]
    return common.common_add(table, module_headers)


# removes record from table
def remove(table, id_):
    """
    Remove a record with a given id from the table.
    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed
    Returns:
        list: Table without specified record.
    """
    return common.common_remove(table, id_, "store/games.csv")



# updates record in table
def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.
    Args:
        table (list): list in which record should be updated
        id_ (str): id of a record to update
    Returns:
        list: table with updated record
    """

    module_headers = ["Title: ", "Manufacturer: ", "Price: ", "In stock: "]
    return common.common_update(table, id_, "inventory/inventory.csv", module_headers)


# Special functions
# counts item by manufacturer
def get_counts_by_manufacturers(table):
    """
    Question: How many different kinds of game are available of each manufacturer?
    Args:
        table (list): data table to work on
    Returns:
         dict: A dictionary with this structure: { [manufacturer] : [count] }
    """

    counted_games = {}
    for item in table:
        if item[manuf_index] in counted_games.keys():
            counted_games[item[manuf_index]] += 1
        else:
            counted_games[item[manuf_index]] = 1
    return counted_games


# function for ERP - manufacturer is an input
def get_average_by_manufacturerERP(table, manufacturer):
    """
    Question: What is the average amount of games in stock of a given manufacturer?
    Args:
        table (list): data table to work on
        manufacturer (str): Name of manufacturer
    Returns:
         number
    """

    manufacturers = []
    in_stocks = []
    total = 0
    try:
        for i in range(len(table)):
            if manufacturer == table[i][2]:
                in_stocks.append(int(table[i][4]))
        for in_stock in in_stocks:
            total += in_stock
        return total / len(in_stocks)
    except BaseException:
        ui.print_error_message("There's no such manufacturer in table!")

