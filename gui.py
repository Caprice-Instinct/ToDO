import time
import FreeSimpleGUI as sg
from modules import functions
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", 'w') as file:
        pass

sg.theme("DarkBlue9")
clk_label = sg.Text('', key="clock")
label = sg.Text("Type a to-do item")
input_box = sg.InputText(tooltip="Enter todo...", key="todo")
add_btn = sg.Button('Add',
                    mouseover_colors="LightBlue2",
                    tooltip="Add to do", key="Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=[45, 10])

edit_btn = sg.Button("Edit")
complete_btn = sg.Button('Complete',key="Complete", tooltip="To complete a todo...",
                         mouseover_colors="LightBlue")

exit_btn = sg.Button("Exit")

window = sg.Window("To-Do App",
                   layout=[[clk_label],[label], [input_box, add_btn],
                           [list_box, edit_btn, complete_btn],
                           [exit_btn]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%Y-%m-%d %H:%M:%S %A"))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo']
            todos.append(new_todo.strip(' ').capitalize() + '\n')
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value="")

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + '\n'
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select a todo to edit.",
                         font=('Helvetica', 20))

        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")

            except IndexError:
                sg.popup("Please select a todo to complete.",
                         font=('Helvetica', 20))
        case "Exit":
            break
        case "todos":
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()