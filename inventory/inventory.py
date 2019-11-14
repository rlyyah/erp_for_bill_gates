""" Inventory module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string): Name of item
    * manufacturer (string)
    * purchase_year (number): Year of purchase
    * durability (number): Years it can be used
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
               "Available items",
               'Show average durability by manufacturers']

    menu_title = "Inventory module:"
    exit_message = "Back to main menu"
    ui.print_menu(menu_title, options, exit_message)


def choose_inventory_module():
    FILE_PATH = 'inventory/inventory.csv'
    TITLE_LIST = ['id', 'name', 'manufacturer', 'purchase_year', 'durability']

    table = data_manager.get_table_from_file(FILE_PATH)
    inputs = ui.get_inputs(["Please enter a number: "], "")
    INDEX_OF_FIRST_ELEMENT_OF_INPUTS_LIST = 0
    option = inputs[INDEX_OF_FIRST_ELEMENT_OF_INPUTS_LIST]
    if option == "0":
        return False
    elif option == "1":
        common.clear_terminal()
        ui.blank_line()
        ui.headline('---- TABLE WITH INVENTORY ----')
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
        ui.headline('---- TABLE WITH INVENTORY ----')
        table = data_manager.get_table_from_file(FILE_PATH)
        # ui.print_table(table, "where is it?")  # second parameter not used yet TODO
        ui.print_enumerate_table(table)
        ui.blank_line()
        ui.blank_line()
        ui.headline('Removing item from inventory')
        # header = ui.headline('Removing item from inventory')
        data_manager.write_table_to_file(FILE_PATH, remove(table, find_id(table, ui.get_inputs(['Insert index of file to remove'], "REMOVE"))))
        # data_manager.write_table_to_file(FILE_PATH, remove(table, find_id(table, ui.get_inputs(['Insert index of file to remove'], header))))
    elif option == "4":
        common.clear_terminal()
        ui.blank_line()
        ui.blank_line()
        ui.headline('EDITING EXISTING RECORD')
        table = data_manager.get_table_from_file(FILE_PATH)
        ui.print_enumerate_table(table)
        data_manager.write_table_to_file(FILE_PATH, update(table, find_id(table, ui.get_inputs(['Insert index of file to update'], "UPDATING"))))
    elif option == "5":
        common.clear_terminal()
        ui.headline('GETTING AVAILABLE ITEMS')
        TITLE_LIST = ['']
        year = ui.get_inputs(TITLE_LIST, "Please enter information about year")
        INDEX_OF_FIRST_ELEMENT_OF_YEAR_LIST = 0
        year = int(year[INDEX_OF_FIRST_ELEMENT_OF_YEAR_LIST])
        ui.blank_line()
        ui.headline('ITEMS THAT MEETS YOUR CONDITIONS')
        ui.blank_line()
        show_table(get_available_items(table, year))
    elif option == "6":
        common.clear_terminal()
        ui.blank_line()
        ui.blank_line()
        ui.headline('GETTING AVERAGE DURABILITY BY MANUFRACTURERS')
        table = data_manager.get_table_from_file(FILE_PATH)
        ui.blank_line()
        ui.print_dictionary(get_average_durability_by_manufacturers(table))


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
            ui.print_error_message(str(err))


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """
    TITLE_LIST = ['id', 'name', 'manufacturer', 'purchase_year', 'durability']
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
    TITLE_LIST = ['What is the item? ', 'Who manufactured the item? ', 'What is the purchase year? [year]', 'What is the durability? [year] ']
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

    INDEX_OF_FIRST_ELEMENT_OF_ASK_INPUT = 0
    INDEX_OF_SECOND_ELEMENT_OF_ASK_INPUT = 1
    INDEX_OF_THIRD_ELEMENT_OF_ASK_INPUT = 2
    INDEX_OF_FOURTH_ELEMENT_OF_ASK_INPUT = 3

    for record in table:
        if record[ID_POSITION] == id_:
            # print(record[ID_POSITION])
            # print(record)
            record[INDEX_OF_SECOND_ELEMENT_OF_RECORD] = ask_input[INDEX_OF_FIRST_ELEMENT_OF_ASK_INPUT]
            record[INDEX_OF_THIRD_ELEMENT_OF_RECORD] = ask_input[INDEX_OF_SECOND_ELEMENT_OF_ASK_INPUT]
            record[INDEX_OF_FOURTH_ELEMENT_OF_RECORD] = ask_input[INDEX_OF_THIRD_ELEMENT_OF_ASK_INPUT]
            record[INDEX_OF_FIVE_ELEMENT_OF_RECORD] = ask_input[INDEX_OF_FOURTH_ELEMENT_OF_ASK_INPUT]

    return table


# special functions:
# ------------------

def get_available_items(table, year):
    """
    Question: Which items have not exceeded their durability yet (in a given year)?

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        list: list of lists (the inner list contains the whole row with their actual data types)
    """

    # ACTUAL_YEAR = 2019
    # TITLE_LIST = ['What is the year you want to know the items will be still available? ']
    # year = ui.get_inputs(TITLE_LIST, "Please enter information about year")
    
    PURCHASE_YEAR_INDEX = 3
    DURABILITY_INDEX = 4
    list_of_available_items = []

    for elem in range(len(table)):
        # print(table[elem])
        # print(table[elem][PURCHASE_YEAR_INDEX])

        table[elem][PURCHASE_YEAR_INDEX] = int(table[elem][PURCHASE_YEAR_INDEX])
        # print(table[elem][PURCHASE_YEAR_INDEX])

        table[elem][DURABILITY_INDEX] = int(table[elem][DURABILITY_INDEX])
        # print(table[elem][DURABILITY_INDEX])
        
        expiration_difference = table[elem][PURCHASE_YEAR_INDEX] + table[elem][DURABILITY_INDEX]
        # print('expi diff: ', expiration_difference)

        if expiration_difference >= year:
            list_of_available_items.append(table[elem])

    # print(list_of_available_items)
    return list_of_available_items 


def get_average_durability_by_manufacturers(table):
    """
    Question: What are the average durability times for each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
        dict: a dictionary with this structure: { [manufacturer] : [avg] }
    """

    list_of_manufacturers = []
    manufacturer_index = 2
    # print(table)
    for elem in table:
        # print(elem)
        list_of_manufacturers.append(elem[manufacturer_index])
    
    # print()
    # print(list_of_manufacturers)
    adding_one_to_count_of_each_manufacturers = 1 

    dictionary_of_manufacturers = {}
    for elem in list_of_manufacturers:
        if elem in dictionary_of_manufacturers:
            dictionary_of_manufacturers[elem] += adding_one_to_count_of_each_manufacturers
        else:
            dictionary_of_manufacturers[elem] = adding_one_to_count_of_each_manufacturers

    # print(dictionary_of_manufacturers)
    return dictionary_of_manufacturers
