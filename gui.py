import FreeSimpleGUI as sg
from modules import functions

label = sg.Text("Type a to-do item")
input_box = sg.InputText(tooltip="Enter todo...", key="todo")
add_btn = sg.Button("Add")

window = sg.Window("To-Do App",
                   layout=[[label], [input_box, add_btn]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo']
            todos.append(new_todo.strip(' ').capitalize() + '\n')
            functions.write_todos(todos)

        case sg.WIN_CLOSED:
            break

window.close()