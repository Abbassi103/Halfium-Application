import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import subprocess
import os
import webbrowser
import platform

#full screen app
class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)            
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom

class App(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)
        self.original = Image.open('Background.png')
        self.image = ImageTk.PhotoImage(self.original)
        self.display = Canvas(self, bd=0, highlightthickness=0)
        self.display.create_image(0, 0, image=self.image, anchor=NW, tags="IMG")
        self.display.grid(row=0, sticky=W+E+N+S)
        self.pack(fill=BOTH, expand=1)
        self.bind("<Configure>", self.resize)

    def resize(self, event):
        size = (event.width, event.height)
        resized = self.original.resize(size,Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(resized)
        self.display.delete("IMG")
        self.display.create_image(0, 0, image=self.image, anchor=NW, tags="IMG")


root = Tk()
app = App(root)
root.title('HALFIUM CALCUL')
FullScreenApp(root)
icone = tk.PhotoImage(file=r'C:/Ham_HA/Halfium Calc/LSAMA.png')
root.iconphoto(True, icone)

#===================================== New Windows ===========================
def open_mov():
    try:
        subprocess.run("mov_test.py", shell=True)
    except:
        print('Mov module not found!')

def open_bas():
    try:
        subprocess.run("bas_test.py", shell=True)
    except:
        print('Bas module not found!')
    
def open_ham():
    try:
        subprocess.run("ham_test.py", shell=True)
    except:
        print('Ham module not found!')

def open_eik():
    try:
        subprocess.run("eik_test.py", shell=True)
    except:
        print('Eik module not found!')

def open_kmat():
    try:
        subprocess.run("kmat_test.py", shell=True)
    except:
        print('Kmat module not found!')

def open_mqdt():
    try:
        subprocess.run("mqdt_test.py", shell=True)
    except:
        print('Mqdt module not found!')

def open_dip():
    try:
        subprocess.run("dip_test.py", shell=True)
    except:
        print('Dip module not found!')

def open_others():
    try:
        subprocess.run("others_test.py", shell=True)
    except:
        print('Others module not found!')
    
    

#==================================== Toolbar Menu ===============================
my_menu = Menu(root)
root.config(menu=my_menu)

def file_command():
    pass

def open_command():
    Mov = Toplevel()
    Mov.title('Mov')
    label_mov = Label(Mov, text='Hello world').pack()

def edit_command():
    pass

def options_command():
    pass

def help_command():
    pass

def open_google():
    #webbrowser.open_new('https://accounts.google.com/AccountChooser/signinchooser?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&flowName=GlifWebSignIn&flowEntry=AccountChooser')
    user_OS = platform.system()
    chrome_path_windows = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    chrome_path_linux = '/usr/bin/google-chrome %s'
    chrome_path_mac = 'open -a /Applications/Google\ Chrome.app %s'
    chrome_path = ''
    game_site_link = 'https://www.gamelink'

    if user_OS == 'Windows':
        chrome_path = chrome_path_windows
    elif user_OS == 'Linux':
        chrome_path = chrome_path_linux
    elif user_OS == 'Darwin':
        chrome_path = chrome_path_mac
    elif user_OS == 'Java':
        chrome_path = chrome_path_mac
    else:
        webbrowser.open_new_tab(game_site_link)
    webbrowser.get(chrome_path).open_new_tab(game_site_link)
def open_gmail():
    
    webbrowser.open_new('https://www.google.com/?hl=fr')



    
#Create a menu item
file_menu = Menu(my_menu)
my_menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New File', command=file_command)
file_menu.add_separator()
file_menu.add_command(label='Open', command=open_command)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.destroy)

#Create an edit menu item
edit_menu = Menu(my_menu)
my_menu.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label='Copy', command=edit_command)
edit_menu.add_separator()
edit_menu.add_command(label='Paste', command=root.destroy)

#Create an option menu item
option_menu = Menu(my_menu)
my_menu.add_cascade(label='Options', menu=option_menu)
option_menu.add_command(label='Configure App', command=options_command)
option_menu.add_separator()
option_menu.add_command(label='Code Context', command=root.destroy)

#Create an help menu item
web_menu = Menu(my_menu)
my_menu.add_cascade(label='Web Site', menu=web_menu)
web_menu.add_command(label='Gmail', command=open_gmail)
web_menu.add_separator()
web_menu.add_command(label='Google', command=open_google)

#Create an help menu item
help_menu = Menu(my_menu)
my_menu.add_cascade(label='Help', menu=help_menu)
help_menu.add_command(label='About Apps', command=help_command)
help_menu.add_separator()
help_menu.add_command(label='About Halfium', command=root.destroy)


#==================================== Frames ==============================
def Mov_entered(event):
    Mov_Frame.place(relwidth=0.17, relheight=0.17, relx=0.1, rely=0.27)
    Mov_label = Label(Mov_Frame,text='', bg='#98C0F9', relief=RIDGE).pack()
    
def Mov_leaved(event):
    Mov_Frame.place(relwidth=0.15, relheight=0.15, relx=0.1, rely=0.26)
    Mov_label = Label(Mov_Frame,text='', bg='#98C0F9', relief=RIDGE).pack()

def Bas_entered(event):
    Bas_Frame.place(relwidth=0.17, relheight=0.17, relx=0.3, rely=0.27)
    Bas_label = Label(Bas_Frame,text='', bg='#98C0F9', relief=RIDGE).pack()
    
def Bas_leaved(event):
    Bas_Frame.place(relwidth=0.15, relheight=0.15, relx=0.3, rely=0.26)
    Bas_label = Label(Bas_Frame,text='', bg='#98C0F9', relief=RIDGE).pack()

def Ham_entered(event):
    Ham_Frame.place(relwidth=0.17, relheight=0.17, relx=0.5, rely=0.27)
    Ham_label = Label(Ham_Frame,text='', bg='#98C0F9', relief=RIDGE).pack()
    
def Ham_leaved(event):
    Ham_Frame.place(relwidth=0.15, relheight=0.15, relx=0.5, rely=0.26)
    Ham_label = Label(Ham_Frame,text='', bg='#98C0F9', relief=RIDGE).pack()

def Eik_entered(event):
    Eik_Frame.place(relwidth=0.17, relheight=0.17, relx=0.7, rely=0.27)
    Eik_label = Label(Eik_Frame,text='', bg='#98C0F9', relief=RIDGE).pack()
    
def Eik_leaved(event):
    Eik_Frame.place(relwidth=0.15, relheight=0.15, relx=0.7, rely=0.26)
    Eik_label = Label(Eik_Frame,text='', bg='#98C0F9', relief=RIDGE).pack()

def Kmat_entered(event):
    Kmat_Frame.place(relwidth=0.17, relheight=0.17, relx=0.1, rely=0.53)
    Kmat_label = Label(Kmat_Frame,text='', bg='#98C0F9', relief=RIDGE).pack()
    
def Kmat_leaved(event):
    Kmat_Frame.place(relwidth=0.15, relheight=0.15, relx=0.1, rely=0.52)
    Kmat_label = Label(Kmat_Frame,text='', bg='#98C0F9', relief=RIDGE).pack()

def Mqdt_entered(event):
    Mqdt_Frame.place(relwidth=0.17, relheight=0.17, relx=0.3, rely=0.53)
    Mqdt_label = Label(Mqdt_Frame,text='', bg='#98C0F9', relief=RIDGE).pack()
    
def Mqdt_leaved(event):
    Mqdt_Frame.place(relwidth=0.15, relheight=0.15, relx=0.3, rely=0.52)
    Mqdt_label = Label(Mqdt_Frame,text='', bg='#98C0F9', relief=RIDGE).pack()

def Dip_entered(event):
    Dip_Frame.place(relwidth=0.17, relheight=0.17, relx=0.5, rely=0.53)
    Dip_label = Label(Dip_Frame,text='', bg='#98C0F9', relief=RIDGE).pack()
    
def Dip_leaved(event):
    Dip_Frame.place(relwidth=0.15, relheight=0.15, relx=0.5, rely=0.52)
    Dip_label = Label(Dip_Frame,text='', bg='#98C0F9', relief=RIDGE).pack()

def Others_entered(event):
    Others_Frame.place(relwidth=0.17, relheight=0.17, relx=0.7, rely=0.53)
    Others_label = Label(Others_Frame,text='', bg='#98C0F9', relief=RIDGE).pack()
    
def Others_leaved(event):
    Others_Frame.place(relwidth=0.15, relheight=0.15, relx=0.7, rely=0.52)
    Others_label = Label(Others_Frame,text='', bg='#98C0F9', relief=RIDGE).pack()     
    
    
TitleFrame = Frame(app, bd=3, padx=50, pady=8, bg='white', relief=RAISED, borderwidth = 6)
TitleFrame.place(relwidth=0.6, relheight=0.132, relx=0.194, rely=0)

lebelTitle = Label(TitleFrame, font=('arial', 40, 'bold'), text='  HALFIUM APPLICATION', bg='white')
lebelTitle.grid()

Mov_Frame = Frame(app, bd=1, padx=10, pady=8, bg='#98C0F9', relief=RAISED, borderwidth = 3)
Mov_Frame.place(relwidth=0.15, relheight=0.15, relx=0.1, rely=0.26)
Mov_label = Label(Mov_Frame,text='', bg='#98C0F9').pack()
Mov_Frame.bind("<Enter>",Mov_entered)
Mov_Frame.bind("<Leave>",Mov_leaved)
btn_mov = tk.Button(Mov_Frame, text='Open Mov', padx=2, pady=2, fg="white", bg="#263042", command=open_mov).pack()

Bas_Frame = Frame(app, bd=1, padx=10, pady=8, bg='#98C0F9', relief=RAISED, borderwidth = 3)
Bas_Frame.place(relwidth=0.15, relheight=0.15, relx=0.3, rely=0.26)
Bas_Frame.bind("<Enter>",Bas_entered)
Bas_Frame.bind("<Leave>",Bas_leaved)
btn_bas = tk.Button(Bas_Frame, text='Open Bas', padx=2, pady=2, fg="white", bg="#263042", command=open_bas).pack()

Ham_Frame = Frame(app, bd=1, padx=10, pady=8, bg='#98C0F9', relief=RAISED, borderwidth = 3)
Ham_Frame.place(relwidth=0.15, relheight=0.15, relx=0.5, rely=0.26)
Ham_Frame.bind("<Enter>",Ham_entered)
Ham_Frame.bind("<Leave>",Ham_leaved)
btn_ham = tk.Button(Ham_Frame, text='Open Ham', padx=2, pady=2, fg="white", bg="#263042", command=open_ham).pack()

Eik_Frame = Frame(app, bd=1, padx=10, pady=8, bg='#98C0F9', relief=RAISED, borderwidth = 3)
Eik_Frame.place(relwidth=0.15, relheight=0.15, relx=0.7, rely=0.26)
Eik_Frame.bind("<Enter>",Eik_entered)
Eik_Frame.bind("<Leave>",Eik_leaved)
btn_eik = tk.Button(Eik_Frame, text='Open Eik', padx=2, pady=2, fg="white", bg="#263042", command=open_eik).pack()

Kmat_Frame = Frame(app, bd=1, padx=10, pady=8, bg='#98C0F9', relief=RAISED, borderwidth = 3)
Kmat_Frame.place(relwidth=0.15, relheight=0.15, relx=0.1, rely=0.52)
Kmat_Frame.bind("<Enter>",Kmat_entered)
Kmat_Frame.bind("<Leave>",Kmat_leaved)
btn_kmat = tk.Button(Kmat_Frame, text='Open Kmat', padx=2, pady=2, fg="white", bg="#263042", command=open_kmat).pack()

Mqdt_Frame = Frame(app, bd=1, padx=10, pady=8, bg='#98C0F9', relief=RAISED, borderwidth = 3)
Mqdt_Frame.place(relwidth=0.15, relheight=0.15, relx=0.3, rely=0.52)
Mqdt_Frame.bind("<Enter>",Mqdt_entered)
Mqdt_Frame.bind("<Leave>",Mqdt_leaved)
btn_mqdt = tk.Button(Mqdt_Frame, text='Open Mqdt', padx=2, pady=2, fg="white", bg="#263042", command=open_mqdt).pack()

Dip_Frame = Frame(app, bd=1, padx=10, pady=8, bg='#98C0F9', relief=RAISED, borderwidth = 3)
Dip_Frame.place(relwidth=0.15, relheight=0.15, relx=0.5, rely=0.52)
Dip_Frame.bind("<Enter>",Dip_entered)
Dip_Frame.bind("<Leave>",Dip_leaved)
btn_dip = tk.Button(Dip_Frame, text='Open Dip', padx=2, pady=2, fg="white", bg="#263042", command=open_dip).pack()

Others_Frame = Frame(app, bd=1, padx=10, pady=8, bg='#98C0F9', relief=RAISED, borderwidth = 3)
Others_Frame.place(relwidth=0.15, relheight=0.15, relx=0.7, rely=0.52)
Others_Frame.bind("<Enter>",Others_entered)
Others_Frame.bind("<Leave>",Others_leaved)
btn_others = tk.Button(Others_Frame, text='Others', padx=2, pady=2, fg="white", bg="#263042", command=open_others).pack()


'''#========================================= Insert an image ===================
img = ImageTk.PhotoImage(Image.open('LSAMA.png'))
panel = tk.Label(app, image = img)
panel.place(relwidth=0.077, relheight=0.14, relx=0.45, rely=0.85)'''












app.mainloop()
