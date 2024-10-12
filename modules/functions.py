def get_todos(filepath="todos.txt"):
    """ Read a text file.
    Returns the to-dos list from the text file."""
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_local, filepath="todos.txt"):
    """Write or modify the to-do list from text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_local)


