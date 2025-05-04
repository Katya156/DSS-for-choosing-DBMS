import psycopg2
import tkinter as tk
import re
from info.vars import *
import pandas as pd
from tkinter import messagebox
from dotenv import load_dotenv
import os

# Загружаем данные из .env файла
load_dotenv()

# Подключаемся к базе
connection = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=""
)
# connection.set_client_encoding('WIN1252')
cursor = connection.cursor()

class SelectCriteria(tk.Toplevel):
    def __init__(self, parent, criteria_dict, enter_criteria_lst, criterion_name, task_id):
        tk.Toplevel.__init__(self, parent, bg=MAINCOLOR)

        if criterion_name.split()[0] not in enter_criteria_lst:
            is_entry = 0
        else:
            is_entry = 1
        def is_valid(newval):
            # проверка того, что вводится только цифры
            return (re.match("^[0-9.]*$", newval) is not None)

        def check_entries(entry, minimum_value = 0, maximum_value = 0, is_entry = 0):
            # Проверяем, заполнены ли все поля Entry
            if not is_entry:
                if [i.get() for i in entry.values()].count(1) >= 1:
                    bt.config(state='normal')
                else:
                    bt.config(state='disabled')
            else:
                if entry.get() and minimum_value <= float(entry.get()) <= maximum_value:
                    bt.config(state='normal')  # Активируем кнопку
                else:
                    if not entry.get():
                        messagebox.showerror("Ошибка", "Поле не должно быть пустым")
                    else:
                        messagebox.showerror("Ошибка", f"Значение должно быть в диапазоне от {minimum_value} до {maximum_value}")
                    bt.config(state='disabled')  # Деактивируем кнопку

        def get_results():

            cursor.execute(f"""select id
                                from criteria c
                                where criteria_name = '{criterion_name}'""")
            # Извлечение данных
            rows = cursor.fetchall()
            for i in rows:
                id_criteria = i[0]
            if is_entry == 0:
                res = pd.DataFrame([{'criteria_name': k, 'value': chosen_criteria_dict[k].get()} for k in chosen_criteria_dict])
                res = tuple(res[res.value == 1].criteria_name)
                for i in res:
                    cursor.execute(f"""insert into task_info(criteria_id, tasks_id, task_value, filling_date) values(
                                                                            {id_criteria}, {task_id}, '{i}', current_date)""")
                    connection.commit()
            else:
                if criterion_name.split()[0] in ['К5.1.', 'К7.2.', 'К8.2.']:
                    comp = '>'
                elif criterion_name.split()[0] in ['К7.3.', 'К8.1.']:
                    comp = '<'
                else:
                    comp = '='
                cursor.execute(f"""insert into task_info(criteria_id, tasks_id, task_value, filling_date, comparison) values(
                                                                {id_criteria}, {task_id}, '{entry.get()}', current_date, '{comp}')""")
                connection.commit()
            self.destroy()

        if is_entry == 0:
            tk.Label(self, text=f'Выберите значения критерия {criterion_name}',
                     font=LARGEFONT, bg=MAINCOLOR, fg=FONTCOLOR).grid(row=1, column=1, stick='n', columnspan = 2)


            cursor.execute(f"""select allowed_value 
                                from criteria c
                                    join criteria_allowed_values ca
                                        on c.id = ca.criteria_id
                                        and criteria_name = '{criterion_name}'""")
            # Извлечение данных
            rows = cursor.fetchall()
            # Обработка данных
            chosen_criteria_dict = {i[0]: tk.IntVar() for i in rows}
            row = 2
            column = 1
            for i in chosen_criteria_dict:
                ch = tk.Checkbutton(self, text=i, variable=chosen_criteria_dict[i],
                                    bg=MAINCOLOR,
                                    command=lambda: check_entries(chosen_criteria_dict, is_entry = 0)
                                    )
                if row == 13:
                    row = 2
                    column = 2
                ch.grid(row=row, column=column, stick="w")
                row += 1
        else:
            tk.Label(self, text=f'Введите значение критерия {criterion_name}',
                     font=LARGEFONT, bg=MAINCOLOR, fg=FONTCOLOR).grid(row=1, column=1, stick='n', columnspan = 2)
            if criterion_name.split()[0] in ['К5.1.', 'К7.2.', 'К8.2.']:
                text = 'минимальное'
            else:
                text = 'максимальное'

            tk.Label(self, text=f'Введите {text} подходящее значение критерия',
                     font=MIDFONT, bg=MAINCOLOR, fg=FONTCOLOR).grid(row=2, column=1, stick='n', columnspan=2)

            cursor.execute(f"""select minimum_value, maximum_value 
                                            from criteria c
                                            where criteria_name = '{criterion_name}'""")  # Замените your_table_name на имя вашей таблицы
            # Извлечение данных
            rows = cursor.fetchall()
            for i in rows:
                minimum_value, maximum_value = map(float, i)
            check = (self.register(is_valid), "%P")
            entry = tk.Entry(self, width=50, validate = 'key', validatecommand=check)
            # tk.Scale(self, from_= minimum_value, to= maximum_value, orient='horizontal', command=show_value)
            entry.grid(row=4, column=1, columnspan=2)
            entry.bind("<KeyRelease>", lambda e: check_entries(entry, minimum_value, maximum_value, 1))

        bt = tk.Button(self, text='Подтвердить', font=LARGEFONT, bg=BUTTONCOLOR, fg=FONTCOLOR,
                  state='disabled', activeforeground=BUTTONCOLOR, command=get_results)
        bt.grid(row=13, column = 1, stick='n', columnspan = 2)

        for i in range(4):
            self.grid_columnconfigure(i, minsize=100)
        for i in range(15):
            self.grid_rowconfigure(i, minsize=35)