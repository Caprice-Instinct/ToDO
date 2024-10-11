while True:
    # Get user input and strip space chars
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if 'add' in user_action:
        todo = user_action[4:]

        with open("files/todos.txt", 'r') as file:
            todos = file.readlines()

        todos.append(todo.strip(" ").capitalize())

        with open("files/todos.txt", 'w') as file:
            file.writelines(todos)

    elif 'show' in user_action:
        with open("files/todos.txt", 'r') as file:
            todos = file.readlines()

        # new_todos = [item.strip("\n") for item in todos]

        for index, x in enumerate(todos):
            print(f"{index + 1}-{x.title().strip("\n")}")

    elif 'edit' in user_action:
        number = int(user_action[5:])

        with open("files/todos.txt", 'r') as file:
            todos = file.readlines()

        new_todo = input("Enter a new edited todo: ")
        todos[number - 1] = new_todo + '\n'
        # todos.__setitem__(number, new_todo)

        with open("files/todos.txt", 'w') as file:
            file.writelines(todos)

    elif 'complete' in user_action:
        number = int(user_action[9:])
        with open("files/todos.txt", 'r') as file:
            todos = file.readlines()

        index = number - 1
        completed_todo = todos[index].strip('\n')
        todos.pop(index)

        with open("files/todos.txt", 'w') as file:
            file.writelines(todos)

        message = f"Todo {completed_todo} was completed and removed from the list."
        print(message)

    elif 'exit' in user_action:
        break

    else:
        print("Invalid command!")

print("Bye!")
