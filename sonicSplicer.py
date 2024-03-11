import tkinter as tk

def main():
    #Create main application window.
    root = tk.Tk()
    root.title("SonicSplicer - Music Editing Application")

    # Background color.
    root.configure(bg='#1a1a1a')

    #Calculate dimensions for the window to be 70% of screen size.
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    width = int(screen_width * 0.7)
    height = int(screen_height * 0.7)

    # Center tthe window on the screen.
    x_offset = int((screen_width - width) / 2)
    y_offset = int((screen_height - height) / 2)

    # Set the initial size and position of the window.
    root.geometry(f'{width}x{height}+{x_offset}+{y_offset}')

    # Make the layout responsive to window resizing.
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)

    # Start the Tkinter event loop.
    root.mainloop()

if __name__ == "__main__":
    main()