from tkinter import*
import numpy as np
from ham_db import Database
import subprocess
import os
import tkinter
import shutil
import multiprocessing
from multiprocessing import Process

ham_db = Database('store.db')


app = Tk()
app.title('Ham Module')
icone = tkinter.PhotoImage(file=r'C:/Ham_HA/Halfium Calc/LSAMA.png')
app.iconphoto(True, icone)

w=600
h=570
ws = app.winfo_screenwidth()
hs = app.winfo_screenheight()
x = (ws/2) - (w/2)    
y = (hs/2) - (h/2)
app.geometry('%dx%d+%d+%d' % (w, h, x, y))

global R
global Xi0
global R_Number
global Xi_Number
global Spin 
global Lambda 
global Parity
global Sym
global Lamda
global Part
global Isy
global Isym

R=[]
Xi0=[]
Spin = []
Lambda = []
Isym = []
Parity = []
Sym = []
Lamda = [(0,'S'),(1,'P'),(2,'D'),(3,'Phi')]
Part = [(0,'g'),(1,'u')]
Isy = [(0,'+'),(1,'-')]

var0 = IntVar() # variable for R radiobutton
var0.set('None')
var1 = IntVar() # variable for Xi0 radiobutton
var1.set('None')

Rval = StringVar()
Rlist = StringVar()
Xi0val = StringVar()
Xi0list = StringVar()
Spin_para = StringVar()
Lambda_para = StringVar()
Isym_para = StringVar()
Parite_para = StringVar()
Iprt_para = StringVar()

#==================================== Toolbar Menu ===============================
ham_menu = Menu(app)
app.config(menu=ham_menu)

def file_command():
    pass

def open_command():
    pass

def edit_command():
    pass

def options_command():
    pass

def help_command():
    pass

#Create a menu item
file_menu = Menu(ham_menu)
ham_menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New File', command=file_command)
file_menu.add_separator()
file_menu.add_command(label='Open', command=open_command)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=app.destroy)

#Create an edit menu item
edit_menu = Menu(ham_menu)
ham_menu.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label='Copy', command=edit_command)
edit_menu.add_separator()
edit_menu.add_command(label='Paste', command=app.destroy)

#Create an option menu item
option_menu = Menu(ham_menu)
ham_menu.add_cascade(label='Options', menu=option_menu)
option_menu.add_command(label='Configure App', command=options_command)
option_menu.add_separator()
option_menu.add_command(label='Code Context', command=app.destroy)

#Create an help menu item
help_menu = Menu(ham_menu)
ham_menu.add_cascade(label='Help', menu=help_menu)
help_menu.add_command(label='About Apps', command=help_command)
help_menu.add_separator()
help_menu.add_command(label='About Halfium', command=app.destroy)




def R_val_entry():
    R_val.configure(state="normal")
    R_list.configure(state="disabled")
    R_val.update()
    R_list.update()

def R_list_entry():
    R_val.configure(state="disabled")
    R_list.configure(state="normal")
    R_val.update()
    R_list.update()

def Xi_val_entry():
    Xi_val.configure(state="normal")
    Xi_list.configure(state="disabled")
    Xi_val.update()
    Xi_list.update()

def Xi_list_entry():
    Xi_val.configure(state="disabled")
    Xi_list.configure(state="normal")
    Xi_val.update()
    Xi_list.update()
    


def clear_fuc():
   listbox.delete(0,END)
   R_val.delete(0,END)
   R_list.delete(0,END)
   Xi_val.delete(0,END)
   Xi_list.delete(0,END)
   Spin_param.delete(0,END)
   Lambda_param.delete(0,END)
   Isym_param.delete(0,END)
   Parite_param.delete(0,END)
   Iprt_param.delete(0,END)
   

def register_fuc():
    ham_db.insert(Rval.get(), Rlist.get(), Xi0val.get(), Xi0list.get(), Spin_para.get(), Lambda_para.get(), Parite_para.get(),Isym_para.get(), Iprt_para.get())
    listbox.delete(0, END)
    if var0.get()==1:
        listbox.insert(1, ("R = "+ Rval.get()))
        R.append(Rval.get())
    else:
        listbox.insert(1, ("R = ["+Rlist.get()+"]"))
        OMG = Rlist.get()
        for i in OMG:
            if i != ',':
                R.append(i)
    if var1.get()==1:
        listbox.insert(2, ("Xi0 = "+Xi0val.get()))
        Xi0.append(Xi0val.get())
    else:
        listbox.insert(2, ( "Xi0 = ["+Xi0list.get()+"]"))
        OMG0 = Xi0list.get()
        for j in OMG0:
            if j != ',':
                Xi0.append(j)
    listbox.insert(4, ("Printing option = " +Iprt_para.get()))            
    listbox.insert(5, ("Spin = "+Spin_para.get() + "; Lambda = " + Lambda_para.get() + "; Isym = " + Isym_para.get() + "; Parity = " + Parite_para.get()))
    OMG1 = Spin_para.get()
    for k in OMG1:
        if k != ',':
            Spin.append(k)
    OMG2 = Lambda_para.get()
    for l in OMG2:
        if l != ',':
            Lambda.append(l)
    OMG3 = Isym_para.get()
    for m in OMG3:
        if m != ',':
            Isym.append(m)
    OMG4 = Parite_para.get()
    for n in OMG4:
        if n != ',':
            Parity.append(n)
            
    

##########################################################################################
#################### Création des dossiers pour chaque R et pour chaque Xi_0 #############
##########################################################################################
    for i in range(len(Xi0)):
        Xi_Number = str(Xi0[i]) #(Xi0=3,5,8,........)
        Xi0_folder = r"C:\Ham_HA\AbsoftHA\xi="+Xi_Number  # xi=3 ; xi=5 ; xi=8; ......
        #os.mkdir(Xi0_folder)
        for j in range(len(R)):
            R_Number = str(R[j]) #(R=1,2,3,........)
            R_folder = Xi0_folder+"\R="+R_Number  # R=1 ; R=2 ; R=3; ........
            mono_folder = R_folder + r"\mono" 
            for a in Spin:
                for b in Lambda:
                    for c in Parity:
                        for d in Isym:
                            def Lamda_eq(var):
                                for N,L in Lamda:
                                    if var!=',':
                                        if var == str(N):
                                            return L
                                return Lamda_eq(b)
                            def Parity_eq(var):
                                for N,L in Part:
                                    if var!=',':
                                        if var == str(N):
                                            return L
                                return Parity_eq(c)
                            def Isym_eq(var):
                                for N,L in Isy:
                                    if var!=',':
                                        if var == str(N):
                                            return L
                                return Isym_eq(d)           
                            Sym = [str(a)+Lamda_eq(b)+Parity_eq(c)+Isym_eq(d)]
                            for k in range(len(Sym)):
                                Symetry_folder = R_folder +'\\' + Sym[k]                      
############ Création du fichier donmov #########################################                             
                                donham = os.open(Symetry_folder + r"\donhamR"+R_Number+"Xi"+str(Xi_Number)+"H2"+ Sym[k] + ".txt", os.O_RDWR|os.O_CREAT ) # openning of the file
                                hamline1 = Iprt_para.get() + "        iprt option d'impression    \n"
                                hamline2 = Symetry_folder + r"\bas.txt" + "\n"
                                hamline3 = mono_folder + r"\ang.txt" + "\n"
                                hamline4 = mono_folder + r"\rad.txt" + "\n"
                                hamline5 = Symetry_folder + r"\nik.txt" + "\n"
                                hamline6 = Symetry_folder + r"\bio.txt" + "\n"
                                hamline7 = Symetry_folder + r"\r12.txt" + "\n"
                                hamline8 = Symetry_folder + r"\ham.txt" + "\n"
                                hamline9 = Symetry_folder + r"\dia.txt" + "\n"

                                hamL1 = str.encode(hamline1)
                                hamL2 = str.encode(hamline2)
                                hamL3 = str.encode(hamline3)
                                hamL4 = str.encode(hamline4)
                                hamL5 = str.encode(hamline5)
                                hamL6 = str.encode(hamline6)
                                hamL7 = str.encode(hamline7)
                                hamL8 = str.encode(hamline8)
                                hamL9 = str.encode(hamline9)
            
                                os.write(donham, hamL1)
                                os.write(donham, hamL2)
                                os.write(donham, hamL3)
                                os.write(donham, hamL4)
                                os.write(donham, hamL5)
                                os.write(donham, hamL6)
                                os.write(donham, hamL7)
                                os.write(donham, hamL8)
                                os.write(donham, hamL9)
                                shutil.copy(Symetry_folder + r"\donhamR"+R_Number+"Xi"+str(Xi_Number)+"H2"+ Sym[k] + ".txt", 'C:\Ham_HA\AbsoftHA\ham\Debug')
                                os.close(donham)
                                listbox.insert(6, ("Closed donhamR"+R_Number+"Xi"+str(Xi_Number)+"H2"+ Sym[k] + ".txt file successfully!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"))


def run_all():
    def exec_calc(cmd):
        p= subprocess.Popen(["start", "cmd", "/c",cmd], shell = True,stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE,bufsize=1)
        while True:
            line = p.stdout.readline()
            if line:
                print(line)
            if not line:
                break
            
    for i in range(len(Xi0)):
        Xi_Number = str(Xi0[i]) #(Xi0=3,5,8,........)
        Xi0_folder = r"C:\Ham_HA\AbsoftHA\xi="+Xi_Number  # xi=3 ; xi=5 ; xi=8; ......
        #os.mkdir(Xi0_folder)
        for j in range(len(R)):
            R_Number = str(R[j]) #(R=1,2,3,........)
            R_folder = Xi0_folder+"\R="+R_Number  # R=1 ; R=2 ; R=3; ........
            mono_folder = R_folder + r"\mono"
            try:
                cmd1 = "cd\ && cd Ham_HA\AbsoftHA\mov\Debug && mov.exe <donmovR"+str(R_Number)+"Xi"+str(Xi_Number)+"H2.txt"
                if os.path.exists(r"C:\Ham_HA\AbsoftHA\mov\Debug\donmovR" + str(R_Number)+"Xi"+str(Xi_Number)+"H2.txt"):
                    exec_calc(cmd1)
                else:
                    listbox.insert(6+i*j, ("donmovR" + str(R_Number)+"Xi"+str(Xi_Number)+"H2.txt file not found !" ) )     
            except:
                j+=1 # if file R=R[j] exist then j+=1
                listbox.insert(6+i*j+i+j, ("The donmovR" + str(R_Number)+"Xi"+str(Xi_Number)+"H2.txt file is already exist"))
                if j==len(R):
                    break
            for a in Spin:
                for b in Lambda:
                    for c in Parity:
                        for d in Isym:
                            def Lamda_eq(var):
                                for N,L in Lamda:
                                    if var!=',':
                                        if var == str(N):
                                            return L
                                return Lamda_eq(b)
                            def Parity_eq(var):
                                for N,L in Part:
                                    if var!=',':
                                        if var == str(N):
                                            return L
                                return Parity_eq(c)
                            def Isym_eq(var):
                                for N,L in Isy:
                                    if var!=',':
                                        if var == str(N):
                                            return L
                                return Isym_eq(d)           
                            Sym = [str(a)+Lamda_eq(b)+Parity_eq(c)+Isym_eq(d)]
                            for k in range(len(Sym)):
                                try:
                                    cmd2 = "cd\ && cd Ham_HA/AbsoftHA/bas/Debug && bas.exe <donbasR"+str(R_Number)+"Xi"+str(Xi_Number)+"H2"+ Sym[k] + ".txt" 
                                    if os.path.exists(r"C:\Ham_HA\AbsoftHA\bas\Debug\donbasR"+str(R_Number)+"Xi"+str(Xi_Number)+"H2"+ Sym[k]+ ".txt"):
                                        exec_calc(cmd2)
                                    else:
                                        listbox.insert(6+i*j+i+j, ("donbasR"+str(R_Number)+"Xi"+str(Xi_Number)+"H2"+ str(Sym[k]) + ".txt not found !" ))      
                                except:
                                    k+=1 # if file R=R[j] exist then j+=1
                                    listbox.insert(6+i*j+i+j+k, ("The donbasR"+str(R_Number)+"Xi"+str(Xi_Number)+"H2"+ Sym[k]+ ".txt file is already calculated"))
                                    if k==len(Sym):
                                        break

                                try:
                                    cmd3 = "cd\ && cd Ham_HA\AbsoftHA\ham\Debug && ham.exe <donhamR"+str(R_Number)+"Xi"+str(Xi_Number)+"H2"+ Sym[k] + ".txt" 
                                    if os.path.exists(r"C:\Ham_HA\AbsoftHA\ham\Debug\donhamR"+str(R_Number)+"Xi"+str(Xi_Number)+"H2"+ Sym[k]+ ".txt" ):
                                        exec_calc(cmd3)
                                    else:
                                        listbox.insert(6+i*j+i+j+k, ("donhamR"+str(R_Number)+"Xi"+str(Xi_Number)+"H2"+ str(Sym[k]) + ".txt not found !" ))      
                                except:
                                    k+=1 # if file R=R[j] exist then j+=1
                                    listbox.insert(6+i*j+i+j*k, ("donhamR"+str(R_Number)+"Xi"+str(Xi_Number)+"H2"+ Sym[k] + ".txt file is already calculated"))
                                    if k==len(Sym):
                                        break   
                                        
def run_ham():
    def exec_calc(cmd):
        p= subprocess.Popen(["start", "cmd", "/c",cmd], shell = True,stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        while True:
            line = p.stdout.readline()
            if line:
                print(line)
            if not line:
                break
            
    for i in range(len(Xi0)):
        Xi_Number = str(Xi0[i]) #(Xi0=3,5,8,........)
        Xi0_folder = r"C:\Ham_HA\AbsoftHA\xi="+Xi_Number  # xi=3 ; xi=5 ; xi=8; ......
        #os.mkdir(Xi0_folder)
        for j in range(len(R)):
            R_Number = str(R[j]) #(R=1,2,3,........)
            R_folder = Xi0_folder+"\R="+R_Number  # R=1 ; R=2 ; R=3; ........
            mono_folder = R_folder + r"\mono"
            for a in Spin:
                for b in Lambda:
                    for c in Parity:
                        for d in Isym:
                            def Lamda_eq(var):
                                for N,L in Lamda:
                                    if var!=',':
                                        if var == str(N):
                                            return L
                                return Lamda_eq(b)
                            def Parity_eq(var):
                                for N,L in Part:
                                    if var!=',':
                                        if var == str(N):
                                            return L
                                return Parity_eq(c)
                            def Isym_eq(var):
                                for N,L in Isy:
                                    if var!=',':
                                        if var == str(N):
                                            return L
                                return Isym_eq(d)           
                            Sym = [str(a)+Lamda_eq(b)+Parity_eq(c)+Isym_eq(d)]
                            for k in range(len(Sym)):
                                try:
                                    cmd_ham = "cd\ && cd Ham_HA\AbsoftHA\ham\Debug && ham.exe <donhamR"+str(R_Number)+"Xi"+str(Xi_Number)+"H2"+ Sym[k] + ".txt" 
                                    if os.path.exists(r"C:\Ham_HA\AbsoftHA\ham\Debug\donhamR"+str(R_Number)+"Xi"+str(Xi_Number)+"H2"+ Sym[k]+ ".txt"):
                                        exec_calc(cmd_ham)
                                    else:
                                        listbox.insert(6+i*j+i+j*k, ("donhamR"+str(R_Number)+"Xi"+str(Xi_Number)+"H2"+ str(Sym[k]) + ".txt not found !" ))      
                                except:
                                    k+=1 # if file R=R[j] exist then j+=1
                                    listbox.insert(6+i*j+i+j*k, ("donhamR"+str(R_Number)+"Xi"+str(Xi_Number)+"H2"+ Sym[k] + ".txt file is already calculated"))
                                    if k==len(Sym):
                                        break         
               
                                     


                                   
#Radiobutton for R distance 
Label(app, text = "Select R distance").grid(row=1, column=0, sticky=W)
Radiobutton(app, text = "Single value", variable = var0, value = 1, width=10,font=('bold',9), command = R_val_entry).grid(row=0, column=1,sticky=W)
Radiobutton(app, text = "List of values", variable = var0, value = 2,width=25, command = R_list_entry).grid(row=0, column=2,sticky=W)
R_val = Entry(app, textvariable=Rval, width=10)
R_val.grid(row=1, column=1, ipadx=1, ipady=4,sticky=W)
R_val.delete(0, END) # clear the entry field
R_list = Entry(app, textvariable=Rlist, width=25)
R_list.grid(row=1, column=2, ipadx=1, ipady=4)
R_list.delete(0, END) # clear the entry field

#Radiobutton for Xi0
Label(app, text = " ").grid(row=2, column=0, sticky=W)
Label(app, text = "Select Xi0").grid(row=4, column=0, sticky=W)
Radiobutton(app, text = "Single value", variable = var1, value = 1, width=10,font=('bold',9), command = Xi_val_entry).grid(row=3, column=1,sticky=W)
Radiobutton(app, text = "List of values", variable = var1, value = 2,width=25, command = Xi_list_entry).grid(row=3, column=2,sticky=W)
Xi_val = Entry(app, textvariable=Xi0val, width=10)
Xi_val.grid(row=4, column=1, ipadx=1, ipady=4,sticky=W)
Xi_val.delete(0, END) # clear the entry field
Xi_list = Entry(app, textvariable=Xi0list, width=25)
Xi_list.grid(row=4, column=2, ipadx=1, ipady=4)
Xi_list.delete(0, END) # clear the entry field

# Others parameters
Label(app, text = "").grid(row=5, column=1,sticky=W)
Label(app, text = "Printing option").grid(row=7, column=0,sticky=W)
Iprt_param = Entry(app, textvariable=Iprt_para, width=10)
Iprt_param.grid(row=7, column=1, ipadx=1, ipady=4,sticky=W)
Iprt_param.delete(0, END) # clear the entry field

#Radiobutton for Symetries
Label(app, text = " ").grid(row=8, column=0, sticky=W)
Label(app, text = "Spin").grid(row=9, column=1,sticky=W)
Label(app, text = "Lambda").grid(row=9, column=2,sticky=W)
Label(app, text = "Symetries",width=10).grid(row=12, column=0,sticky=W)
Spin_param = Entry(app, textvariable=Spin_para, width=10)
Spin_param.grid(row=10, column=1, ipadx=1, ipady=4,sticky=W)
Spin_param.delete(0, END) # clear the entry field
Lambda_param = Entry(app, textvariable=Lambda_para, width=10)
Lambda_param.grid(row=10, column=2, ipadx=1, ipady=4,sticky=W)
Lambda_param.delete(0, END) # clear the entry field
Label(app, text = "Parity").grid(row=12, column=1,sticky=W)
Label(app, text = "Isym").grid(row=12, column=2,sticky=W)
Isym_param = Entry(app, textvariable=Isym_para, width=10)
Isym_param.grid(row=13, column=1, ipadx=1, ipady=4,sticky=W)
Isym_param.delete(0, END) # clear the entry field
Parite_param = Entry(app, textvariable=Parite_para, width=10)
Parite_param.grid(row=13, column=2, ipadx=1, ipady=4,sticky=W)
Parite_param.delete(0, END) # clear the entry field


#Buttons
Label(app, text = " ").grid(row=14, column=2, sticky=W)
clear_btn = Button(app, text = "Clear Input",width=10, command = clear_fuc).grid(row=15,column=0,columnspan=4,ipadx=60, ipady=1,sticky=W)
register_btn = Button(app, text = "Register",width=10, command = register_fuc).grid(row=15,column=2,columnspan=4,ipadx=65, ipady=1)
run_ham = Button(app, text = "Run Ham",width=10, command = run_ham).grid(row=16,column=0,columnspan=4,ipadx=60, ipady=1,sticky=W)
run_btn = Button(app, text = "Run All",width=10, command = run_all).grid(row=16,column=2,columnspan=4,ipadx=65, ipady=1)

#Listbox)
listbox = Listbox(app, height=8, width=65, border=3)
listbox.grid(row=17, column=0,columnspan=3, pady=10, padx=10,sticky=W)

# Creating a Y Scrollbar 
Yscrollbar = Scrollbar(app)
Yscrollbar.grid(row=17, column=3,columnspan=4,ipady=40, sticky=W)#(side = RIGHT, fill = BOTH)
listbox.config(yscrollcommand = Yscrollbar.set)  
Yscrollbar.config(command = listbox.yview)


# Creating a X Scrollbar   
Xscrollbar = Scrollbar(app,orient=HORIZONTAL)
Xscrollbar.grid(row=18, column=0,columnspan=3,sticky=E+W)#(side = RIGHT, fill = BOTH)
listbox.config(xscrollcommand = Xscrollbar.set)  
Xscrollbar.config(command = listbox.xview)

mainloop()

