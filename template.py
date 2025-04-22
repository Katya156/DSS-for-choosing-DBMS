# class tkinterApp:
#     """
#      Создается окно в котором мы будем работать и выстраиваются все параметры
#     """
#     root = tk.Tk()
#     root.title('СППР для выбора СУБД')
#     root.geometry('1050x700+100+50')
#     root.resizable(False, True)
#     root.config(bg=MAINCOLOR)
#     photo = tk.PhotoImage(file = "./icon.png")
#     root.iconphoto(False, photo)
#
#     def __init__(self):
#         container = tk.Frame(tkinterApp.root)
#         container.pack()
#
#         container.grid_rowconfigure(0, weight = 1, minsize = 750)
#         container.grid_columnconfigure(0, weight = 1,  minsize = 1050)
#
#         self.frames = {}
#         for F in (StartPage, OldResults, ChooseMethod, ChooseCriteria, FillCriteriaOut, FillCriteriaIn, ShowResult):
#             frame = F(container, self)
#             self.frames[F] = frame
#             frame.grid(row = 0, column = 0, sticky ="n")
#         self.show_frame(StartPage)
#         tkinterApp.root.mainloop()
#
#     def show_frame(self, cont, method = None, criteria = None, criteria_out = None, criteria_in = None, task_name = None):
#         frame = self.frames[cont]
#         if method is not None or criteria is not None:
#             frame.set_method(method, criteria, criteria_out, criteria_in, task_name)  # Передаем результаты в фрейм
#         #     эту функцию нужно сделать в каждом классе который должен что-то принимать от пред окна
#         frame.tkraise()
#
#
# class StartPage(tk.Frame):
#     """
#      Данное поле открывается когда программа начинает работать
#     """
#     def __init__(self, parent, controller):
#
#         tk.Frame.__init__(self, parent,  bg = MAINCOLOR)
#
#         tk.Label(self, text ="СППР для выбора СУБД", font = LARGEFONT, bg =MAINCOLOR, fg = FONTCOLOR
#                  ).grid(row = 1, column = 1, padx = 10, pady = 10)
#
#         main_menu = ['Выбрать СУБД', 'Поcмотреть старые результаты']
#
#         tk.Button(self, text=main_menu[0], font=LARGEFONT, bg=BUTTONCOLOR, fg=FONTCOLOR,
#                   activeforeground=BUTTONCOLOR, command=lambda: controller.show_frame(ChooseMethod)
#                   ).grid(row=3, column=1, stick='snwe')
#
#         tk.Button(self, text=main_menu[1], font=LARGEFONT, bg=BUTTONCOLOR, fg=FONTCOLOR,
#                   activeforeground=BUTTONCOLOR, command=lambda: controller.show_frame(OldResults)
#                   ).grid(row=4, column=1, stick='snwe')
#
#         for i in range(3):
#             self.grid_columnconfigure(i, minsize=350)
#         for i in range(7):
#             self.grid_rowconfigure(i, minsize=100)
#
#
# class OldResults(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent, bg=MAINCOLOR)
#
#         # tk.Label(self, text='Выберите задачу', font=LARGEFONT, fg=FONTCOLOR, bg=MAINCOLOR, width=30, height=3).grid(row=1, column=1)
#         #
#         # tk.Button(self, text='Подтвердить', font=LARGEFONT, bg=BUTTONCOLOR, fg=FONTCOLOR, activeforeground=BUTTONCOLOR,
#         #           command=lambda: controller.show_frame(FillCriteria)).grid(row=6, column=1, stick='nw')
#         # tk.Button(self, text='Назад', font=LARGEFONT, bg=BUTTONCOLOR, fg=FONTCOLOR, activeforeground=BUTTONCOLOR,
#         #           command=lambda: controller.show_frame(StartPage)).grid(row=6, column=1, stick='ne')
#
#         for i in range(3):
#             self.grid_columnconfigure(i, minsize=350)
#         for i in range(7):
#             self.grid_rowconfigure(i, minsize=100)
#
# class ChooseMethod(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent, bg=MAINCOLOR)
#
#         def check_entries(entry):
#             # Проверяем, заполнены ли все поля Entry
#             if entry.get():
#                 bt.config(state='normal')  # Активируем кнопку
#             else:
#                 bt.config(state='disabled')  # Деактивируем кнопку
#         def insert_task_name(entry):
#             # тут записываю название задачи в бд
#             cursor.execute(f"insert into tasks(task_name, filling_date) values('{entry.get()}', current_date)")
#             connection.commit()
#             return entry.get()
#
#         tk.Label(self, text='Введите название вашей задачи', font=MIDFONT, bg=MAINCOLOR, fg=FONTCOLOR, width=30,
#                  height=3).grid(row=1, column=1, stick='n')
#
#         entry = tk.Entry(self, width=50)
#         entry.grid(row=3, column=1)
#         entry.bind("<KeyRelease>", lambda e: check_entries(entry))
#
#         tk.Label(self, text='Выберите метод ранжирования', font=MIDFONT, bg=MAINCOLOR, fg=FONTCOLOR, width=30, height=3
#                  ).grid(row=6, column=1, stick='n')
#
#         selected_var = tk.StringVar(value='Метод анализa иерархий')
#
#         tk.Radiobutton(self, text="Метод анализa иерархий", variable=selected_var, value='Метод анализa иерархий',
#             font=MIDFONT, bg=MAINCOLOR).grid(row=8, column=1, stick="w")
#
#         tk.Radiobutton(self, text="Метод TOPSIS", variable=selected_var, value='Метод TOPSIS',
#             font=MIDFONT, bg=MAINCOLOR).grid(row = 9, column=1, stick="w")
#
#         bt = tk.Button(self, text='Подтвердить', font=MIDFONT, bg=BUTTONCOLOR, fg=FONTCOLOR, activeforeground=BUTTONCOLOR,
#                   state='disabled', command=lambda: controller.show_frame(ChooseCriteria, task_name = insert_task_name(entry),
#                                                                           method = selected_var.get()))
#         bt.grid(row=11, column=1, stick='nw')
#
#         tk.Button(self, text='Назад', font=MIDFONT, bg=BUTTONCOLOR, fg=FONTCOLOR, activeforeground=BUTTONCOLOR,
#                   command=lambda: controller.show_frame(StartPage)).grid(row=11, column=1, stick='ne')
#
#         for i in range(3):
#             self.grid_columnconfigure(i, minsize=350)
#         for i in range(14):
#             self.grid_rowconfigure(i, minsize=50)
#
#
# class ChooseCriteria(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent, bg=MAINCOLOR)
#         self.controller = controller
#
#     def open_select_criteria(self, criteria_dict, enter_criteria_lst, criterion_name, task_name):
#         # Открываем новое окно для выбора критерия
#         select_criteria_window = SelectCriteria(self, criteria_dict, enter_criteria_lst, criterion_name, task_name)
#         select_criteria_window.grab_set()  # Блокируем взаимодействие с родительским окном
#
#     def set_method(self, method, criteria, criteria_out, criteria_in, task_name):
#         self.task_name = task_name
#         self.method = method
#
#         print("Выбранный метод:", self.method)  # Для проверки
#         print('Название задачи:', self.task_name)
#
#         def check_entries(criteria_dict, key):
#             # Проверяем, заполнены ли все поля Entry
#             if [i.get() for i in criteria_dict.values()].count(1) >= 2:
#                 button1.config(state='normal')  # Активируем кнопку
#             else:
#                 button1.config(state='disabled')  # Деактивируем кнопку
#             self.open_select_criteria(criteria_dict, enter_criteria_lst, key, self.task_name)  # Открываем окно выбора для этого критерия
#
#         def check_res(criteria_dict):
#             res = {}
#             out_criteria = []
#             c = -1
#             for i in criteria_dict:
#                 if criteria_dict[i].get() == 1:
#                     res[i] = out_criteria[c]
#                 if i[3] == ' ':
#                     out_criteria.append(i)
#                     c += 1
#             return res
#
#         tk.Label(self, text='Выберите критерии (минимум 2)', font=MIDFONT, bg=MAINCOLOR, fg=FONTCOLOR
#                  ).grid(row=1, column=1, stick='n', columnspan = 2)
#
#         # чтение названия критериев
#         with open('criteria.txt', 'r', encoding = 'utf-8') as f:
#             criteria_lst = []
#             for i in f:
#                 criteria_lst.append(i.strip())
#
#         enter_criteria_lst = ['К5.1.', 'К8.2.', "К7.3.", "К8.1.", 'К7.2.']
#         criteria_dict = {key: tk.IntVar() for key in criteria_lst}
#         f, col, row = 0, 1, 2
#         for i in criteria_dict:
#             key = i
#             if f == len(criteria_dict) // 2:
#                 row = 2
#                 col += 1
#             if i[3] != ' ':
#                 ch = tk.Checkbutton(self, text=i, variable=criteria_dict[i],
#                                     bg=MAINCOLOR, command = lambda key=key: check_entries(criteria_dict, key))
#                 ch.grid(row=row, column=col, stick="w")
#                 # ch.bind("<ButtonRelease>", lambda e, key=key: check_entries(criteria_dict.values(), key))
#
#             else:
#                 tk.Label(self, text=i, font = SMALLFONT, bg=MAINCOLOR, fg=FONTCOLOR,
#                  ).grid(row=row, column=col, stick = 'w')
#             row += 1
#             f += 1
#         if self.method == 'Метод анализa иерархий':
#             button1 = tk.Button(self, text='Подтвердить', font=LARGEFONT, bg=BUTTONCOLOR, fg=FONTCOLOR,
#                                 activeforeground=BUTTONCOLOR, state='disabled',
#                                 command=lambda: self.controller.show_frame(FillCriteriaOut, task_name=self.task_name,
#                                                                            method=self.method,
#                                                                            criteria=check_res(criteria_dict)))
#             button1.grid(row=18, column=1, stick='n')
#
#         elif self.method == 'Метод TOPSIS':
#             button1 = tk.Button(self, text='Подтвердить', font=LARGEFONT, bg=BUTTONCOLOR, fg=FONTCOLOR,
#                                 activeforeground=BUTTONCOLOR, state='disabled',
#                                 command=lambda: self.controller.show_frame(ShowResult, task_name=self.task_name,
#                                                                            method=self.method,
#                                                                            criteria=check_res(criteria_dict)))
#             button1.grid(row=18, column=1, stick='n')
#
#         tk.Button(self, text='Назад', font=LARGEFONT, bg=BUTTONCOLOR, fg=FONTCOLOR, activeforeground=BUTTONCOLOR,
#                   command=lambda: self.controller.show_frame(StartPage)).grid(row=18, column=2, stick='n')
#
#         for i in range(4):
#             self.grid_columnconfigure(i, minsize=262.5)
#         for i in range(20):
#             self.grid_rowconfigure(i, minsize=35)
#
#
# class SelectCriteria(tk.Toplevel):
#     def __init__(self, parent, criteria_dict, enter_criteria_lst, criterion_name, task_name):
#         tk.Toplevel.__init__(self, parent, bg=MAINCOLOR)
#
#         if criterion_name.split()[0] not in enter_criteria_lst:
#             is_entry = 0
#         else:
#             is_entry = 1
#         def is_valid(newval):
#             # проверка того, что вводятся только цифры
#             return (re.match("^[0-9.]*$", newval) is not None)
#
#         def check_entries(entry, minimum_value = 0, maximum_value = 0, is_entry = 0):
#             # Проверяем, заполнены ли все поля Entry
#             if not is_entry:
#                 if [i.get() for i in entry.values()].count(1) >= 1:
#                     bt.config(state='normal')
#                 else:
#                     bt.config(state='disabled')
#             else:
#                 if entry.get() and minimum_value <= float(entry.get()) <= maximum_value:
#                     bt.config(state='normal')  # Активируем кнопку
#                 else:
#                     if not entry.get():
#                         messagebox.showerror("Ошибка", "Поле не должно быть пустым")
#                     else:
#                         messagebox.showerror("Ошибка", f"Значение должно быть в диапазоне от {minimum_value} до {maximum_value}")
#                     bt.config(state='disabled')  # Деактивируем кнопку
#
#         def get_results():
#             cursor.execute(f"""select id
#                                 from tasks t
#                                 where task_name = '{task_name}'""")
#             # Извлечение данных
#             rows = cursor.fetchall()
#             for i in rows:
#                 id = i[0]
#
#             cursor.execute(f"""select id
#                                 from criteria c
#                                 where criteria_name = '{criterion_name}'""")
#             # Извлечение данных
#             rows = cursor.fetchall()
#             for i in rows:
#                 id_criteria = i[0]
#             if is_entry == 0:
#                 res = pd.DataFrame([{'criteria_name': k, 'value': chosen_criteria_dict[k].get()} for k in chosen_criteria_dict])
#                 res = tuple(res[res.value == 1].criteria_name)
#                 for i in res:
#                     cursor.execute(f"""insert into task_info(criteria_id, tasks_id, task_value, filling_date) values(
#                                                                             {id_criteria}, {id}, '{i}', current_date)""")
#                     connection.commit()
#             else:
#                 if criterion_name.split()[0] in ['К5.1.', 'К7.2.', 'К8.2.']:
#                     comp = '>'
#                 elif criterion_name.split()[0] in ['К7.3.', 'К8.1.']:
#                     comp = '<'
#                 else:
#                     comp = '='
#                 cursor.execute(f"""insert into task_info(criteria_id, tasks_id, task_value, filling_date, comparison) values(
#                                                                 {id_criteria}, {id}, '{entry.get()}', current_date, '{comp}')""")
#                 connection.commit()
#             self.destroy()
#
#         if is_entry == 0:
#             tk.Label(self, text=f'Выберите значения критерия {criterion_name}',
#                      font=LARGEFONT, bg=MAINCOLOR, fg=FONTCOLOR).grid(row=1, column=1, stick='n', columnspan = 2)
#
#
#             cursor.execute(f"""select allowed_value
#                                 from criteria c
#                                     join criteria_allowed_values ca
#                                         on c.id = ca.criteria_id
#                                         and criteria_name = '{criterion_name}'""")
#             # Извлечение данных
#             rows = cursor.fetchall()
#             # Обработка данных
#             chosen_criteria_dict = {i[0]: tk.IntVar() for i in rows}
#             row = 2
#             column = 1
#             for i in chosen_criteria_dict:
#                 ch = tk.Checkbutton(self, text=i, variable=chosen_criteria_dict[i],
#                                     bg=MAINCOLOR,
#                                     command=lambda: check_entries(chosen_criteria_dict, is_entry = 0)
#                                     )
#                 if row == 13:
#                     row = 2
#                     column = 2
#                 ch.grid(row=row, column=column, stick="w")
#                 row += 1
#         else:
#             tk.Label(self, text=f'Введите значение критерия {criterion_name}',
#                      font=LARGEFONT, bg=MAINCOLOR, fg=FONTCOLOR).grid(row=1, column=1, stick='n', columnspan = 2)
#             if criterion_name.split()[0] in ['К5.1.', 'К7.2.', 'К8.2.']:
#                 text = 'минимальное'
#             else:
#                 text = 'максимальное'
#
#             tk.Label(self, text=f'Введите {text} подходящее значение критерия',
#                      font=MIDFONT, bg=MAINCOLOR, fg=FONTCOLOR).grid(row=2, column=1, stick='n', columnspan=2)
#
#             cursor.execute(f"""select minimum_value, maximum_value
#                                             from criteria c
#                                             where criteria_name = '{criterion_name}'""")  # Замените your_table_name на имя вашей таблицы
#             # Извлечение данных
#             rows = cursor.fetchall()
#             for i in rows:
#                 minimum_value, maximum_value = map(float, i)
#             check = (self.register(is_valid), "%P")
#             entry = tk.Entry(self, width=50, validate = 'key', validatecommand=check)
#             # tk.Scale(self, from_= minimum_value, to= maximum_value, orient='horizontal', command=show_value)
#             entry.grid(row=3, column=1)
#             entry.bind("<KeyRelease>", lambda e: check_entries(entry, minimum_value, maximum_value, 1))
#
#         bt = tk.Button(self, text='Подтвердить', font=LARGEFONT, bg=BUTTONCOLOR, fg=FONTCOLOR,
#                   state='disabled', activeforeground=BUTTONCOLOR, command=get_results)
#         bt.grid(row=13, column = 1, stick='n', columnspan = 2)
#
#         for i in range(4):
#             self.grid_columnconfigure(i, minsize=100)
#         for i in range(15):
#             self.grid_rowconfigure(i, minsize=35)
#
#
# class FillCriteriaOut(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent, bg=MAINCOLOR)
#         self.controller = controller
#
#     def set_method(self, method, criteria, criteria_out, criteria_in, task_name):
#         self.method = method  # Сохраняем переданные результаты
#         self.criteria = criteria
#         self.task_name = task_name
#
#         print('Критерии:', self.criteria)
#
#         def is_valid(newval):
#             # проверка того, что вводится только цифры или /
#             result = re.match("^[13579/]*$", newval) is not None
#             return result
#
#         def check_entries(entries):
#             # Проверяем, заполнены ли все поля Entry
#             if all([i.get() for i in list(itertools.chain.from_iterable(entries))]):
#                 flg = 1
#                 # проверяем, правильно ли по диагонали все заполнено
#                 for i in range(len(entries)):
#                     for j in range(len(entries[i])):
#                         if entries[i][j].get() != '1':
#                             if (entries[i][j].get().replace('1/', '') != entries[j][i].get().replace('1/', ''))\
#                                     or ('/' not in entries[i][j].get() and '/' not in entries[j][i].get()):
#                                 flg = 0
#                                 break
#                 if flg == 1:
#                     button2.config(state='normal')  # Активируем кнопку
#             else:
#                 button2.config(state='disabled')  # Деактивируем кнопку
#
#         def return_result(entries):
#             res = {}
#             for i in range(len(entries)):
#                 for j in range(len(entries[i])):
#                     if i != j:  # пропускаем диагональ (там всегда 1)
#                         key = (s[i], s[j])  # названия критериев
#                         val = entries[i][j].get()
#                         if '/' in val:
#                             val = float(val[0]) / float(val[2])
#                         res[key] = val
#             return res
#
#         cnt_out = len(sorted(set(self.criteria.values())))
#
#         tk.Label(self, text='Введите степени важности критериев верхнего уровня', font=MIDFONT, fg=FONTCOLOR, bg=MAINCOLOR
#                  ).grid(row=0, column=0, columnspan=cnt_out + 2, sticky='nsew')
#         tk.Label(self, text='''Шкала относительной важности:
#                         1 – равная важность, 3(1/3) – умеренное превосходство, 5(1/5) – существенное превосходство,
#                         7(1/7) – значительное превосходство, 9(1/9) – очень большое превосходство''',
#                  font=SMALLFONT, fg=FONTCOLOR, bg=MAINCOLOR
#                  ).grid(row=1, column=0, columnspan=cnt_out + 2, sticky='nsew')
#
#         c = 0
#         s = sorted(set(self.criteria.values()))
#         # подписываем критерии
#         for i in range(1, cnt_out+1):
#             text = s[c].split()[0]
#             c += 1
#             lbl = tk.Label(self, text=text, font=SMALLFONT, fg=FONTCOLOR, bg=MAINCOLOR)
#             lbl.grid(row=2, column=i)
#             CreateToolTip(lbl, f'Критерий {s[c-1]}')
#         c = 0
#         for i in range(3, cnt_out+3):
#             text = s[c].split()[0]
#             c += 1
#             lbl2 = tk.Label(self, text=text, font=SMALLFONT, fg=FONTCOLOR, bg=MAINCOLOR)
#             lbl2.grid(row=i, column=0, sticky='e')
#             CreateToolTip(lbl2, f'Критерий {s[c-1]}')
#
#         check = (self.register(is_valid), "%P")
#         rows = range(3, cnt_out + 3)
#         columns = range(1, cnt_out + 1)
#         entries = []
#         for i in rows:
#             row_entries = []
#             for j in columns:
#                 entry = tk.Entry(self, width=5, validate = 'key', validatecommand=check)
#                 entry.grid(row=i, column=j)
#                 # вставка 1 по главной диагонали
#                 if i - j == 2:
#                     entry.insert(0, '1')
#                     entry.config(state = 'disabled')
#                 entry.bind("<KeyRelease>", lambda e: check_entries(entries))
#                 row_entries.append(entry)
#             entries.append(row_entries)
#
#         button2 = tk.Button(self, text='Подтвердить', font=LARGEFONT, bg=BUTTONCOLOR, fg=FONTCOLOR,
#                 activeforeground=BUTTONCOLOR, state = 'disabled',
#                 command=lambda: self.controller.show_frame(FillCriteriaIn, self.method, self.criteria, return_result(entries), None, self.task_name))
#         button2.grid(row=cnt_out + 3, column=1)
#
#         tk.Button(self, text='Назад', font=LARGEFONT, bg=BUTTONCOLOR, fg=FONTCOLOR, activeforeground=BUTTONCOLOR,
#                   command=lambda: self.controller.show_frame(ChooseMethod)).grid(row=cnt_out + 3, column=cnt_out)
#
#         for i in range(cnt_out + 2):
#             self.grid_columnconfigure(i, minsize=1050/(cnt_out+2))
#         for i in range(cnt_out + 5):
#             self.grid_rowconfigure(i, minsize=700/(cnt_out+5))
#
# class FillCriteriaIn(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent, bg=MAINCOLOR)
#         self.controller = controller
#
#     def set_method(self, method, criteria, criteria_out, criteria_in, task_name):
#         self.method = method  # Сохраняем переданные результаты
#         self.criteria = criteria
#         self.criteria_out = criteria_out
#         self.task_name = task_name
#         print('Критерии внешнего уровня:', self.criteria_out)
#
#         def is_valid(newval):
#             # проверка того, что вводится только цифры или /
#             result = re.match("^[13579/]*$", newval) is not None
#             return result
#
#         def check_entries(entries):
#             # Проверяем, заполнены ли все поля Entry
#             if all([i.get() for i in list(itertools.chain.from_iterable(entries))]):
#                 flg = 1
#                 # проверяем, правильно ли все заполнено
#                 for i in range(len(entries)):
#                     for j in range(len(entries[i])):
#                         if entries[i][j].get() != '1':
#                             if (entries[i][j].get().replace('1/', '') != entries[j][i].get().replace('1/', '')) \
#                                     or ('/' not in entries[i][j].get() and '/' not in entries[j][i].get()):
#                                 flg = 0
#                                 break
#                 if flg == 1:
#                     button2.config(state='normal')  # Активируем кнопку
#             else:
#                 button2.config(state='disabled')  # Деактивируем кнопку
#
#         def return_result_in(entries_in):
#             res = {}
#             for i in range(len(entries_in)):
#                 for j in range(len(entries_in[i])):
#                     if i != j:  # пропускаем диагональ (там всегда 1)
#                         key = (s[i], s[j])  # названия критериев
#                         val = entries_in[i][j].get()
#                         if '/' in val:
#                             val = float(val[0]) / float(val[2])
#                         res[key] = val
#             return res
#
#         cnt_in = len(self.criteria.keys())
#
#         tk.Label(self, text='Введите степени важности критериев второго уровня', font=MIDFONT, fg=FONTCOLOR,
#                  bg=MAINCOLOR
#                  ).grid(row=0, column=0, columnspan=cnt_in + 2, sticky='nsew')
#         tk.Label(self, text='''Шкала относительной важности:
#                                 1 – равная важность, 3(1/3) – умеренное превосходство, 5(1/5) – существенное превосходство,
#                                 7(1/7) – значительное превосходство, 9(1/9) – очень большое превосходство''',
#                  font=SMALLFONT, fg=FONTCOLOR, bg=MAINCOLOR
#                  ).grid(row=1, column=0, columnspan=cnt_in + 2, sticky='nsew')
#
#         c = 0
#         s = sorted(set(self.criteria.keys()))
#         for i in range(1, cnt_in + 1):
#             text = s[c].split()[0]
#             c += 1
#             lbl = tk.Label(self, text=text, font=SMALLFONT, fg=FONTCOLOR, bg=MAINCOLOR)
#             lbl.grid(row=2, column=i)
#             CreateToolTip(lbl, f'Критерий {s[c - 1]}')
#         c = 0
#         for i in range(3, cnt_in + 3):
#             text = s[c].split()[0]
#             c += 1
#             lbl2 = tk.Label(self, text=text, font=SMALLFONT, fg=FONTCOLOR, bg=MAINCOLOR)
#             lbl2.grid(row=i, column=0, sticky='e')
#             CreateToolTip(lbl2, f'Критерий {s[c - 1]}')
#
#         check = (self.register(is_valid), "%P")
#         rows = range(3, cnt_in + 3)
#         columns = range(1, cnt_in + 1)
#         entries_in = []
#         for i in rows:
#             row_entries = []
#             for j in columns:
#                 entry = tk.Entry(self, width=5, validate='key', validatecommand=check)
#                 entry.grid(row=i, column=j)
#                 # вставка 1 по главной диагонали
#                 if i - j == 2:
#                     entry.insert(0, '1')
#                     entry.config(state='disabled')
#                 entry.bind("<KeyRelease>", lambda e: check_entries(entries_in))
#                 row_entries.append(entry)
#             entries_in.append(row_entries)
#
#         button2 = tk.Button(self, text='Подтвердить', font=LARGEFONT, bg=BUTTONCOLOR, fg=FONTCOLOR,
#                             activeforeground=BUTTONCOLOR, state='disabled', command=lambda:
#             self.controller.show_frame(ShowResult, self.method, self.criteria, self.criteria_out,
#                                        return_result_in(entries_in), self.task_name))
#         button2.grid(row=cnt_in + 3, column=1)
#
#         tk.Button(self, text='Назад', font=LARGEFONT, bg=BUTTONCOLOR, fg=FONTCOLOR, activeforeground=BUTTONCOLOR,
#                   command=lambda: self.controller.show_frame(FillCriteriaOut)).grid(row=cnt_in + 3, column=cnt_in)
#
#         for i in range(cnt_in + 2):
#             self.grid_columnconfigure(i, minsize=1050 / (cnt_in + 2))
#         for i in range(cnt_in + 5):
#             self.grid_rowconfigure(i, minsize=700 / (cnt_in + 5))
#
#
# class ShowResult(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent, bg=MAINCOLOR)
#         self.controller = controller
#
#     def set_method(self, method, criteria, criteria_out, criteria_in, task_name):
#
#         # ОТБОР ПОДХОДЯЩИХ СУБД
#         cursor.execute(f"""
#             select version_name, count(distinct task_info_id) as cnt
#             from task_info c
#                 join tasks ca
#                     on c.tasks_id = ca.id
#                     and task_name = '{task_name}'
#                 join criteria_allowed_values cav
#                     on cav.criteria_id = c.criteria_id
#                     and task_value = allowed_value
#                 left join criteria_values cv
#                     on cav.id = criteria_allowed_values_id
#                 join dbms_versions dv
#                     on cv.dbms_id = dv.id
#             group by version_name
#             having count(distinct task_info_id) = max(task_info_id)""")
#         # Извлечение данных
#         rows = cursor.fetchall()
#         names = []
#         for i in rows:
#             name = i[0]
#             names.append(name)
#         print(names)
#
#         if method == 'Метод TOPSIS':
#             pass
#         elif method == 'Метод анализa иерархий':
#             criteria_in_weights = ahp(criteria_in, criteria_out)
#             print(criteria_in_weights)
#         tk.Label(self, text='Результат ранжирования', font=MIDFONT, fg=FONTCOLOR,
#                  bg=MAINCOLOR
#                  ).grid(row=0, column=0, columnspan=2, sticky='nsew')
#
#         for i in range(3):
#             self.grid_columnconfigure(i, minsize=350)
#         for i in range(7):
#             self.grid_rowconfigure(i, minsize=100)
