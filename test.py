import tkinter as tk
from tkinter import TOP

class PackedLabel(tk.Label):
    #Subclass of label which automatically packs itself after initialisation.
    def __init__(self, parent, side=tk.TOP, padx=0, pady=0, **kwargs):
        self.side = side
        self.padx = padx
        self.pady = pady
        self.parent = parent
        self.label = super().__init__(self.parent, **kwargs)

    def __post_init__(self):
        self.label.pack(side=self.side, padx=self.padx, pady=self.pady)
        super().__post_init__()


class gui(tk.Tk):
    def __init__(self):
        self.window = tk.Tk()
        self.window.protocol("WM_DELETE_WINDOW", exit)
        self.window.geometry('1500x1000')
        self.window.own_hand_frame = tk.Frame(self.window, borderwidth=2, relief="groove")
        self.window.own_hand_frame.pack(side=TOP)
        self.window.label = PackedLabel(self.window.own_hand_frame, side=TOP, text = 'Your Own Hand')

        self.window.mainloop()

if __name__ == "__main__":
    game = gui()
