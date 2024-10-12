# from modules.functions import get_todos, write_todos
from modules import functions

while True:
    # Get user input and strip space chars
    user_action = input('Type add, show, edit, complete or exit: ')
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo.strip(' ').capitalize() + '\n')

        functions.write_todos(todos)

    elif user_action.startswith('show'):
        todos = functions.get_todos()

        # new_todos = [item.strip("\n") for item in todos]

        for index, x in enumerate(todos):
            print(f"{index + 1} - {x.title().rstrip()}")

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])

            todos = functions.get_todos()

            new_todo = input("Enter a new edited todo: ")
            todos[number - 1] = new_todo + '\n'
            # todos.__setitem__(number, new_todo)

            functions.write_todos(todos)

        except ValueError:
            print('Your command is invalid.')
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            todos = functions.get_todos()

            index = number - 1
            completed_todo = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todo {completed_todo} was completed and removed from the list."
            print(message)
        except IndexError:
            print('The number you chose is out of the range available in the todo list')
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print('Invalid command!')

print('Bye!')
