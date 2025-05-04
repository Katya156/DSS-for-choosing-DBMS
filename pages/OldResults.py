import psycopg2
import tkinter as tk
from tkinter import ttk
from info.vars import *
from dotenv import load_dotenv
import os
from collections import defaultdict

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

class OldResults(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=MAINCOLOR)

        tk.Label(self, text='Выберите задачу', font=LARGEFONT, fg=FONTCOLOR, bg=MAINCOLOR, width=30, height=3
                 ).grid(row=0, column=1, columnspan=2)

        # --- СОЗДАЕМ отдельный фрейм для вывода результата ---
        self.result_frame = tk.Frame(self, bg=MAINCOLOR)
        self.result_frame.grid(row=3, column=0, columnspan=4)

        # --- Загружаем данные для комбобокса ---
        cursor.execute("""SELECT DISTINCT task_name
                          FROM results r
                          JOIN tasks t ON r.tasks_id = t.id""")
        row = cursor.fetchall()
        names = [i[0] for i in row]

        if names:
            combobox = ttk.Combobox(self, values=names, state="readonly", width=50)
            combobox.grid(row=1, column=1, columnspan=2, sticky='n')
            combobox.current(0)

            def get_result():
                # ОЧИЩАЕМ фрейм от предыдущего вывода
                for widget in self.result_frame.winfo_children():
                    widget.destroy()

                # Дальше твой вывод результатов
                tk.Label(self.result_frame, text='Результат ранжирования', font=LARGEFONT,
                         fg=FONTCOLOR, bg=MAINCOLOR, width=30, height=3
                         ).grid(row=0, column=2, columnspan=2)

                tk.Label(self.result_frame, text='Информация о задаче', font=LARGEFONT,
                         fg=FONTCOLOR, bg=MAINCOLOR, width=30, height=3
                         ).grid(row=0, column=0, columnspan=2)

                # Твои запросы и отображение информации...
                cursor.execute(f"""SELECT dv.version_name, r.dbms_weight
                                   FROM results r
                                   JOIN tasks t ON r.tasks_id = t.id AND task_name = '{combobox.get()}'
                                   JOIN dbms_versions dv ON r.dbms_version_id = dv.id
                                   ORDER BY dbms_weight DESC""")
                row = cursor.fetchall()
                res = {i[0]: float(i[1]) for i in row}

                cursor.execute(f"""SELECT criteria_name, selected_method, task_value
                                   FROM tasks t
                                   JOIN task_info ti ON ti.tasks_id = t.id AND task_name = '{combobox.get()}'
                                   JOIN criteria c ON c.id = ti.criteria_id""")
                rows = cursor.fetchall()

                grouped_data = defaultdict(list)
                for criterion, method, value in rows:
                    grouped_data[criterion].append(value)

                tk.Label(self.result_frame, text=f"Метод ранжирования - {method}", font=SMALLFONT,
                         fg=FONTCOLOR, bg=MAINCOLOR
                         ).grid(row=1, column=0, sticky='n', columnspan=2)

                start = 2
                for criterion, values in grouped_data.items():
                    tk.Label(self.result_frame, text=f"{criterion} — {', '.join(values)}", font=SMALLFONT,
                             fg=FONTCOLOR, bg=MAINCOLOR
                             ).grid(row=start, column=0, sticky='n', columnspan=2)
                    start += 1

                start = 1
                cnt = 1
                for i in res:
                    tk.Label(self.result_frame, text=f'{cnt}. {i}, вес - {res[i]}', font=SMALLFONT,
                             fg=FONTCOLOR, bg=MAINCOLOR
                             ).grid(row=start, column=2, sticky='n', columnspan=2)
                    start += 1
                    cnt += 1

            # При нажатии кнопки
            tk.Button(self, text='Подтвердить', font=LARGEFONT, bg=BUTTONCOLOR, fg=FONTCOLOR,
                      activeforeground=BUTTONCOLOR, command=get_result).grid(row=2, column=1, columnspan=2, sticky='n')

        else:
            tk.Label(self, text='Старых задач не найдено', font=LARGEFONT, fg=FONTCOLOR, bg=MAINCOLOR,
                     width=30, height=3).grid(row=2, column=1, columnspan=2)

        for i in range(4):
            self.grid_columnconfigure(i, minsize=1050/4)
        for i in range(10):
            self.grid_rowconfigure(i, minsize=70)