import tkinter as tk

def main():
    #Create main application window.
    root = tk.Tk()
    root.title("SonicSplicer - Music Editing Application")

    #Calculate dimensions for the window to be 70% of screen size.
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    width = int(screen_width * 0.7)
    height = int(screen_height * 0.7)