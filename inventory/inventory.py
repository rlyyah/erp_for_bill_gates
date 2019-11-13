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
               "Add product to table"]

    menu_title = "Inventory module:"
    exit_message = "Back to main menu"
    ui.print_menu(menu_title, options, exit_message)


def choose_inventory_module():
    # inv = data_manager.get_table_from_file(table) 
    FILE_PATH = 'inventory/inventory.csv'
    TITLE_LIST = [id, 'name', 'manufacturer', 'purchase_year', 'durability']
    inventory = data_manager.get_table_from_file(FILE_PATH)

    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "0":
        return False
    if option == "1":
        show_table(data_manager.get_table_from_file(FILE_PATH))     # ONLY THIS NEEDEd TO PRINT TABLE RIGHT NOW
        # display_table = show_table(data_manager.get_table_from_file(FILE_PATH))
        # ui.print_table(display_table, TITLE_LIST)
        # ui.print_table(show_table(inventory), TITLE_LIST)
        # ui.print_table(show_table(FILE_PATH), TITLE_LIST)     # UNCOMMENT TO WORK - VERSION 1
    if option == "2":
        # add('inventory/inventory.csv')
        ui.print_table(add(FILE_PATH), TITLE_LIST)


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
    print('I am in inventory module')   # delete in future!!
    # your code


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """
    # inv = data_manager.get_table_from_file(table)     # UNCOMMENT TO WORK - VERSION 1
    # print(inv)            # 2 versions of printing
    # print()
    # for elem in inv:
        # print(elem)

    # print(inv)
    # print()

    # for i in range(1, 11):        # printing in one line example
    #     print(i, end='')
    # return inv    # UNCOMMENT TO WORK - VERSION 1
    TITLE_LIST = [id, 'name', 'manufacturer', 'purchase_year', 'durability']
    ui.print_table(table, TITLE_LIST)

    # FILE_PATH = 'inventory/inventory.csv'
    # inventory = data_manager.get_table_from_file(FILE_PATH)
    # table = data_manager.get_table_from_file(table)     # UNCOMMENT TO WORK - VERSION 1
    # ui.print_table(table, title_list)     # use in future!!


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    # your code
    new_record = []
    # adding_new_record_text = '\033[1;34;49m ADDING NEW ALBUM'
    # adding_new_record_text_alignment = adding_new_record_text.center(60)
    # print(adding_new_record_text_alignment)
    # print('\033[0;37;49m ')

    # use in future!!
    # id = common.generate_random(table)
    # input_class_list = [id, 'name', 'manufacturer', 'purchase_year', 'durability']
    
    input_class_list = ['id', 'name', 'manufacturer', 'purchase_year', 'durability']
    for elem in input_class_list:
        element = input(f'Input {elem} : ')
        new_record.append(element)
    print()
    new_record_text = 'Your new record is: '
    print(new_record_text)
    print()
    print(new_record)
    print()

    # inv = data_manager.get_table_from_file(table)

    # record_to_file = ','.join(new_record)
    # print('r to file:      ', record_to_file)
    
    # table.append(record_to_file)
    # data_manager.write_table_to_file(inv, table)
    # show_table(table)

    # return table
    
    record_to_file = ','.join(new_record)
    with open(table, 'a+') as fo:
        print('It has been added to record list')
        print(record_to_file)
        fo.writelines('\n' + record_to_file)
        # fo.writelines('%s' % '\n' + record_to_file)
        fo.close()

    inv = data_manager.get_table_from_file(table)
    return inv

    # return new_record           # which one??
    # return table        # this one should be? why return table???


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """

    # your code
    # for elem in inv:
    #     print(elem)

    # show_table(table)
    # line_number = input_mod.number_with_terms('Line: ', 'Please provide number of line you want to remove',
    #                                 range(1, (len(table) + 1)))
    # id_ = common.convert_input_to_id(table, line_number)
    # for line in table:
    #     if line[0] == id_:
    #         table.remove(line)
    # data_manager.write_table_to_file(file_name, table)
    # show_table(table)
    # return table

    # return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table (list): list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    # your code

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

    # your code


def get_average_durability_by_manufacturers(table):
    """
    Question: What are the average durability times for each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
        dict: a dictionary with this structure: { [manufacturer] : [avg] }
    """

    # your code
