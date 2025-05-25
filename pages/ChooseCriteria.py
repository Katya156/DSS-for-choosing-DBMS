import tkinter as tk
from data.vars import *
from pages.SelectCriteria import SelectCriteria
from pages.FillCriteriaOut import FillCriteriaOut
from pages.ShowResult import ShowResult
import os
import psycopg2
from dotenv import load_dotenv

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

class ChooseCriteria(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=MAINCOLOR)
        self.controller = controller

    def open_select_criteria(self, criteria_dict, enter_criteria_lst, criterion_name, task_id):
        # Открываем новое окно для выбора критерия
        select_criteria_window = SelectCriteria(self, criteria_dict, enter_criteria_lst, criterion_name, task_id)
        select_criteria_window.grab_set()  # Блокируем взаимодействие с родительским окном

    def set_method(self, method, criteria, criteria_out, criteria_in, task_id):
        self.task_id = task_id
        self.method = method

        print("Выбранный метод:", self.method)  # Для проверки
        print('ID задачи:', self.task_id)

        def check_entries(criteria_dict, key):
            # Проверяем, заполнены ли все поля Entry
            if [i.get() for i in criteria_dict.values()].count(1) >= 2:
                button1.config(state='normal')  # Активируем кнопку
            else:
                button1.config(state='disabled')  # Деактивируем кнопку
            if criteria_dict[key].get():
                self.open_select_criteria(criteria_dict, enter_criteria_lst, key, self.task_id)  # Открываем окно выбора для этого критерия

        def check_res(criteria_dict):
            res = {}
            out_criteria = []
            c = -1
            for i in criteria_dict:
                if criteria_dict[i].get() == 1:
                    res[i] = out_criteria[c]
                if i[3] == ' ':
                    out_criteria.append(i)
                    c += 1
            return res

        tk.Label(self, text='Выберите критерии (минимум 2)', font=LARGEFONT, bg=MAINCOLOR, fg=FONTCOLOR
                 ).grid(row=1, column=0, stick='n', columnspan = 2)


        criteria_lst = []
        cursor.execute('''select distinct id, criteria_name from criteria order by id''')
        rows = cursor.fetchall()
        for i in rows:
            name = i[1]
            criteria_lst.append(name)

        enter_criteria_lst = ['К5.1.', 'К8.2.', "К7.3.", "К8.1.", 'К7.2.']
        criteria_dict = {key: tk.IntVar() for key in criteria_lst}
        f, col, row = 0, 0, 2
        for i in criteria_dict:
            key = i
            if f == len(criteria_dict) // 2:
                row = 2
                col += 1
            if i[3] != ' ':
                ch = tk.Checkbutton(self, text=i, variable=criteria_dict[i],
                                    bg=MAINCOLOR, command = lambda key=key: check_entries(criteria_dict, key))
                ch.grid(row=row, column=col, stick="w", padx = (80,0))
                # ch.bind("<ButtonRelease>", lambda e, key=key: check_entries(criteria_dict.values(), key))

            else:
                tk.Label(self, text=i, font = SMALLFONT, bg=MAINCOLOR, fg=FONTCOLOR,
                 ).grid(row=row, column=col, stick = 'w', padx = (80,0))
            row += 1
            f += 1
        if self.method == 'Метод анализa иерархий':
            button1 = tk.Button(self, text='Подтвердить', font=LARGEFONT, bg=BUTTONCOLOR, fg=FONTCOLOR,
                                activeforeground=BUTTONCOLOR, state='disabled',
                                command=lambda: self.controller.show_frame(FillCriteriaOut, task_id=self.task_id,
                                                                           method=self.method,
                                                                           criteria=check_res(criteria_dict)))
            button1.grid(row=18, column=0, stick='n', columnspan=2)

        elif self.method == 'Метод TOPSIS':
            button1 = tk.Button(self, text='Подтвердить', font=LARGEFONT, bg=BUTTONCOLOR, fg=FONTCOLOR,
                                activeforeground=BUTTONCOLOR, state='disabled',
                                command=lambda: self.controller.show_frame(ShowResult, task_id=self.task_id,
                                                                           method=self.method,
                                                                           criteria=check_res(criteria_dict)))
            button1.grid(row=18, column=0, stick='n', columnspan=2)

        for i in range(2):
            self.grid_columnconfigure(i, minsize=1050/2)
        for i in range(20):
            self.grid_rowconfigure(i, minsize=35)