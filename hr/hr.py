""" Human resources module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * birth_year (number)
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


def start_module():
    is_running = True
    while is_running:
        handle_menu()
        try:
            is_running = choose()
        except KeyError as err:
            ui.print_error_message(str(err))
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    # your code


def handle_menu():
    options = ["Show table", "Add new item", "Update item", "Remove item", "Get oldest person", "Get persons closest to average"]
    menu_title = "HR module"
    exit_message = "Back to main menu"
    ui.print_menu(menu_title, options, exit_message)


def choose():
    path = data_manager.get_table_from_file("hr/persons.csv")
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1":
        show_table(path)
    elif option == "2":
        common.clear_terminal()
        ui.blank_line()
        data_manager.write_table_to_file(path, add(path))
    elif option == "3":
        update()
    elif option == "4":
        common.clear_terminal()
        ui.headline('----  Persons Table  ----')
        table = data_manager.get_table_from_file(path)
        ui.print_enumerate_table(table)
        ui.blank_line()
        ui.blank_line()
        ui.headline('Removing person from list')
        data_manager.write_table_to_file(path, remove(table, find_id(table, ui.get_inputs(['Insert index of file to remove'], "REMOVE"))))
        
    elif option == "5":
        get_oldest_person(table)
    elif option == "6":
        get_persons_closest_to_average(table)
    elif option == "0":
        sys.exit(0)
    else:
        raise KeyError("There is no such option.")
    

def show_table(table):
    TITLE_LIST = [id, 'name', 'year']
    ui.print_table(table, TITLE_LIST)
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """
    
    # your code


def add(table):
    ui.headline('Adding person to the list')
    # path = data_manager.get_table_from_file("hr/persons.csv")
    table = data_manager.get_table_from_file("hr/persons.csv")
    id = common.generate_random(table)
    TITLE_LIST = ['What is ID? ', 'What is name? ', 'What is born year?']
    ask_input = ui.get_inputs(TITLE_LIST, 'Please enter information about a person')
    ask_input.insert(0, id)
    table.append(ask_input)
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    # your code

    return table


def remove(table, id_):
    D_POSITION = 0
    for index, record in enumerate(table):
        if record[ID_POSITION] == id_:
            table.pop(index - 1)

    return table
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """

    # your code

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

    # your code

    return table


# special functions:
# ------------------

def get_oldest_person(table):
    """
    Question: Who is the oldest person?

    Args:
        table (list): data table to work on

    Returns:
        list: A list of strings (name or names if there are two more with the same value)
    """

    # your code


def get_persons_closest_to_average(table):
    """
    Question: Who is the closest to the average age?

    Args:
        table (list): data table to work on

    Returns:
        list: list of strings (name or names if there are two more with the same value)
    """

    # your code
