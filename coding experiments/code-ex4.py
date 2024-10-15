import FreeSimpleGUI as sg
from bonus_examples.converter14 import convert

sg.theme('Black')
label1 = sg.Text("Enter feet:")
input1 = sg.Input(key="feet")

label2 = sg.Text("Enter inches:")
input2 = sg.Input(key="inches")

convert_btn = sg.Button("Convert")
exit_btn = sg.Button("Exit")
output_label = sg.Text(key="output")

window = sg.Window("Convertor",
                   layout=[[label1, input1],
                           [label2, input2],
                           [convert_btn, exit_btn, output_label]])

while True:
    event, values = window.read()
    match event:
        case 'Convert':
            try:
                feet = float(values['feet'])
                inches = float(values['inches'])
                meters = convert(feet, inches)
                window['output'].update(value=f"You are {meters}m")
            except ValueError:
                sg.popup("Please provide the two numbers.")
        case 'Exit':
            break
        case sg.WIN_CLOSED:
            break

print("Bye")
window.close()