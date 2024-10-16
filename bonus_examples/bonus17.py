import FreeSimpleGUI as sg
from zip_extractor import extract_archive


sg.theme('Black')
label1 = sg.Text("Select archive: ")
input1 = sg.Input(key="zipfile")
choose_btn1 = sg.FileBrowse("Choose", key='archive')

label2 = sg.Text("Select destination: ")
input2 = sg.Input(key="dest_folder")
choose_btn2 = sg.FolderBrowse("Choose", key='folder')

extract_btn = sg.Button("Extract", key='Extract')
output_label = sg.Text(key='Output')


window = sg.Window("Archive Extractor",
                   layout=[[label1, input1, choose_btn1],
                           [label2, input2, choose_btn2],
                           [extract_btn, output_label]])

while True:
    event, values = window.read()
    print(event, values)
    archive_path = values['archive']
    dest_folder = values['dest_folder']
    extract_archive(archive_path, dest_folder)
    window['Output'].update(value="Extraction completed!")

window.close()