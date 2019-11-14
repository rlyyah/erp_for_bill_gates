""" User Interface (UI) module """
def find_longest_width(table, title_list):
    width_list = []
    for title in title_list:
        width_list.append(len(title))
    for line in table:
        for num, col in enumerate(line):
            if len(str(col)) > width_list[num]:
                width_list[num] = len(str(col))
    return width_list


def copy_table(table):
    copied_table = []
    copied_line = []
    ID_POSITION = 0
    
    for index, record in enumerate(table):
        copied_line = record[:]
        copied_line[ID_POSITION] = str(index+1)
        copied_table.append(copied_line)
    return copied_table


def print_table(table, title_list):
    """
    Prints table with data.
    Example:
        /-----------------------------------\
        |   id   |      title     |  type   |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/
    Args:
        table (list): list of lists - table to display
        title_list (list): list containing table headers
    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    print(table)
    table_copy = copy_table(table) 
    print(table)
    width_list = find_longest_width(table_copy, title_list)
    top = '-' * (sum(width_list)+len(width_list)*2+len(width_list)+1-2)
    spacer = top + 2 * '-' 
    print(f'/{top}\\')
    print('|', end='')
    for num, title in enumerate(title_list):
        print(f"{title.center(width_list[num]+2)}|", end='')
    print()
    print(spacer)
    for record in table_copy:
        print('|', end='')
        for col in range(len(record)):
            print(f"{str(record[col]).center(width_list[col]+2)}|", end='')
        if table_copy.index(record) == len(table_copy)-1:
            print()
            print(f'\\{top}/')
        else:
            print()
            print(spacer)    
        
    # your goes code bal balalsad
    # testing merging


def print_result(result, label):
    """
    Displays results of the special functions.

    Args:
        result: result of the special function (string, number, list or dict)
        label (str): label of the result

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your code


def print_menu(title, list_options, exit_message):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    print()
    print(title)
    for index, element in enumerate(list_options):
        print('    ({}) {}'.format(index + 1, element))
    print('    (0) {}'.format(exit_message))
    # your code


def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>

    Args:
        list_labels (list): labels of inputs
        title (string): title of the "input section"

    Returns:
        list: List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """
    print()
    print(title)
    inputs = []
    for label in list_labels:
        print(label)
        user_input = input()
        inputs.append(user_input)
    # print(inputs)
    return inputs


def print_error_message(message):
    """
    Displays an error message (example: ``Error: @message``)

    Args:
        message (str): error message to be displayed

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your code


def headline(head):
    headline = '\033[1;34;49m {}'.format(head)
    headline_alignment = headline.center(60)
    print(headline_alignment, '\033[0;37;49m ')
    # print('\033[0;37;49m ')


def print_enumerate_table(table):
    for i, item in enumerate(table, 1):
        print('{}. {}'.format(i, item))


def blank_line():
    print() 


def print_dictionary(dict):
    print(dict)