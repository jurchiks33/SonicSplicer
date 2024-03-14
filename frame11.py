#frame11.py(equalizer)
import tkinter as tk
import random

class EqualizerFrame:
    def __init__(self, parent):
        self.frame = tk.Frame(parent, bg='black')
        self.canvas = tk.Canvas(self.frame, bg='black')
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.bars = []