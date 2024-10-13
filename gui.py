import functions

import FreeSimpleGUI as sg

label = sg.Text("Type a to-do item")
input_box = sg.InputText(tooltip="Enter todo...")
add_btn = sg.Button("Add")

window = sg.Window("To-Do App", layout=[[label], [input_box, add_btn], []])
window.read()
window.close()