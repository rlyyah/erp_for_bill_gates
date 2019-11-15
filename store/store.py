<<<<<<< HEAD
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
        tabl""" Customer Relationship Management (CRM) module
Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * email (string)
    * subscribed (int): Is she/he subscribed to the newsletter? 1/0 = yes/no
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


# general variables
file_name = 'crm/customers.csv'
table = data_manager.get_table_from_file(file_name)
id_index = 0
name_index = 1
email_index = 2
subs_index = 3
id_ = ''
id = ''

# variables for menu crm
OPTION = ['0', '1', '2', '3', '4', '5', '6']
title = "CRM menu:"
options = ["Show table",
           "Add record",
           "Remove record",
           "Update data",
           "Get longest name id",
           "Get subscribed emails"]
exit_message = "Back to main menu"


# variables for function show in crm
title_list = ['Id', 'Name', 'Email', 'Subscribed']


# variables for crm function remove and update
id_ = ''
details_update_list_labels = 'Number of category: '
detail_update_title = """Please provide number of category you want to update:
1 - Name', '2 - Email', '3 - Subscription'"""


# helpful functions for crm only
# choosing option in menu
def choose():
    """ Function gets input from user
    and starts options from module.
    No arg
    Returns nothing"""
    FILE_PATH = 'crm/customers.csv'
    # TITLE_LIST = ['id', 'name', 'email', 'subscription']
    # INDEX_OF_FIRST_ELEMENT_OF_INPUTS_LIST = 0

    table = data_manager.get_table_from_file(FILE_PATH)
    inputs = ui.get_inputs(['Enter a number: '], '')
    option = inputs[0]
    if option == "1":
        common.clear_terminal()
        ui.blank_line()
        ui.headline('---- TABLE WITH INVENTORY ----')
        ui.blank_line()
        show_table(table)
    elif option == "2":
        # add(table)
        common.clear_terminal()
        ui.blank_line()
        data_manager.write_table_to_file(FILE_PATH, add(data_manager.get_table_from_file(FILE_PATH)))
    elif option == "3":
        # remove(table, id_)
        common.clear_terminal()
        ui.headline('---- TABLE WITH INVENTORY ----')
        table = data_manager.get_table_from_file(FILE_PATH)
        ui.blank_line()
        show_table(data_manager.get_table_from_file(FILE_PATH))     # ONLY THIS NEEDEd TO PRINT TABLE RIGHT NOW
        ui.blank_line()
        ui.blank_line()
        ui.headline('Removing item from inventory')
        data_manager.write_table_to_file(FILE_PATH, remove(table, find_id(table, ui.get_inputs(['Insert index of file to remove'], "REMOVE"))))
    elif option == "4":
        # update(table, id_)
        common.clear_terminal()
        ui.blank_line()
        ui.blank_line()
        ui.headline('EDITING EXISTING RECORD')
        table = data_manager.get_table_from_file(FILE_PATH)
        ui.blank_line()
        show_table(data_manager.get_table_from_file(FILE_PATH))     # ONLY THIS NEEDEd TO PRINT TABLE RIGHT NOW
        data_manager.write_table_to_file(FILE_PATH, update(table, find_id(table, ui.get_inputs(['Insert index of file to update'], "UPDATING"))))
    elif option == "5":
        ui.print_result(get_longest_name_id(table), 'Longest name: ')
    elif option == "6":
        ui.print_result(get_subscribed_emails(table), 'Customers subscribed to newsletter: ')
    elif option == '0':
        raise ValueError
    while option not in OPTION:
        raise KeyError


# Main crm module
# starts module crm
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


def find_id(table, index):
    INDEX_POSITION = 0
    INDEX_OF_FIRST_ELEMENT_OF_INDEX_LIST = 0
    NUMBER_TO_DISTRACT_BECAUES_INDEXING_IS_FROM_ZER0 = 1
    number_of_id = table[int(index[INDEX_OF_FIRST_ELEMENT_OF_INDEX_LIST]) - NUMBER_TO_DISTRACT_BECAUES_INDEXING_IS_FROM_ZER0][INDEX_POSITION]
    # number_of_id = number_of_id - 1
    return number_of_id


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
    * id (string): Unique and random generated identifier
      at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * email (string)
    * subscribed (int): Is she/he subscribed to the newsletter? 1/0 = yes/no
    """

    ui.headline('Adding item to inventory')

    id = common.generate_random(table)
    # without id!!!!! :
    # TITLE_LIST = ['id: ', 'What is the item? ', 'Who manufactured the item? ', 'What is the purchase year? [year]', 'What is the durability? [year] ']
    TITLE_LIST = ['What is your name? ', 'What is your email? ', 'Do you want to subscribe to the newsletter?  1/0 = yes/no']
    ask_input = ui.get_inputs(TITLE_LIST, 'Please enter information')

    INDEX_OF_ID_TO_ADD_TO_ASK_INPUT = 0
    ask_input.insert(INDEX_OF_ID_TO_ADD_TO_ASK_INPUT, id)
    table.append(ask_input)

    return table


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

    ID_POSITION = 0
    for index, record in enumerate(table):
        if record[ID_POSITION] == id_:
            table.pop(index)

    return table


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
    TITLE_LIST = ['What is your name? ', 'What is your email? ', 'Do you want to subscribe to the newsletter? 1/0 = yes/no']
    ask_input = ui.get_inputs(TITLE_LIST, 'Please enter information about an item')

    # print('ask input: ', ask_input)
    # print('ask input 0:', ask_input[0])

    ID_POSITION = 0
    INDEX_OF_SECOND_ELEMENT_OF_RECORD = 1
    INDEX_OF_THIRD_ELEMENT_OF_RECORD = 2
    INDEX_OF_FOURTH_ELEMENT_OF_RECORD = 3

    INDEX_OF_FIRST_ELEMENT_OF_ASK_INPUT = 0
    INDEX_OF_SECOND_ELEMENT_OF_ASK_INPUT = 1
    INDEX_OF_THIRD_ELEMENT_OF_ASK_INPUT = 2

    for record in table:
        if record[ID_POSITION] == id_:
            # print(record[ID_POSITION])
            # print(record)
            record[INDEX_OF_SECOND_ELEMENT_OF_RECORD] = ask_input[INDEX_OF_FIRST_ELEMENT_OF_ASK_INPUT]
            record[INDEX_OF_THIRD_ELEMENT_OF_RECORD] = ask_input[INDEX_OF_SECOND_ELEMENT_OF_ASK_INPUT]
            record[INDEX_OF_FOURTH_ELEMENT_OF_RECORD] = ask_input[INDEX_OF_THIRD_ELEMENT_OF_ASK_INPUT]
    return table


# function returns id of longest name in reverse alphabetical order
def get_longest_name_id(table):
    """
        Question: What is the id of the customer with the longest name?
        Args:
            table(list): data table to work on
        Returns:
            string: id of the longest name(if there are more than one, return
                the last by alphabetical order of the names)
        """

    names = [line[name_index] for line in table]
    length_of_names = []
    for item in names:
        n = len(item)
        length_of_names.append(n)
    longest = max(length_of_names)
    # list_of_longest = []
    id_name_dict = {}
    for line in table:
        if len(line[name_index]) == longest:
            id_name_dict[line[id_index]] = line[name_index]
    longest_name_reverse_order = max(id_name_dict, key=id_name_dict.get)
    return longest_name_reverse_order


# the question: Which customers has subscribed to the newsletter?
# return type: list of strings (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table):
    """
    Question: Which customers has subscribed to the newsletter?
    Args:
        table (list): data table to work on
    Returns:
        list: list of strings (where a string is like "email;name")
    """

    list_subscribed_customers = []
    for line in table:
        if line[subs_index] == '1':
            email_and_name = str(line[email_index])+';'+str(line[name_index])
            list_subscribed_customers.append(email_and_name)
    return list_subscribed_customers


# functions supports data analyser


def get_name_by_id(id):
    """
    Reads the table with the help of the data_manager module.
    Returns the name (str) of the customer with the given id (str) on None om case of non-existing id.
    Args:
        id (str): the id of the customer
    Returns:
        str: the name of the customer
    """

    table = data_manager.get_table_from_file(file_name)
    for line in table:
        if line[id_index] == id:
            return str(line[name_index])


def get_name_by_id_from_table(table, id):
    """
    Returns the name (str) of the customer with the given id (str) on None om case of non-existing id.
    Args:
        table (list of lists): the customer table
        id (str): the id of the customer
    Returns:
        str: the name of the customer
    """

    for line in table:
        if line[id_index] == id:
            return str(line[name_index])


def get_id_name_set():
    """
    Creates dictionery of id and names of customers
    Arg - table
    Returns dict(k,v) (id: name)
    """

    table = data_manager.get_table_from_file(file_name)
    id_name_dict = {line[id_index]: line[name_index] for line in table}
    return id_name_dicte (list): table to add new record to
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


=======
# """ Store module
# Data table structure:
#     * id (string): Unique and random generated identifier
#         at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
#     * title (string): Title of the game
#     * manufacturer (string)
#     * price (number): Price in dollars
#     * in_stock (number)
# """

# # everything you'll need is imported:
# # User interface module
# import ui
# # data manager module
# import data_manager
# # common module
# import common
# import input_mod
# import sys


# # general variables for store
# file_name = 'store/games.csv'
# table = data_manager.get_table_from_file(file_name)
# id_index = 0
# title_index = 1
# manuf_index = 2
# price_index = 3
# stock_index = 4
# manufacturer = ''


# # variables for menu
# OPTION = ['0', '1', '2', '3', '4', '5', '6']
# title = "Store menu:"
# options = ["Show table",
#            "Add record",
#            "Remove record",
#            "Update data",
#            "Counts by manufacturers",
#            "The average amount of games of a manufacturer"]
# exit_message = "Back to main menu"


# # variables for function show in store:
# title_list = ['Id', 'Title', 'Manufacturer', 'Price', 'In stock']


# # variables for store function remove and update
# id_ = ''
# details_update_list_labels = 'Number of category: '
# detail_update_title = """Please provide number of category you want to update:
# 1 - Title, 2 - Manufacturer, 3 - Price, 4 - In stock"""


# # helpful functions for store only
# # choosing option in menu
# def choose():
#     """ Function gets input from user
#     and starts options from module.
#     No arg
#     Returns nothing"""
#     inputs = input_mod.get_inputs(['Enter a number: '], '')
#     option = inputs[0]
#     if option == "1":
#         show_table(table)
#     elif option == "2":
#         add(table)
#     elif option == "3":
#         remove(table, id_)
#     elif option == "4":
#         update(table, id_)
#     elif option == "5":
#         ui.print_result(get_counts_by_manufacturers(table), 'Kinds of game of each manufacturer: ')
#     elif option == "6":
#         ui.print_result(get_average_by_manufacturerERP(table, manufacturer),
#                         'Average amount of games in stock of a manufacturer: ')
#     elif option == '0':
#         sys.exit(0)
#     while option not in OPTION:
#         raise KeyError
#         #menu_control()


# # Main store module
# # starts module store
# def start_module():
#     """
#     Starts this module and displays its menu.
#      * User can access default special features from here.
#      * User can go back to main menu from here.
#     Returns:
#         None
#     """

#     while True:
#         ui.print_menu(title, list_options, exit_message)
#         try:
#             choose()
#         except ValueError:
#             break
#         except KeyError:
#             ui.print_error_message('There is no such option')


# # shows all data in table
# def show_table(table):
#     """
#     Display a table
#     Args:
#         table (list): list of lists to be displayed.
#     Returns:
#         None
#     """
#     table = data_manager.get_table_from_file(file_name)
#     ui.print_table(table, title_list)


# # adds record to table
# def add(table):
#     """
#     Asks user for input and adds it into the table.
#     Args:
#         table (list): table to add new record to
#     Returns:
#         list: Table with a new record
#     """

#     id = common.generate_random(table)
#     record = [id, input_mod.name('Game title: ', 'Provide data to add'), input_mod.name('Manufacturer: ', ''),
#               input_mod.number('Price: ', ''), input_mod.number('In stock: ', '')]
#     table.append(record)
#     data_manager.write_table_to_file(file_name, table)
#     show_table(table)
#     return table


# # removes record from table
# def remove(table, id_):
#     """
#     Remove a record with a given id from the table.
#     Args:
#         table (list): table to remove a record from
#         id_ (str): id of a record to be removed
#     Returns:
#         list: Table without specified record.
#     """
#     show_table(table)
#     line_number = input_mod.number_with_terms('Line: ', 'Please provide number of line you want to remove',
#                                        range(1, (len(table) + 1)))
#     id_ = common.convert_input_to_id(table, line_number)
#     for line in table:
#         if line[0] == id_:
#             table.remove(line)
#     data_manager.write_table_to_file(file_name, table)
#     show_table(table)
#     return table


# # updates record in table
# def update(table, id_):
#     """
#     Updates specified record in the table. Ask users for new data.
#     Args:
#         table (list): list in which record should be updated
#         id_ (str): id of a record to update
#     Returns:
#         list: table with updated record
#     """

#     line_number = input_mod.number_with_terms('Line: ', 'Please provide number of line you want to update',
#                                        range(1, (len(table) + 1)))
#     id_ = common.convert_input_to_id(table, line_number)
#     line_data = input_mod.number_with_terms(details_update_list_labels, detail_update_title, range(1, 6))
#     new_record = input_mod.get_inputs(['New data: '], 'Please provide new data')[0]
#     # mam tu problem z wprowadzaniem nowych danych = powinno być to obudowane warunkami. ale nie wiem jak
#     for number, line in enumerate(table):
#         if line[0] == id_:
#             table[number][line_data] = new_record
#     data_manager.write_table_to_file(file_name, table)
#     show_table(table)
#     return table


# # Special functions
# # counts item by manufacturer
# def get_counts_by_manufacturers(table):
#     """
#     Question: How many different kinds of game are available of each manufacturer?
#     Args:
#         table (list): data table to work on
#     Returns:
#          dict: A dictionary with this structure: { [manufacturer] : [count] }
#     """

#     counted_games = {}
#     for item in table:
#         if item[manuf_index] in counted_games.keys():
#             counted_games[item[manuf_index]] += 1
#         else:
#             counted_games[item[manuf_index]] = 1
#     return counted_games


# # function for ERP - manufacturer is an input
# def get_average_by_manufacturerERP(table, manufacturer):
#     """
#     Question: What is the average amount of games in stock of a given manufacturer?
#     Args:
#         table (list): data table to work on
#         manufacturer (str): Name of manufacturer
#     Returns:
#          number
#     """

#     manufacturer = input_mod.name('Manufacturer: ', 'Provide name of manufacturer')
#     counted_manufacturer = 0
#     games_count = 0
#     for line in table:
#         if manufacturer in line[manuf_index]:
#             counted_manufacturer += 1
#             games_count += int(line[stock_index])
#     average = games_count/counted_manufacturer
#     return average


# # function for test
# def get_average_by_manufacturer(table, manufacturer):
#     """
#     Question: What is the average amount of games in stock of a given manufacturer?
#     Args:
#         table (list): data table to work on
#         manufacturer (str): Name of manufacturer
#     Returns:
#          number
#     """

#     counted_manufacturer = 0
#     games_count = 0
#     for line in table:
#         if manufacturer in line[manuf_index]:
#             counted_manufacturer += 1
#             games_count += int(line[stock_index])
#     average = games_count/counted_manufacturer
#     return average
>>>>>>> 70dc5e1ad3b6497a6ffbf929a562f34f72773525
