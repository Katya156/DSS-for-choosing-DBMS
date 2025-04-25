import tkinter as tk
from info.vars import *
from pages.StartPage import StartPage
from pages.OldResults import OldResults
from pages.ChooseMethod import ChooseMethod
from pages.FillCriteriaOut import FillCriteriaOut
from pages.FillCriteriaIn import FillCriteriaIn
from pages.ShowResult import ShowResult
from pages.ChooseCriteria import ChooseCriteria
from info.paths import resource_path

class tkinterApp():
    """
     Создается окно в котором мы будем работать и выстраиваются все параметры
    """
    root = tk.Tk()
    root.title('СППР для выбора СУБД')
    root.geometry('1050x700+100+50')
    root.resizable(False, True)
    root.config(bg=MAINCOLOR)
    photo = tk.PhotoImage(file =resource_path("info/icon.png"))
    root.iconphoto(False, photo)

    def __init__(self):
        container = tk.Frame(tkinterApp.root)
        container.pack()

        container.grid_rowconfigure(0, weight = 1, minsize = 750)
        container.grid_columnconfigure(0, weight = 1,  minsize = 1050)

        self.frames = {}
        for F in (StartPage, OldResults, ChooseMethod, ChooseCriteria, FillCriteriaOut, FillCriteriaIn, ShowResult):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky ="n")
        self.show_frame(StartPage)
        tkinterApp.root.mainloop()

    def show_frame(self, cont, method = None, criteria = None, criteria_out = None, criteria_in = None, task_id = None):
        frame = self.frames[cont]
        if method is not None or criteria is not None:
            frame.set_method(method, criteria, criteria_out, criteria_in, task_id)  # Передаем результаты в фрейм
        #     эту функцию нужно сделать в каждом классе который должен что-то принимать от пред окна
        frame.tkraise()