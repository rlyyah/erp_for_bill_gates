""" Sales module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game sold
    * price (number): The actual sale price in USD
    * month (number): Month of the sale
    * day (number): Day of the sale
    * year (number): Year of the sale
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


def handle_menu_inventory_module():
    options = ["Show table",
               "Add item to table",
               "Remove item from the table",
               "Update item in table",
               "Get lowest price item id",
               'Get items sold between']

    menu_title = "Sales module menu"
    menu_title = ui.return_headline_for_menu_title_(menu_title)
    exit_message = "Back to main menu"
    ui.print_menu(menu_title, options, exit_message)


def choose_inventory_module():
    FILE_PATH = 'sales/sales.csv'

    table = data_manager.get_table_from_file(FILE_PATH)
    inputs = ui.get_inputs(["Please enter a number: "], "")
    INDEX_OF_FIRST_ELEMENT_OF_INPUTS_LIST = 0
    option = inputs[INDEX_OF_FIRST_ELEMENT_OF_INPUTS_LIST]
    if option == "0":
        return False
    elif option == "1":
        common.clear_terminal()
        ui.blank_line()
        ui.headline('---- TABLE WITH SALES ----')
        ui.blank_line()
        show_table(data_manager.get_table_from_file(FILE_PATH))     # ONLY THIS NEEDEd TO PRINT TABLE RIGHT NOW
    elif option == "2":
        # list_from_file = data_manager.get_table_from_file(FILE_PATH)
        # data_manager.write_table_to_file(FILE_PATH, add(list_from_file))
        common.clear_terminal()
        ui.blank_line()
        data_manager.write_table_to_file(FILE_PATH, add(data_manager.get_table_from_file(FILE_PATH)))     # same as above but in one line
    elif option == "3":
        common.clear_terminal()
        ui.headline('---- TABLE WITH SALES ----')
        table = data_manager.get_table_from_file(FILE_PATH)
        ui.blank_line()
        show_table(data_manager.get_table_from_file(FILE_PATH))     # ONLY THIS NEEDEd TO PRINT TABLE RIGHT NOW
        ui.blank_line()
        ui.blank_line()
        ui.headline('Removing item from sales')
        # header = ui.headline('Removing item from inventory')
        data_manager.write_table_to_file(FILE_PATH, remove(table, find_id(table, ui.get_inputs(['Insert index of file to remove'], "REMOVE"))))
        # data_manager.write_table_to_file(FILE_PATH, remove(table, find_id(table, ui.get_inputs(['Insert index of file to remove'], header))))
    elif option == "4":
        common.clear_terminal()
        ui.blank_line()
        ui.blank_line()
        ui.headline('EDITING EXISTING RECORD')
        table = data_manager.get_table_from_file(FILE_PATH)
        ui.blank_line()
        show_table(data_manager.get_table_from_file(FILE_PATH))     # ONLY THIS NEEDEd TO PRINT TABLE RIGHT NOW
        data_manager.write_table_to_file(FILE_PATH, update(table, find_id(table, ui.get_inputs(['Insert index of file to update'], "UPDATING"))))
    elif option == "5":
        ui.print_result(get_lowest_price_item_id(table),"Lowest price ID")
    elif option == "6":
        TITLE_LIST = ['id', 'title', 'price', 'month', 'day', 'year']
        user_inputs = ui.get_inputs(['month_from', 'day_from', 'year_from', 'month_to', 'day_to', 'year_to'],'get_items_sold_between')
        ui.print_table(get_items_sold_between(table, user_inputs[0], user_inputs[1], user_inputs[2], user_inputs[3], user_inputs[4], user_inputs[5]),TITLE_LIST)
    elif option == "0":
        # print('asdasdas')
        # common.clear_terminal()
        # print('asdasdas')
        return False
    else:
        common.clear_terminal()
        print('Please enter number of one of the options')
        # raise KeyError("There is no such option.")
    return True


def find_id(table, index):
    INDEX_POSITION = 0
    INDEX_OF_FIRST_ELEMENT_OF_INDEX_LIST = 0
    NUMBER_TO_DISTRACT_BECAUES_INDEXING_IS_FROM_ZER0 = 1
    number_of_id = table[int(index[INDEX_OF_FIRST_ELEMENT_OF_INDEX_LIST]) - NUMBER_TO_DISTRACT_BECAUES_INDEXING_IS_FROM_ZER0][INDEX_POSITION]
    # number_of_id = number_of_id - 1
    return number_of_id


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
        handle_menu_inventory_module()
        try:
            is_running = choose_inventory_module()
        except KeyError as err:
            ui.print_error_message(str(err), 'There is no such option')


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """
    TITLE_LIST = ['id', 'title', 'price', 'month', 'day', 'year']

    ui.print_table(table, TITLE_LIST)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    ui.headline('Adding item to inventory')

    id = common.generate_random(table)
    # without id!!!!! :
    # TITLE_LIST = ['id: ', 'What is the item? ', 'Who manufactured the item? ', 'What is the purchase year? [year]', 'What is the durability? [year] ']
    TITLE_LIST = ['What is the name? ', 'What is the price? ', 'What is the month? ', 'What is the day? ', 'What is the year? ']
    ask_input = ui.get_inputs(TITLE_LIST, 'Please enter information about an item')

    INDEX_OF_ID_TO_ADD_TO_ASK_INPUT = 0
    ask_input.insert(INDEX_OF_ID_TO_ADD_TO_ASK_INPUT, id)
    table.append(ask_input)

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

    TITLE_LIST = ['What is the item? ', 'Who manufactured the item? ', 'What is the purchase year? [year]', 'What is the durability? [year] ']
    ask_input = ui.get_inputs(TITLE_LIST, 'Please enter information about an item')

    # print('ask input: ', ask_input)
    # print('ask input 0:', ask_input[0])

    ID_POSITION = 0
    INDEX_OF_SECOND_ELEMENT_OF_RECORD = 1
    INDEX_OF_THIRD_ELEMENT_OF_RECORD = 2
    INDEX_OF_FOURTH_ELEMENT_OF_RECORD = 3
    INDEX_OF_FIVE_ELEMENT_OF_RECORD = 4
    INDEX_OF_SIX_ELEMENT_OF_RECORD = 5

    INDEX_OF_FIRST_ELEMENT_OF_ASK_INPUT = 0
    INDEX_OF_SECOND_ELEMENT_OF_ASK_INPUT = 1
    INDEX_OF_THIRD_ELEMENT_OF_ASK_INPUT = 2
    INDEX_OF_FOURTH_ELEMENT_OF_ASK_INPUT = 3
    INDEX_OF_FIVE_ELEMENT_OF_ASK_INPUT = 4

    for record in table:
        if record[ID_POSITION] == id_:
            # print(record[ID_POSITION])
            # print(record)
            record[INDEX_OF_SECOND_ELEMENT_OF_RECORD] = ask_input[INDEX_OF_FIRST_ELEMENT_OF_ASK_INPUT]
            record[INDEX_OF_THIRD_ELEMENT_OF_RECORD] = ask_input[INDEX_OF_SECOND_ELEMENT_OF_ASK_INPUT]
            record[INDEX_OF_FOURTH_ELEMENT_OF_RECORD] = ask_input[INDEX_OF_THIRD_ELEMENT_OF_ASK_INPUT]
            record[INDEX_OF_FIVE_ELEMENT_OF_RECORD] = ask_input[INDEX_OF_FOURTH_ELEMENT_OF_ASK_INPUT]
            record[INDEX_OF_SIX_ELEMENT_OF_RECORD] = ask_input[INDEX_OF_FIVE_ELEMENT_OF_ASK_INPUT]

    return table


# special functions:
# ------------------

def get_lowest_price_item_id(table):
    """
    Question: What is the id of the item that was sold for the lowest price?
    if there are more than one item at the lowest price, return the last item by alphabetical order of the title

    Args:
        table (list): data table to work on

    Returns:
         string: id
    """
    PRICE_POSITION = 2
    FIRST_ITEM = 0
    lowest_price = int(table[FIRST_ITEM][PRICE_POSITION])
    lowest_index = 0

    for index, record in enumerate(table):
        if int(record[PRICE_POSITION]) < lowest_price:
            lowest_price = int(record[PRICE_POSITION])
            lowest_index = index

    lowest_id = find_id(table,str(lowest_index))

    return lowest_id    
        
    # your code


def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    """
    Question: Which items are sold between two given dates? (from_date < sale_date < to_date)

    Args:
        table (list): data table to work on
        month_from (int)
        day_from (int)
        year_from (int)
        month_to (int)
        day_to (int)
        year_to (int)

    Returns:
        list: list of lists (the filtered table)
    """
    line = []
    line_wrapper = []
    MONTH_POSITION = 3
    DAY_POSITION = 4
    YEAR_POSITION = 5
    # 3 4 5
    for record in table:
        if int(record[5]) >= int(year_from): 
            if int(record[5]) <= int(year_to):
                if int(record[3]) >= int(month_from):
                    if int(record[3]) <= int(month_to):
                        if int(record[4]) >= int(day_from): 
                            if int(record[4]) <= int(day_to):
                                line = record[:]
                                line_wrapper.append(line)

    return line_wrapper


    # your code
