import FreeSimpleGUI as sg
from modules import functions

label = sg.Text("Type a to-do item")
input_box = sg.InputText(tooltip="Enter todo...", key="todo")
add_btn = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=[45, 10])

edit_btn = sg.Button("Edit")

window = sg.Window("To-Do App",
                   layout=[[label], [input_box, add_btn],
                           [list_box, edit_btn]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values['todos'])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo']
            todos.append(new_todo.strip(' ').capitalize() + '\n')
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + '\n'
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "todos":
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()