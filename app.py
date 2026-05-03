import tkinter as tk
from gui import MainWindow


def run_app():
    root = tk.Tk()
    MainWindow(root).build()
    root.mainloop()
