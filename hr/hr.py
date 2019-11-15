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
    table = data_manager.get_table_from_file("hr/persons.csv")
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1":
        show_table(table)
    elif option == "2":
        common.clear_terminal()
        ui.blank_line()
        data_manager.write_table_to_file("hr/persons.csv", add(table))
    elif option == "3":
        show_table(table)
        data_manager.write_table_to_file("hr/persons.csv", update(table, find_id(table, ui.get_inputs(['Insert index of file to update'], "UPDATE"))))

    elif option == "4":
        common.clear_terminal()
        ui.headline('----  Persons Table  ----')
        table = data_manager.get_table_from_file("hr/persons.csv")
        ui.print_enumerate_table(table)
        ui.blank_line()
        ui.blank_line()
        ui.headline('Removing person from list')
        data_manager.write_table_to_file("hr/persons.csv", remove(table, find_id(table, ui.get_inputs(['Insert index of file to remove'], "REMOVE"))))
        
    elif option == "5":
        ui.print_result(get_oldest_person(table), "Oldest people")

    elif option == "6":
        ui.print_result(get_persons_closest_to_average(table), "Average persons")

    elif option == "0":
        sys.exit(0)
    else:
        raise KeyError("There is no such option.")


def find_id(table, index):
    INDEX_POSITION = 0
    number_of_id = table[int(index[0])-1][INDEX_POSITION]
    return number_of_id   


def show_table(table):
    TITLE_LIST = ['id', 'name', 'year']
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
    TITLE_LIST = ['What is name? ', 'What is born year?']
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
    ID_POSITION = 0
    for index, record in enumerate(table):
        if record[ID_POSITION] == id_:
            table.pop(index)

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

    TITLE_LIST = ['What is name? ', 'What is born year?']
    ask_input = ui.get_inputs(TITLE_LIST, 'Please enter information about a person')
    ID_POSITION = 0
    INDEX_OF_SECOND_ELEMENT_OF_RECORD = 1
    INDEX_OF_THIRD_ELEMENT_OF_RECORD = 2

    INDEX_OF_FIRST_ELEMENT_OF_ASK_INPUT = 0
    INDEX_OF_SECOND_ELEMENT_OF_ASK_INPUT = 1

    for record in table:
        if record[ID_POSITION] == id_:
            record[INDEX_OF_SECOND_ELEMENT_OF_RECORD] = ask_input[INDEX_OF_FIRST_ELEMENT_OF_ASK_INPUT]
            record[INDEX_OF_THIRD_ELEMENT_OF_RECORD] = ask_input[INDEX_OF_SECOND_ELEMENT_OF_ASK_INPUT]
    return table


# special functions:
# ------------------

def get_oldest_person(table):
    max = 99999
    year_list = []
    for i in range(len(table)):
        year_list.append(int(table[i][2]))
    for i in range(len(year_list)):
        if year_list[i] < max:
            max = year_list[i]
            name = table[i][1]
        list_oldest_persons = []
        for i in range(len(year_list)):
            if max == year_list[i]:
                list_oldest_persons.append(table[i][1])

    return list_oldest_persons
    """
    Question: Who is the oldest person?
    Args:
        table (list): data table to work on
    Returns:
        list: A list of strings (name or names if there are two more with the same value)
    """

    # your code


def get_persons_closest_to_average(table):
    year_list = []
    for i in range(len(table)):
        year_list.append(int(table[i][2]))
    sum = 0
    for ele in year_list:
        sum += ele
    averega_years = sum / len(year_list)

    min_diff = None
    closest = None
    for i in year_list:
        diff = abs(averega_years - i)
        if min_diff is None or diff < min_diff:
            min_diff = diff
            closest = i
            a = year_list.index(closest)
    
    list_avg_pers = []
    for i in range(len(year_list)):
        if closest == year_list[i]:
            list_avg_pers.append(table[i][1])
        else:
            pass
    
    return list_avg_pers
    
    """
    Question: Who is the closest to the average age?
    Args:
        table (list): data table to work on
    Returns:
        list: list of strings (name or names if there are two more with the same value)
    """

    # your code