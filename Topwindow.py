import tkinter as tk
import Controller, Model, Size

add_window: tk.Tk
change_contact: tk.Tk
add_entry: [] = []
change_entry: [] = []

def createAddWindow():
    global add_window
    global add_entry

    add_window = tk.Toplevel()
    add_window.title('Добавить контакт')
    add_window.geometry(Size.window_geometry(add_window, Size.width_add_cont, Size.height_add_cont))
    add_window.resizable(False, False)
    photo = tk.PhotoImage(file='book.png')
    add_window.iconphoto(False, photo)
    add_window.wm_attributes("-topmost", 1)

    add_window.columnconfigure(index=0, weight=50)
    add_window.columnconfigure(index=1, weight=250)

    name_label = tk.Label(add_window, text='Имя')
    surname_label = tk.Label(add_window, text='Фамилия')
    phone_label = tk.Label(add_window, text='Номер телефона')
    comment_label = tk.Label(add_window, text='Комментарий')
    name_label.grid(column=0, row=0, sticky='e')
    surname_label.grid(column=0, row=1, sticky='e')
    phone_label.grid(column=0, row=2, sticky='e')
    comment_label.grid(column=0, row=3, sticky='e')

    add_entry = [tk.Entry(add_window, width=30) for _ in range(4)]
    for i, entry in enumerate(add_entry):
        add_entry[i].grid(column=1, row=i)

    add_button = tk.Button(add_window, text='Добавить',
                           command=lambda: add_contact(add_entry))
    add_button.grid(columnspan=2, row=4)

    add_window.mainloop()

def add_contact(add_entry: list):
    global add_window

    Model.my_phonebook.add(add_entry[0].get(), add_entry[1].get(), add_entry[2].get(),
                           add_entry[3].get())
    Controller.new_table()
    add_window.destroy()

def add_change_contact(change_entry: list, contact: list):
    global change_contact

    Model.my_phonebook.set(contact[0], change_entry[0].get(), change_entry[1].get(),
                        change_entry[2].get(), change_entry[3].get())

    Controller.new_table()
    change_contact.destroy()

def createChangeWindow(contact: list):
    global change_contact
    global change_entry

    change_contact = tk.Toplevel()
    change_contact.title('Изменить контакт')
    change_contact.geometry(Size.window_geometry(change_contact, Size.width_add_cont, Size.height_add_cont))
    change_contact.resizable(False, False)
    photo = tk.PhotoImage(file='book.png')
    change_contact.iconphoto(False, photo)
    change_contact.wm_attributes("-topmost", 1)

    change_contact.columnconfigure(index=0, weight=50)
    change_contact.columnconfigure(index=1, weight=250)

    surname_label = tk.Label(change_contact, text='Фамилия')
    name_label = tk.Label(change_contact, text='Имя')
    phone_label = tk.Label(change_contact, text='Телефон')
    comment_label = tk.Label(change_contact, text='Комментарий')

    surname_label.grid(column=0, row=0, sticky='e')
    name_label.grid(column=0, row=1, sticky='e')
    phone_label.grid(column=0, row=2, sticky='e')
    comment_label.grid(column=0, row=3, sticky='e')

    change_entry = [tk.Entry(change_contact, width=30) for _ in range(4)]
    for i, entry in enumerate(change_entry):
        change_entry[i].insert(0, contact[i+1])
        change_entry[i].grid(column=1, row=i)


    change_button = tk.Button(change_contact, text='Изменить', command=lambda: add_change_contact(change_entry, contact))
    change_button.grid(columnspan=2, row=4)

    change_contact.mainloop()