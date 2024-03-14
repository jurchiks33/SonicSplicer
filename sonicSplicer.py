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

    # # Make the layout responsive to window resizing.
    # root.grid_columnconfigure(0, weight=1)
    # root.grid_rowconfigure(0, weight=1)
    frame1 = tk.Frame(root, bg='silver', bd=2, relief='solid')
    frame2 = tk.Frame(root, bg='silver', bd=2, relief='solid')
    frame3 = tk.Frame(root, bg='silver', bd=2, relief='solid')
    frame4 = tk.Frame(root, bg='silver', bd=2, relief='solid')
    frame5 = tk.Frame(root, bg='silver', bd=2, relief='solid')
    frame6 = tk.Frame(root, bg='silver', bd=2, relief='solid')
    frame7 = tk.Frame(root, bg='silver', bd=2, relief='solid')
    frame8 = tk.Frame(root, bg='silver', bd=2, relief='solid')
    frame9 = tk.Frame(root, bg='silver', bd=2, relief='solid')

    #Place frames in a layout.
    frame1.place(relx=0.05, rely=0.05, relwidth=0.2, relheight=0.2)  
    frame2.place(relx=0.05, rely=0.28, relwidth=0.2, relheight=0.2)
    frame3.place(relx=0.3, rely=0.05, relwidth=0.4, relheight=0.43)
    frame4.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.2)
    frame5.place(relx=0.75, rely=0.28, relwidth=0.2, relheight=0.2)
    frame6.place(relx=0.26, rely=0.05, relwidth=0.03, relheight=0.43) #Long vertical left
    frame7.place(relx=0.71, rely=0.05, relwidth=0.03, relheight=0.43) #Long vertical right
    frame8.place(relx=0.15, rely=0.49, relwidth=0.7, relheight=0.15)
    frame9.place(relx=0.05, rely=0.49, relwidth=0.095, relheight=0.15)

    # Start the Tkinter event loop.
    root.mainloop()

if __name__ == "__main__":
    main()