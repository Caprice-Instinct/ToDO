import FreeSimpleGUI as sg
from bonus_examples.converter14 import convert

label1 = sg.Text("Enter feet:")
input1 = sg.Input(key="feet")

label2 = sg.Text("Enter inches:")
input2 = sg.Input(key="inches")

convert_btn = sg.Button("Convert")
output_label = sg.Text(key="output")

window = sg.Window("Convertor",
                   layout=[[label1, input1],
                           [label2, input2],
                           [convert_btn, output_label]])

while True:
    event, values = window.read()
    feet = float(values['feet'])
    inches = float(values['inches'])
    meters = convert(feet, inches)
    window['output'].update(value=f"You are {meters}m")
print("Bye")
window.close()