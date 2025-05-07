import itertools
import re
from pages.Tooltip import CreateToolTip
import tkinter as tk
from data.vars import *


def return_result(entries, s):
    res = {}
    for i in range(len(entries)):
        for j in range(len(entries[i])):
            if i != j:  # пропускаем диагональ (там всегда 1)
                key = (s[i], s[j])  # названия критериев
                val = entries[i][j].get()
                if '/' in val:
                    val = float(val[0]) / float(val[2])
                res[key] = val
    return res

def fill_criteria(self, button2, cnt, s, text_in):

    def is_valid(newval):
        # проверка того, что вводится только цифры или /
        result = re.match("^[13579/]*$", newval) is not None
        return result
    def check_entries(entries):
        # вставляем обратные значения
        for i in range(len(entries)):
            for j in range(len(entries[i])):
                if i > j:
                    value = entries[i][j].get()
                    if '/' in value or value == '1':
                        x = value[-1]
                    else:
                        x = f'1/{value}'
                    entries[j][i].config(state='normal')
                    entries[j][i].delete(0, 'end')
                    entries[j][i].insert(0, x)
                    entries[j][i].config(state='disabled')

            # После заполнения проверяем, все ли ячейки заполнены
        if all([i.get() for i in list(itertools.chain.from_iterable(entries))]):
            if all([i.get() for i in list(itertools.chain.from_iterable(entries))]):
                flg = 1
                # проверяем, правильно ли по диагонали все заполнено
                for i in range(len(entries)):
                    for j in range(len(entries[i])):
                        if entries[i][j].get() != '1':
                            if ('/' not in entries[i][j].get() and '/' not in entries[j][i].get()) \
                                    and (entries[i][j].get() != 1) \
                                    and (entries[j][i].get() != 1):
                                flg = 0
                                break
                            elif ('/' in entries[i][j].get() and '/' in entries[j][i].get()):
                                flg = 0
                                break
                            elif entries[i][j].get().replace('1/', '') != entries[j][i].get().replace('1/', '') \
                                    and (('/' in entries[i][j].get() and '/' not in entries[j][i].get())
                                         or ('/' not in entries[i][j].get() and '/' in entries[j][i].get())):
                                flg = 0
                                break
                if flg == 1:
                    button2.config(state='normal')
                else:
                    button2.config(state='disabled')
        else:
            button2.config(state='disabled')

    tk.Label(self, text=f'Введите степени важности критериев {text_in} уровня', font=MIDFONT, fg=FONTCOLOR,
             bg=MAINCOLOR
             ).grid(row=0, column=0, columnspan=cnt + 2, sticky='nsew')
    tk.Label(self, text='''Шкала относительной важности:
                            1 – равная важность, 3(1/3) – умеренное превосходство, 5(1/5) – существенное превосходство,
                            7(1/7) – значительное превосходство, 9(1/9) – очень большое превосходство''',
             font=SMALLFONT, fg=FONTCOLOR, bg=MAINCOLOR
             ).grid(row=1, column=0, columnspan=cnt + 2, sticky='nsew')

    c = 0
    for i in range(1, cnt + 1):
        text = s[c].split()[0]
        c += 1
        lbl = tk.Label(self, text=text, font=SMALLFONT, fg=FONTCOLOR, bg=MAINCOLOR)
        lbl.grid(row=2, column=i)
        CreateToolTip(lbl, f'Критерий {s[c - 1]}')
    c = 0
    for i in range(3, cnt + 3):
        text = s[c].split()[0]
        c += 1
        lbl2 = tk.Label(self, text=text, font=SMALLFONT, fg=FONTCOLOR, bg=MAINCOLOR)
        lbl2.grid(row=i, column=0, sticky='e')
        CreateToolTip(lbl2, f'Критерий {s[c - 1]}')

    check = (self.register(is_valid), "%P")
    rows = range(3, cnt + 3)
    columns = range(1, cnt + 1)
    entries = []
    for i in rows:
        row_entries = []
        for j in columns:
            entry = tk.Entry(self, width=5, validate='key', validatecommand=check)
            entry.grid(row=i, column=j)
            # вставка 1 по главной диагонали
            if j >=  i - 2:
                if j == i - 2:
                    entry.insert(0, '1')
                entry.config(state='disabled')
            entry.bind("<KeyRelease>", lambda e: check_entries(entries))
            row_entries.append(entry)
        entries.append(row_entries)

    return entries