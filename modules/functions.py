FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file.
    Returns the to-dos list from the text file."""
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_local, filepath=FILEPATH):
    """Write or modify the to-do list from text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_local)


if __name__ == "__main__":
    print(get_todos("../todos.txt"))