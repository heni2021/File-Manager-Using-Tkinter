from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

#Basic Tkinter Set Up
root = Tk()
root.title("Untitled - Notepad")
root.geometry("700x500")
# root.wm_iconbitmap("D:\\Study Materals and Data\\Semester 4\\2CS404 Programing for Scientific Computing\\Notepad.ico")

#Adding text Area 
TextArea = Text(root, font=("Century Schoolbook", 15))
file = None
TextArea.pack(expand=True, fill=BOTH) #will take parent width when expanded

def newFile():
    global file
    root.title("Untitle-Notepad")
    file = None
    TextArea.delete(1.0, END) # 1.0 means 1st line and 0th character will delete till End
def openFile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All files", "*.*"),("Text Documents", "*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+" - Notepad") # will scan the filename
        TextArea.delete(1.0,END)
        f=open(file,"r")
        TextArea.insert(1.0,f.read())
        f.close()
def saveFile():
    global file
    if file==None:
        file=asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt", filetypes=[("All files", "*.*"),("Text Documents", "*.txt")])
        if file=="":
            file=None
        else:
            f = open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file)+" - Notepad") # will scan the filename
            print("File Saved")
    else:
        f = open(file,"w")
        f.write(TextArea.get(1.0,END))
        f.close()
        root.title(os.path.basename(file)+" - Notepad") # will scan the filename
        print("File Saved")
def quitApp():
    root.destroy()
def cut():
    TextArea.event_generate("<<Cut>>") #Automatically handles cut event
def copy():
    TextArea.event_generate("<<Copy>>")
def paste():
    TextArea.event_generate("<<Paste>>")
def about():
    tmsg.showinfo("About Notepad!","This is a licensed version of Notepad 2.1.0")
#Creating Menubar
menu = Menu(root)
#File menu start
FileMenu = Menu(menu, tearoff=0)
FileMenu.add_command(label="New",command=newFile)
FileMenu.add_command(label="Open", command=openFile)
FileMenu.add_command(label="Save",command=saveFile)
FileMenu.add_separator()
FileMenu.add_command(label="Exit", command = quitApp)
menu.add_cascade(label="File",menu=FileMenu)
#Edit menu start
EditMenu = Menu(menu, tearoff=0)
EditMenu.add_command(label="Cut", command=cut)
EditMenu.add_command(label="Copy", command=copy)
EditMenu.add_command(label="Paste", command=paste)
menu.add_cascade(label="Edit",menu=EditMenu)
#help menu start
HelpMenu = Menu(menu, tearoff=0)
HelpMenu.add_command(label="About Notepad", command=about)
menu.add_cascade(label="Help", menu=HelpMenu)
root.config(menu=menu)

#Adding scrollbar
scroll = Scrollbar(TextArea)
scroll.pack(side=RIGHT, fill=Y)
scroll.config(command=TextArea.yview)
TextArea.config(yscrollcommand=scroll.set)
root.mainloop()
