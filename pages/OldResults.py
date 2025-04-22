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
    password=os.getenv("DB_PASS")
)

cursor = connection.cursor()

class OldResults(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=MAINCOLOR)

        tk.Label(self, text='Выберите задачу', font=LARGEFONT, fg=FONTCOLOR, bg=MAINCOLOR, width=30, height=3
                 ).grid(row=0, column=1, columnspan=2)

        cursor.execute("""select distinct task_name
                                      from results r
                                        join tasks t
                                            on r.tasks_id = t.id""")
        row = cursor.fetchall()
        names = []
        for i in row:
            name = i[0]
            names.append(name)

        if names:

            combobox = ttk.Combobox(self, values=names, state="readonly", width = 50)
            combobox.grid(row=1, column=1, columnspan=2, sticky='n')
            combobox.current(0)

            def get_result():

                tk.Label(self, text='Результат ранжирования', font=LARGEFONT, fg=FONTCOLOR, bg=MAINCOLOR, width=30, height=3
                         ).grid(row=3, column=2, columnspan=2)

                tk.Label(self, text='Информация о задаче', font=LARGEFONT, fg=FONTCOLOR, bg=MAINCOLOR, width=30,
                         height=3
                         ).grid(row=3, column=0, columnspan=2)

                cursor.execute(f"""select dv.version_name, r.dbms_weight
                                    from results r
                                        join tasks t
                                            on r.tasks_id = t.id
                                            and task_name = '{combobox.get()}'
                                        join dbms_versions dv
                                            on r.dbms_version_id = dv.id
                                    order by dbms_weight desc""")
                row = cursor.fetchall()
                res = {}
                for i in row:
                    name = i[0]
                    weight = i[1]
                    res[name] = float(weight)

                cursor.execute(f"""select criteria_name, selected_method, task_value
                                    from tasks t
                                        join task_info ti
                                           on ti.tasks_id = t.id
                                           and task_name = '{combobox.get()}'
                                        join criteria c
                                            on c.id = ti.criteria_id""")
                rows = cursor.fetchall()
                grouped_data = defaultdict(list)
                for row in rows:
                    criterion, method, value = row
                    grouped_data[criterion].append(value)

                # Вывод результата
                tk.Label(self, text=f"Метод ранжирования - {method}", font=SMALLFONT, fg=FONTCOLOR,
                         bg=MAINCOLOR
                         ).grid(row=4, column=0, sticky='n', columnspan=2)
                start = 5
                for criterion, values in grouped_data.items():
                    tk.Label(self, text=f"{criterion} — {', '.join(values)}", font=SMALLFONT, fg=FONTCOLOR,
                             bg=MAINCOLOR
                             ).grid(row=start, column=0, sticky='n', columnspan=2)
                    # print(f"{criterion} — {', '.join(values)}")
                    start += 1

                start = 4
                cnt = 1
                for i in res:
                    tk.Label(self, text=f'{cnt}. {i}, вес - {res[i]}', font=SMALLFONT, fg=FONTCOLOR,
                             bg=MAINCOLOR
                             ).grid(row=start, column=2, sticky='n', columnspan=2)
                    start += 1
                    cnt += 1

            tk.Button(self, text='Подтвердить', font=LARGEFONT, bg=BUTTONCOLOR, fg=FONTCOLOR, activeforeground=BUTTONCOLOR,
                      command=get_result).grid(row=2, column=1, columnspan=2, sticky= 'n')
        else:
            tk.Label(self, text='Старых задач не найдено', font=LARGEFONT, fg=FONTCOLOR, bg=MAINCOLOR, width=30, height=3
                     ).grid(row=2, column=1, columnspan=2)

        for i in range(4):
            self.grid_columnconfigure(i, minsize=1050/4)
        for i in range(10):
            self.grid_rowconfigure(i, minsize=70)