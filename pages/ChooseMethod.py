import psycopg2
import tkinter as tk
from info.vars import *
from pages.ChooseCriteria import ChooseCriteria
from dotenv import load_dotenv
from tkinter import messagebox
import os

# Загружаем данные из .env файла
load_dotenv()

# Подключаемся к базе
connection = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS")
)

cursor = connection.cursor()

class ChooseMethod(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=MAINCOLOR)

        def check_entries(entry):
            # Проверяем, заполнены ли все поля Entry
            cursor.execute(f"select distinct task_name from tasks")
            rows = cursor.fetchall()
            names = []
            for i in rows:
                name = i[0]
                names.append(name)
            if entry.get() and entry.get() not in names:
                bt.config(state='normal')  # Активируем кнопку
            else:
                if entry.get() in names:
                    messagebox.showerror("Ошибка", "Такое название задачи уже существует")
                bt.config(state='disabled')  # Деактивируем кнопку

        def insert_task_name(entry, selected_var, scale):
            # тут записываю название задачи в бд
            cursor.execute(f"""insert into tasks(task_name, threshold_task, selected_method, filling_date) values(
                                          '{entry.get()}', {scale.get()}, '{selected_var.get()}', current_date)""")
            connection.commit()
            cursor.execute(f"""select id from tasks where task_name = '{entry.get()}'""")
            rows = cursor.fetchall()
            for i in rows:
                id = i[0]
            return id

        tk.Label(self, text='Введите название вашей задачи', font=LARGEFONT, bg=MAINCOLOR, fg=FONTCOLOR
                 ).grid(row=1, column=0, columnspan=3, stick='n')

        entry = tk.Entry(self, width=50)
        entry.grid(row=3, column=1)
        entry.bind("<KeyRelease>", lambda e: check_entries(entry))

        tk.Label(self, text='Выберите метод ранжирования', font=LARGEFONT, bg=MAINCOLOR, fg=FONTCOLOR,
                 ).grid(row=5, column=0, columnspan=3, stick='n')

        selected_var = tk.StringVar(value='Метод анализa иерархий')

        tk.Radiobutton(self, text="Метод анализa иерархий", variable=selected_var, value='Метод анализa иерархий',
            font=MIDFONT, bg=MAINCOLOR).grid(row=7, column=1, stick="w")

        tk.Radiobutton(self, text="Метод TOPSIS", variable=selected_var, value='Метод TOPSIS',
            font=MIDFONT, bg=MAINCOLOR).grid(row = 8, column=1, stick="w")

        tk.Label(self, text='Выберите максимальное количество выводимых СУБД', font=LARGEFONT, bg=MAINCOLOR, fg=FONTCOLOR
                 ).grid(row=10, column=0, columnspan=3, stick='n')

        scale = tk.Scale(self, from_= 1, to = 10, orient='horizontal', resolution=1, bg=MAINCOLOR)

        scale.grid(row=11, column=0, columnspan=3, stick='n')

        bt = tk.Button(self, text='Подтвердить', font=MIDFONT, bg=BUTTONCOLOR, fg=FONTCOLOR, activeforeground=BUTTONCOLOR,
                  state='disabled', command=lambda: controller.show_frame(ChooseCriteria,
                                                                          task_id = insert_task_name(entry, selected_var, scale),
                                                                          method = selected_var.get()))
        bt.grid(row=12, column=1, stick='n')

        for i in range(3):
            self.grid_columnconfigure(i, minsize=350)
        for i in range(14):
            self.grid_rowconfigure(i, minsize=50)