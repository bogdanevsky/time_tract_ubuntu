from tkinter import *
from utils.get_file import resource_path
from os import path


class Window(Tk):
    def __init__(self, name, w, h):
        super().__init__()
        self.title("pgAdmin4")
        try:
            icon = PhotoImage(file=resource_path(path.join("assets", "postgresql.248x256.png")))
            self.iconphoto(False, icon)
        except Exception as e:
            print(f"Failed to load icon: {e}")
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.resizable(False, False)