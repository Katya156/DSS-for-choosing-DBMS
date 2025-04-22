import tkinter as tk
from info.vars import *
from pages.ChooseMethod import ChooseMethod
from pages.OldResults import OldResults

class StartPage(tk.Frame):
    """
     Данное поле открывается когда программа начинает работать
    """
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent,  bg = MAINCOLOR)

        tk.Label(self, text ="СППР для выбора СУБД", font = LARGEFONT, bg =MAINCOLOR, fg = FONTCOLOR
                 ).grid(row = 1, column = 1, padx = 10, pady = 10)

        main_menu = ['Выбрать СУБД', 'Поcмотреть старые результаты']

        tk.Button(self, text=main_menu[0], font=LARGEFONT, bg=BUTTONCOLOR, fg=FONTCOLOR,
                  activeforeground=BUTTONCOLOR, command=lambda: controller.show_frame(ChooseMethod)
                  ).grid(row=3, column=1, stick='snwe')

        tk.Button(self, text=main_menu[1], font=LARGEFONT, bg=BUTTONCOLOR, fg=FONTCOLOR,
                  activeforeground=BUTTONCOLOR, command=lambda: controller.show_frame(OldResults)
                  ).grid(row=4, column=1, stick='snwe')

        for i in range(3):
            self.grid_columnconfigure(i, minsize=350)
        for i in range(7):
            self.grid_rowconfigure(i, minsize=100)