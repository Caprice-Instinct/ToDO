import FreeSimpleGUI as sg
from zip_creator import make_archive

label1 = sg.Text("Select files for compression: ")
input1 = sg.Input()
choose_btn1 = sg.FilesBrowse("Choose", key="files")

label2 = sg.Text("Choose Destination folder: ")
input2 = sg.Input()
choose_btn2 = sg.FolderBrowse("Choose", key="folder")

compress_btn = sg.Button("Compress")
output_label = sg.Text(key="result", text_color="red")

window = sg.Window("File Compressor",
                   layout=[[label1, input1, choose_btn1],
                           [label2, input2, choose_btn2],
                           [compress_btn, output_label]])

while True:
    event, values = window.read()
    print(event)
    print(values)
    filepaths = values['files'].split(";")
    folder = values['folder']
    make_archive(filepaths, folder)
    window['result'].update(value="Compression completed successfully!")

window.close()