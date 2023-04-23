from tkinter import *
import tkinter.filedialog as fd
import tkinter.messagebox as mb

import os
import shutil
file_notepad=None
root = Tk()
# Creating the backend functions
def open_file():
    #Basic Tkinter Set Up
    root_functions = Toplevel()
    root_functions.title("File Functions")
    root_functions.geometry("250x250")
    root_functions.config(bg = "white")
    root_functions.resizable(0,0)
    def createafile():
        root_notepad = Toplevel()
        root_notepad.title("Untitled - Notepad")
        root_notepad.geometry("700x500")
        # root.wm_iconbitmap("D:\\Study Materals and Data\\Semester 4\\2CS404 Programing for Scientific Computing\\Notepad.ico")

        #Adding text Area 
        TextArea = Text(root_notepad, font=("Century Schoolbook", 15))
        file_notepad = None
        TextArea.pack(expand=True, fill=BOTH) #will take parent width when expanded
        def newFile():
            global file_notepad
            root_notepad.title("Untitle-Notepad")
            file = None
            TextArea.delete(1.0, END) # 1.0 means 1st line and 0th character will delete till End
        def saveFile():
            global file_notepad
            if file_notepad==None:
                file_notepad=fd.asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt", filetypes=[("All files", "*.*"),("Text Documents", "*.txt")])
                if file_notepad=="":
                    file_notepad=None
                else:
                    f = open(file_notepad,"w")
                    f.write(TextArea.get(1.0,END))
                    f.close()
                    root_notepad.title(os.path.basename(file_notepad)+" - Notepad") # will scan the filename
                    print("File Saved")
            else:
                f = open(file_notepad,"w")
                f.write(TextArea.get(1.0,END))
                f.close()
                root_notepad.title(os.path.basename(file_notepad)+" - Notepad") # will scan the filename
                print("File Saved")
        #Creating Menubar
        menu = Menu(root_notepad)
        #File menu start
        FileMenu = Menu(menu, tearoff=0)
        FileMenu.add_command(label="Save",command=saveFile)
        menu.add_cascade(label="File",menu=FileMenu)
        root_notepad.config(menu=menu)

        #Adding scrollbar
        scroll = Scrollbar(TextArea)
        scroll.pack(side=RIGHT, fill=Y)
        scroll.config(command=TextArea.yview)
        TextArea.config(yscrollcommand=scroll.set)
        root_notepad.mainloop()
        return
    
    def openafile():
        root_notepad = Toplevel()
        root_notepad.title("Untitled - Notepad")
        root_notepad.geometry("700x500")
        # root.wm_iconbitmap("D:\\Study Materals and Data\\Semester 4\\2CS404 Programing for Scientific Computing\\Notepad.ico")
        #Adding text Area 
        TextArea = Text(root_notepad, font=("Century Schoolbook", 15))
        TextArea.pack(expand=True, fill=BOTH) #will take parent width when expanded
        # def openFile():
        global file_notepad
        file_notepad = None
        file_notepad = fd.askopenfilename(defaultextension=".txt", filetypes=[("All files", "*.*"),("Text Documents", "*.txt")])
        if file_notepad=="":
            file_notepad=None
        else:
            root_notepad.title(os.path.basename(file_notepad)+" - Notepad") # will scan the filename
            TextArea.delete(1.0,END)
            f=open(file_notepad,"r")
            TextArea.insert(1.0,f.read())
            f.close()
        def saveFile():
            global file_notepad
            if file_notepad==None:
                file_notepad=fd.asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt", filetypes=[("All files", "*.*"),("Text Documents", "*.txt")])
                if file_notepad=="":
                    file_notepad=None
                else:
                    f = open(file_notepad,"w")
                    f.write(TextArea.get(1.0,END))
                    f.close()
                    root_notepad.title(os.path.basename(file_notepad)+" - Notepad") # will scan the filename
                    print("File Saved")
            else:
                f = open(file_notepad,"w")
                f.write(TextArea.get(1.0,END))
                f.close()
                root_notepad.title(os.path.basename(file_notepad)+" - Notepad") # will scan the filename
                print("File Saved")
        #Creating Menubar
        menu = Menu(root_notepad)
        #File menu start
        FileMenu = Menu(menu, tearoff=0)
        # FileMenu.add_command(label="Open", command=openFile)
        FileMenu.add_command(label="Save Changes", command=saveFile)
        menu.add_cascade(label="File",menu=FileMenu)
        root_notepad.config(menu=menu)

        #Adding scrollbar
        scroll = Scrollbar(TextArea)
        scroll.pack(side=RIGHT, fill=Y)
        scroll.config(command=TextArea.yview)
        TextArea.config(yscrollcommand=scroll.set)
        root_notepad.mainloop()
        return

    Button(root_functions, text="Create a File", width = 10, font=button_font, bg=button_background, command=createafile).place(x=70, y=50)
    Button(root_functions, text="Open a File", width = 10, font=button_font, bg=button_background,command=openafile).place(x=70, y=100)

def copy_file():
    file_to_copy = fd.askopenfilename(title='Choose a file to copy', filetypes=[("All files", "*.*")])
    dir_to_copy_to = fd.askdirectory(title="In which folder to copy to?")

    try:
        shutil.copy(file_to_copy, dir_to_copy_to)
        mb.showinfo(title='File copied!', message='Your desired file has been copied to your desired location')
    except:
        mb.showerror(title='Error!', message='We were unable to copy your file to the desired location. Please try again')


def delete_file():
    file = fd.askopenfilename(title='Choose a file to delete', filetypes=[("All files", "*.*")])

    os.remove(os.path.abspath(file))

    mb.showinfo(title='File deleted', message='Your desired file has been deleted')


def rename_file():
    file = fd.askopenfilename(title='Choose a file to rename', filetypes=[("All files", "*.*")])

    rename_wn = Toplevel(root)
    rename_wn.title("Rename the file to")
    rename_wn.geometry("250x80"); rename_wn.resizable(0, 0)

    Label(rename_wn, text='What should be the new name of the file?', font=("Times New Roman", 10)).place(x=0, y=0)
    new_name = Entry(rename_wn, width=40, font=("Times New Roman", 10))
    new_name.place(x=0, y=30)
    def clicked():
        new_file_name = os.path.join(os.path.dirname(file), new_name.get()+os.path.splitext(new_name.get())[1])

        os.rename(file, new_file_name)
        mb.showinfo(title="File Renamed", message='Your desired file has been renamed')
        return
    def clicked1():
        mb.showinfo(title="Action Aborted", message='Your desired file has not been renamed')
        return
    Button(rename_wn, text="Yes", width=5, bg=button_background, font=button_font, command=clicked).place(x=60, y=50)
    Button(rename_wn, text="No", width=5, bg=button_background , font=button_font, command=clicked1).place(x=150, y=50)    


def open_folder():
    folder = fd.askdirectory(title="Select Folder to open")
    os.startfile(folder)


def delete_folder():
    folder_to_delete = fd.askdirectory(title='Choose a folder to delete')
    os.rmdir(folder_to_delete)
    mb.showinfo("Folder Deleted", "Your desired folder has been deleted")


def move_folder():
    folder_to_move = fd.askdirectory(title='Select the folder you want to move')
    mb.showinfo(message='You just selected the folder to move, now please select the desired destination where you want to move the folder to')
    destination = fd.askdirectory(title='Where to move the folder to')

    try:
        shutil.move(folder_to_move, destination)
        mb.showinfo("Folder moved", 'Your desired folder has been moved to the location you wanted')
    except:
        mb.showerror('Error', 'We could not move your folder. Please make sure that the destination exists')


def list_files_in_folder():
    dirname = fd.askdirectory(parent=root, initialdir='/home/', title='Select your database' )
    files=os.listdir(dirname)
    # print (files, file="D:\\Data Science\\GUI\\Notepad.py")

    list_files_wn = Toplevel(root)
    list_files_wn.title('Files in your selected folder')
    list_files_wn.geometry('150x250')
    list_files_wn.resizable(300, 200)
    list_files_wn.config(bg=background)
    scroll = Scrollbar(list_files_wn)
    scroll.pack(side = RIGHT,fill=Y)
    listbox = Listbox(list_files_wn, selectbackground='SteelBlue', font=("Century Schoolbook", 10), height=250, width=150, yscrollcommand= scroll.set)
    for i in files:
        listbox.insert(END,f"{i}")
        listbox.place(x=10, y=10)
    listbox.pack(fill="both", padx=30)
    scroll.config(command =listbox.yview)


def rateus():
    rate_root = Toplevel(root)
    rate_root.title("Rate Us")
    rate_root.geometry('250x150')
    rate_root.resizable(0,0)
    ms1 = Scale(rate_root, from_= 1, to=10, orient=HORIZONTAL)
    ms1.pack()
    def submit():
        mb.showinfo("Feedback", "Thank you for your valueable feedback")
        f = open("D:\\Data Science\\Feedback.txt","a+")
        f.write(str(ms1.get()))
        f.write("\n")
        f.close()
        return
    Button(rate_root, text="Submit Ratings", command = submit).pack()
# Defining the variables
title = 'File Explorer'
background = 'white'

button_font = ("Times New Roman", 13)
button_background = 'Turquoise'

# Initializing the window
blank_space = " "
root.title(50*blank_space+"File Explorer")
root.geometry('500x430')
root.resizable(0,0)
root.config(bg=background)
root.wm_iconbitmap("D:\\Data Science\\GUI\\File_Manager.ico") # Setting Icons of File Manager
# Creating and placing the components in the window
Label(root, text=title, font=("Century Schoolbook", 20,"bold"), bg=background, wraplength=250).place(x=150, y=0)

Button(root, text='File Functions', width=20, font=button_font, bg=button_background, command=open_file).place(x=150, y=50)

Button(root, text='Copy a file', width=20, font=button_font, bg=button_background, command=copy_file).place(x=150, y=90)

Button(root, text='Rename a file', width=20, font=button_font, bg=button_background, command=rename_file).place(x=150, y=130)

Button(root, text='Delete a file', width=20, font=button_font, bg=button_background, command=delete_file).place(x=150, y=170)

Button(root, text='Open a folder', width=20, font=button_font, bg=button_background, command=open_folder).place(x=150, y=210)

Button(root, text='Delete a folder', width=20, font=button_font, bg=button_background, command=delete_folder).place(x=150, y=250)

Button(root, text='Move a folder', width=20, font=button_font, bg=button_background, command=move_folder).place(x=150, y=290)

Button(root, text='List all files in a folder', width=20, font=button_font, bg=button_background, command=list_files_in_folder).place(x=150, y=330)

Button(root, text='Rate Us', width=20, font=button_font, bg=button_background, command=rateus).place(x=150, y=370)

# Finalizing the window
root.update()
root.mainloop()
