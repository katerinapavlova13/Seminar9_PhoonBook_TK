from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import messagebox as mb
import Model
import Window, Topwindow

def new_table():
    Window.main_table.delete(*Window.main_table.get_children())
    for row in Model.my_phonebook.show_all():
        Window.main_table.insert('', 0, values=row)

def change_contact(ID: int):
    contact = Window.main_table.item(ID).get('values')
    Topwindow.createChangeWindow(contact)

def delete_contact(ID: int):
    contact = Window.main_table.item(ID).get('values')
    if mb.askyesno('Удаление', f'Вы точно хотите удалить контакт {contact[1]}?'):
        Model.my_phonebook.remove(str(contact[0]))
        new_table()

def open_file():
    types = (("Текстовый файл", "*.txt"),)
    full_file_name = askopenfilename(title='Открыть....', filetypes=types)
    Model.my_phonebook.clear()
    with open(full_file_name, 'r', encoding='UTF-8') as file:
        for line in file.readlines():
            contact = line.replace('\n', '').replace("'", "").replace('"', '').split(', ')
            Model.my_phonebook.add(contact[1], contact[2], contact[3], contact[4], contact[0])
    new_table()

def save_file():
    global main_table
    types = (("Текстовый файл", "*.txt"),)
    full_file_name = asksaveasfilename(title='Сохранить как...', filetypes=types, initialfile='phonebook.txt')
    with open(full_file_name, 'w', encoding='UTF-8') as file:
        data = ''
        for contact in Model.my_phonebook.show_all():
            data += str(contact)[1:-1] + '\n'
        file.write(data)