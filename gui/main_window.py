import tkinter as tk

from config import color
from .menu import menu
from .layout.header import build_header
from .layout.body import build_body
from .layout.footer import build_footer

class MainWindow:
    def __init__(self, root):
        self.root = root

    def build(self):
        self._configure_root()
        build_header(self)
        build_body(self)
        build_footer(self)

    def _configure_root(self):
        self.root.title("Rectangle Lab")

        window_width = 800
        window_height = 600

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = int((screen_width / 2) - (window_width / 2))
        y = int((screen_height / 2) - (window_height / 2))

        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)