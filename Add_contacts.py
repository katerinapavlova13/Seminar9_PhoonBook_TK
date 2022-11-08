from tkinter import *
import tkinter as tk
import Controller
import Size


class Add_contacts:
    def __init__(self, parent, width, height, title='Добавить контакт', resizable=(False, False)):
        self.root = Toplevel(parent)
        self.root.title(title)
        self.root.geometry(Size.window_geometry(self.root, width, height))
        self.root.resizable(resizable[0], resizable[1])
        photo = tk.PhotoImage(file='book.png')
        self.root.iconphoto(False, photo)
        self.grab_focus()


    def save_contact(self):
        id_lbl = tk.Label(self.root, text='Код')
        name_lbl = tk.Label(self.root, text='Имя')
        surname_lbl = tk.Label(self.root, text='Фамилия')
        phone_lbl = tk.Label(self.root, text='Номер телефона')
        comment_lbl = tk.Label(self.root, text='Комментарий')

        id_lbl.grid(column=0, row=0, sticky='e')
        name_lbl.grid(column=0, row=1, sticky='e')
        surname_lbl.grid(column=0, row=2, sticky='e')
        phone_lbl.grid(column=0, row=3, sticky='e')
        comment_lbl.grid(column=0, row=4, sticky='e')

        add_entry = [tk.Entry(self.root, width=30) for _ in range(5)]
        for i, entry in enumerate(add_entry):
            add_entry[i].grid(column=1, row=i)

        add_button = tk.Button(self.root, text='Добавить', command=lambda: self.add_contact(add_entry))
        add_button.grid(columnspan=2, row=3)

    def add_contact(self, add_entry: list):
        Controller.path.add(add_entry[0].get(), add_entry[1].get(), add_entry[2].get())

    def grab_focus(self):
        # self.root.grab_set()
        self.root.focus_set()
        self.root.wait_window()


