
from tkinter import *


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    # creation if init_window
    def init_window(self):
        # changing of title of master widget
        self.master.title("onscreen_Keyboard")
        self.master.resizable = (0, 0)
        # allowing the widget to take the full space of the root window

    q_to_p_keys = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
    a_to_l_keys = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
    z_to_m_keys = ['z', 'x', 'c', 'v', 'b', 'n', 'm']
