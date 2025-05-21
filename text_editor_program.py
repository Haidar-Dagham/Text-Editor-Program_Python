import os  # Provides functions for interacting with the operating system
from tkinter import *  # Import all tkinter classes/functions
from tkinter import filedialog, colorchooser, font  # Import specific dialog and font modules
from tkinter.messagebox import *  # Import all message box functions
from tkinter.filedialog import *  # Import all file dialog functions

# Function to open a color picker and change the text color
def change_color():
    color = colorchooser.askcolor(title="Pick a Color")  # Open color picker dialog
    text_area.config(fg=color[1])  # Set the chosen color as text foreground color

# Function to change font based on selection
def change_font(*args):
    text_area.config(font=(font_name.get(), size_box.get()))  # Update font and size

# Create a new file (clears text area)
def new_file():
    window.title("Untitled")  # Reset window title
    text_area.delete(1.0, END)  # Clear all text

# Function to open and read a text file
def open_file():
    file = askopenfilename(defaultextension=".txt",
                           file=[("All Files", "*.*"),
                                 ("Text Documents", "*.txt")])  # Show open file dialog
    if file is None:
        return  # If no file selected, exit function
    else:
        try:
            window.title(os.path.basename(file))  # Update window title with file name
            text_area.delete(1.0, END)  # Clear current text
            file = open(file, "r")  # Open file in read mode
            text_area.insert(1.0, file.read())  # Insert file content into text area
        except Exception:
            print("Couldn't read this file!")  # Handle any error
        finally:
            file.close()  # Ensure file is closed

# Function to save the current content to a file
def save_file():
    file = filedialog.asksaveasfilename(initialfile='unititled.txt',
                                        defaultextension=".txt",
                                        filetypes=[("All Files", "*.*"),
                                                   ("Text Documents", "*.txt")])  # Show save dialog
    if file is None:
        return  # Do nothing if user cancels
    else:
        try:
            window.title(os.path.basename(file))  # Update window title
            file = open(file, "w")  # Open file in write mode
            file.write(text_area.get(1.0, END))  # Write all text from the editor
        except Exception:
            print("Couldn't save this file!")  # Handle write error
        finally:
            file.close()  # Always close the file

# Standard clipboard cut operation
def cut():
    text_area.event_generate("<<Cut>>")

# Standard clipboard copy operation
def copy():
    text_area.event_generate("<<Copy>>")

# Standard clipboard paste operation
def paste():
    text_area.event_generate("<<Paste>>")

# Show an 'About' info box
def about():
    showinfo("About", "Written by HaidarDagham")

# Quit the application
def quit():
    window.destroy()  # Close the main window

# GUI Setup

window = Tk()  # Create the main application window
window.title("Haidar Dagham's Text Editor")  # Set window title
file = None  # Placeholder for currently opened file

# Set window size and center on screen
window_width = 500
window_height = 500
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
window.geometry(f"{window_width}x{window_height}+{x}+{y}")  # Apply geometry

# Font settings
font_name = StringVar(window)
font_name.set("Arial")  # Default font

font_size = StringVar(window)
font_size.set("25")  # Default font size

# Create the main text area for editing
text_area = Text(window, font=(font_name.get(), font_size.get()), bg="white")

# Add a vertical scrollbar
scroll_bar = Scrollbar(text_area)
window.grid_rowconfigure(0, weight=1)  # Allow resizing rows
window.grid_columnconfigure(0, weight=1)  # Allow resizing columns
text_area.grid(sticky=N + E + S + W)  # Expand text area in all directions
scroll_bar.pack(side=RIGHT, fill=Y)  # Attach scrollbar to right
text_area.config(yscrollcommand=scroll_bar.set)  # Link scrollbar to text area

# Font & color selection frame
frame = Frame(window)
frame.grid()

# Button to open color chooser
color_button = Button(frame, text="color", command=change_color)
color_button.grid(row=0, column=0)

# Dropdown for selecting font family
font_box = OptionMenu(frame, font_name, *font.families(), command=change_font)
font_box.grid(row=0, column=1)

# Spinbox to select font size
size_box = Spinbox(frame, from_=1, to=100, textvariable=font_size, command=change_font)
size_box.grid(row=0, column=2)

# Create the main menu bar
menu_bar = Menu(window)
window.config(menu=menu_bar)

# File menu with options
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()  # Adds a horizontal separator
file_menu.add_command(label="Exit", command=quit)

# Edit menu with cut/copy/paste
edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)

# Help menu with about section
help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)

window.mainloop()  # Start the Tkinter event loop
