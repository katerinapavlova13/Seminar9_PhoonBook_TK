import tkinter as tk
from tkinter import ttk

import Controller
import Size, Topwindow

window: tk.Tk
main_label: tk.Label
add_entry: []
main_table: ttk.Treeview

def main():
    global window
    global main_table

    window = tk.Tk()
    window.title('Телефонный справочник')
    window.geometry(Size.window_geometry(window, Size.window_width, Size.window_height))
    window.resizable(False, False)
    photo = tk.PhotoImage(file='book.png')
    window.iconphoto(False, photo)
    window.wm_attributes("-topmost", 1)

    menu_bar = tk.Menu(window, tearoff=0)
    window.config(menu=menu_bar)
    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label='Открыть', command=Controller.open_file)
    file_menu.add_command(label='Сохранить как...', command=Controller.save_as_file)
    file_menu.add_separator()
    file_menu.add_command(label='Выйти', command=window.destroy)
    menu_bar.add_cascade(label='Меню', menu=file_menu)

    main_table = ttk.Treeview(window, show='headings')
    heads = ['id', 'Имя', 'Фамилия', 'Телефон', 'Комментарий']
    main_table['columns'] = heads
    for header in heads:
        main_table.heading(header, text=header, anchor='w')
    main_table.column("#1", width=Size.id_column_width)
    main_table.column('#2', width=Size.column_width)
    main_table.column("#3", width=Size.column_width)
    main_table.column("#4", width=Size.column_width)
    main_table.column("#5", width=Size.column_width)
    main_table.bind('<Button-3>', right_button_menu)

    main_table.pack()

    add_button = tk.Button(window, text='Добавить контакт', command=open_window)
    add_button.pack()

    window.mainloop()

def open_window():
    Topwindow.createAddWindow()

def right_button_menu(event):
    global window
    global main_table

    popup_menu = tk.Menu(window, tearoff=0)
    rowID = event.widget.identify('item', event.x, event.y)
    event.widget.focus()
    file_menu = tk.Menu(popup_menu, tearoff=0)
    file_menu.add_command(label='Изменить контакт', command=lambda: Controller.change_contact(rowID))
    file_menu.add_command(label='Удалить контакт', command=lambda: Controller.delete_contact(rowID))
    file_menu.post(event.x_root, event.y_root)