import Controller
import View
import tkinter as tk

def refresh_table():
    View.Window.main_table.delete(*View.my_table.get_children())
    for person in Controller.contacts:
        data = [person[1], person[2], person[3], person[4]]
        View.my_table.insert('', tk.END, values=data)