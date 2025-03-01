from pydoc import text
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import showerror

filename = None


def newfile():
    global filename
    filename = "Untitled"
    text.delete(0.0, END)


def savefile():
    global filename
    t = text.get(0.0, END)
    f = open(filename, "w")
    f.write(t)
    f.close()


def saveAs():
    f = asksaveasfile(mode='w', defaultextension='.txt')
    t = text.get(0.0, END)
    try:
        f.write(t.strip())
    except:
        showerror("Error", "Can't save text.")

def openfile():
    f = askopenfile(mode='r')
    t = f.read()
    text.delete(0.0, END)
    text.insert(0.0, t)

root = Tk()
root.title("HRText Editor")
root.geometry("400x400")
root.resizable(False, False)

text = Text(root, height=400, width=400)
text.pack()

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=newfile)
filemenu.add_command(label="Save", command=savefile)
filemenu.add_command(label="Save As..", command=saveAs)
filemenu.add_command(label="Open", command=openfile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)
root.mainloop()
