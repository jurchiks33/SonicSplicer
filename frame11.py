#frame11.py(equalizer)
import tkinter as tk
import random

class EqualizerFrame:
    def __init__(self, parent):
        self.frame = tk.Frame(parent, bg='black')
        self.canvas = tk.Canvas(self.frame, bg='black')
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.bars = []

        #Create initial bars on the canvas.
        for i in range(10):  #Create 10 bars.
            bar = self.canvas.create_rectangle(10 + i*20, 250, 25 + i*20, 150, fill='green')
            self.bars.append(bar)
        
        self.update_equalizer()