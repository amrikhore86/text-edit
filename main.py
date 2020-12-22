from tkinter import *
from tkinter import filedialog
from tkinter import font

root=Tk()
root.title('Code Edit')
root.iconbitmap(r'C:\Users\Me\Desktop\Projects\Code Edit\icon\icon.ico')
root.geometry('1200x650')

#Functionality goes here
def new_file():
    my_text.delete("1.0",END)
    root.title('New File- Code Edit')
    status_bar.config(text="New File        ")
    
def open_file():
    my_text.delete('1.0',END)
    
    text_file=filedialog.askopenfilename(initialdir=r"C:/User/",title="Open File",filetypes=(("Text Files","*.txt"),("HTML Files","*.html"),("Python Files","*.py"),("All Files","*.*")))
    name=text_file
    status_bar.config(text=f'{name}        ')
    name.replace("C:/User/","")
    root.title(f'{name} - Code Edit')
    
    text_file=open(text_file,'r')
    content=text_file.read()
    my_text.insert(END,content)
    text_file.close()
    
def save_file():
    pass

def save_file_as():
    pass
    
    

#Main Frame goes here
my_frame=Frame(root)
my_frame.pack(pady=5)

#Scrollbar goes here
text_scroll=Scrollbar(my_frame)
text_scroll.pack(side=RIGHT,fill=Y)

#Text Box goes here
my_text=Text(my_frame,width=97,height=25,font=('Helvetica',16),selectbackground='yellow',selectforeground="black",undo=True,yscrollcommand=text_scroll.set)
my_text.pack()

#Menu Goes here
my_menu=Menu(root)
root.config(menu=my_menu)

#File Menu Goes here
file_menu=Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="New",command=new_file)
file_menu.add_command(label="Open",command=open_file)
file_menu.add_command(label="Save",command=save_file)
file_menu.add_command(label="Save As",command=save_file_as)
file_menu.add_command(label="Exit",command=root.destroy)

#Edit Menu Goes here
edit_menu=Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="Edit",menu=edit_menu)
edit_menu.add_command(label="Size")
edit_menu.add_command(label="Font")
edit_menu.add_command(label="Color")
edit_menu.add_command(label="Syntax Highlighting")

#Status Bar goes here
status_bar=Label(root,text="Ready       ",anchor=E)
status_bar.pack(fill=X,side=BOTTOM)

root.mainloop()