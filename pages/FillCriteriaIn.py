import tkinter as tk
from info.vars import *
from pages.ShowResult import ShowResult
from pages.FillCriteria import fill_criteria, return_result

class FillCriteriaIn(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=MAINCOLOR)
        self.controller = controller

    def set_method(self, method, criteria, criteria_out, criteria_in, task_id):
        self.method = method  # Сохраняем переданные результаты
        self.criteria = criteria
        self.criteria_out = criteria_out
        self.task_id = task_id
        print('Критерии внешнего уровня:', self.criteria_out)

        s = sorted(set(self.criteria.keys()))
        cnt = len(s)
        button2 = tk.Button(self, text='Подтвердить', font=LARGEFONT, bg=BUTTONCOLOR, fg=FONTCOLOR,
                            activeforeground=BUTTONCOLOR, state='disabled', command=lambda:
            self.controller.show_frame(ShowResult, self.method, self.criteria, self.criteria_out,
                                       return_result(entries, s), self.task_id))
        button2.grid(row=cnt + 3, column=1, columnspan=2)

        entries = fill_criteria(self, button2, cnt, s, 'второго')
        for i in range(cnt + 2):
            self.grid_columnconfigure(i, minsize=1050 / (cnt + 2))
        for i in range(cnt + 5):
            self.grid_rowconfigure(i, minsize=700 / (cnt + 5))

