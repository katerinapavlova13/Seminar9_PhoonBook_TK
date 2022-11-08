import tkinter as tk
from tkinter import *
import Controller
import Size
from tkinter import messagebox, ttk, filedialog
from Add_contacts import Add_contacts
from tkinter.scrolledtext import ScrolledText


class Window:
    def __init__(self, width, height, title='Телефоная книга', resizable=(False, False)):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(Size.window_geometry(self.root,width, height))
        self.root.resizable(resizable[0], resizable[1])
        photo = tk.PhotoImage(file='book.png')
        self.root.iconphoto(False, photo)

        # self.text = ScrolledText(self.root)
        self.main_table = ttk.Treeview(self.root, show="headings")
        heads = ['Код', 'Имя', 'Фамилия', 'Телефон', 'Комментарий']
        self.main_table['columns'] = heads
        for header in heads:
            self.main_table.heading(header, text=header, anchor='w')
        self.main_table.column("#1", stretch=NO, width=Size.id_colums_width)
        self.main_table.column('#2', stretch=NO, width=Size.column_width)
        self.main_table.column("#3", stretch=NO, width=Size.column_width)
        self.main_table.column("#4", stretch=NO, width=Size.column_width)
        self.main_table.column("#5", stretch=NO, width=Size.column_width)

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def create_add_contacts(self, resizable=(False, False), icon=None):
        Add_contacts(self.root, resizable, icon)

    def draw_widgets(self):
        self.draw_menu()
        # self.text.pack()
        self.main_table.pack()

    def draw_menu(self):
        menu_bar = Menu(self.root)

        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label='Открыть', command=self.open_file)
        file_menu.add_command(label='Добавить', command=self.open_window)
        file_menu.add_command(label='Сохранить как...', command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label='Выйти', command=self.exit)
        info_menu = Menu(menu_bar, tearoff=0)
        info_menu.add_command(label='О приложение', command=self.show_info)

        menu_bar.add_cascade(label='Главное меню', menu=file_menu)
        menu_bar.add_cascade(label='Спарвка', menu=info_menu)
        self.root.configure(menu=menu_bar)

    def open_window(self):
        Add_contacts.save_contact()

    def open_file(self):
        # file_name = filedialog.askopenfilename(title='Открыть...')
        file_name = Controller.path
        if file_name:
            with open(file_name, 'r', encoding='UTF_8') as f:
                self.main_table.insert(END, f.read())

    def save_file(self):
        name = filedialog.asksaveasfilename()
        if name:
            with open(name, 'r', encoding='UTF_8') as f:
                f.write()

    def show_info(self):
        messagebox.showinfo("Информация", "Лучшее графическое приложение")

    def exit(self):
        choice = messagebox.askyesno('Выход из приложения', 'Вы точно хотите выйти?')
        if choice:
            self.root.destroy()

if __name__ == '__main__':
    window = Window(480, 250, 'Телефоная книга')
    # window.create_add_contacts(340, 150)
    window.run()


# columns = ("name", 'surname', "phone", "comments")
# my_table = ttk.Treeview(columns=columns, show="headings")
# my_table.place(x=5, y=5)

# tab_control = ttk.Notebook(window)
#
# # tabl1 = ttk.Frame(tab_control)
# # tab_control.add(tabl1, text='Добавить контакт')
# # tab_control.pack(expand=1, fill='both')
