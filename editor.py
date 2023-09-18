from tkinter import *
from tkinter import filedialog as FileDialog

path = ""

# Functions

def new():
    global path
    message.set("New file")
    path = ""
    text.delete(1.0, "end")
    root.title("My editor")

def open_file():
    global path
    message.set("Open file")
    path = FileDialog.askopenfilename(
                                    initialdir=".",
                                    filetypes=(("Text files", "*.txt"),),
                                    title="Open a text file")
    if path != "":
        file = open(path, "r")
        content = file.read()
        text.delete(1.0, "end")
        text.insert("insert", content)
        file.close()
        root.title(path + " - My editor")

def save():
    message.set("Save file")
    if path != "":
        content = text.get(1.0, "end-1c")
        file = open(path, "w+")
        file.write(content)
        file.close()
        message.set("Saved file")
    else:
        save_as()

def save_as():
    global path
    message.set("Save file as")
    file = FileDialog.asksaveasfile(title="Save file", mode="w", defaultextension=".txt")
    if file is not None:
        path = file.name
        content = text.get(1.0, "end-1c")
        file.write(content)
        file.close()
        message.set("Saved file")
    else:
        message.set("Save canceled")
        path = ""

# Root configuration

root = Tk()
root.title("Text Editor")

# Main menu

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=new)
filemenu.add_command(label="Open", command=open_file)
filemenu.add_command(label="Save", command=save)
filemenu.add_command(label="Save As", command=save_as)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(menu=filemenu, label="File")

root.config(menu=menubar)

# Central text box

text = Text(root)
text.pack(fill="both",expand=1)
text.config(bd=0, padx=6, pady=4, font=("Consolas",12))

# Monitor

message = StringVar()
message.set("Welcome to your editor")
monitor = Label(root, textvar=message, justify="left")
monitor.pack(side="left")

# Aplication loop

root.mainloop()