from tkinter import*
import numpy as np
from bas_db import Database
import subprocess
import os
import tkinter
import shutil
import multiprocessing
from multiprocessing import Process

bas_db = Database('store.db')


app = Tk()
app.title('Bas Module')
icone = tkinter.PhotoImage(file=r'C:/Ham_HA/Halfium Calc/LSAMA.png')
app.iconphoto(True, icone)

w=650
h=650
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
global E_coupure
global Sym
global Lamda
global Part
global Isy
global Isym

E_coupure = 15
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
Mol_sym = StringVar()
Nbas_max = StringVar()
Open_func = StringVar()
    
#==================================== Toolbar Menu ===============================
bas_menu = Menu(app)
app.config(menu=bas_menu)

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

#Create a menu item
file_menu = Menu(bas_menu)
bas_menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New File', command=file_command)
file_menu.add_separator()
file_menu.add_command(label='Open', command=open_command)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=app.destroy)

#Create an edit menu item
edit_menu = Menu(bas_menu)
bas_menu.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label='Copy', command=edit_command)
edit_menu.add_separator()
edit_menu.add_command(label='Paste', command=app.destroy)

#Create an option menu item
option_menu = Menu(bas_menu)
bas_menu.add_cascade(label='Options', menu=option_menu)
option_menu.add_command(label='Configure App', command=options_command)
option_menu.add_separator()
option_menu.add_command(label='Code Context', command=app.destroy)

#Create an help menu item
help_menu = Menu(bas_menu)
bas_menu.add_cascade(label='Help', menu=help_menu)
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
   Molsym.delete(0,END)
   Nbasmax.delete(0,END)
   Openfunc.delete(0,END)
   

def register_fuc():
    bas_db.insert(Rval.get(), Rlist.get(), Xi0val.get(), Xi0list.get(), Spin_para.get(), Lambda_para.get(), Parite_para.get(),Isym_para.get(), Mol_sym.get(), Nbas_max.get(), Open_func.get())
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
    listbox.insert(4, ("Spin = "+Spin_para.get() + "; Lambda = " + Lambda_para.get() + "; Isym = " + Isym_para.get() + "; Parity = " + Parite_para.get()))
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
            
    listbox.insert(5, ("Mol Sym = " +Mol_sym.get()+"; Num Bas Max = " + Nbas_max.get()+ "; Open Func = " + Open_func.get()))
    

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
                                try:
                                    if not os.path.exists(Symetry_folder):
                                        os.makedirs(os.path.join(Symetry_folder))
                                except:                                                   
                                    listbox.insert(5+j+i+k, ("The " + Sym[k]+ " folder for Xi = "+ Xi_Number + " and R = " + R_Number + " is already exist"))
                                    k+=1 # if file R=R[j] exist then j+=1
                                    if k==len(Sym):
                                             break                       
############ Création du fichier donmov #########################################                             
                                donbas = os.open(Symetry_folder + r"\donbasR"+R_Number+"Xi"+str(Xi0[i])+"H2"+ Sym[k] + ".txt", os.O_RDWR|os.O_CREAT ) # openning of the file
                                basline1 = mono_folder + r"\rad.txt" + "\n"
                                basline2 = mono_folder + r"\over.txt" + "\n"
                                basline3 = Symetry_folder + r"\bas.txt" + "\n"
                                basline4 = Symetry_folder + r"\bio.txt" + "\n"
                                basline5 = Symetry_folder + r"\nik.txt" + "\n"
                                basline6 = Symetry_folder + r"\nikbar.txt" + "\n"
                                basline7 = str(a) + "    spin   \n"
                                basline8 = str(b) + "    lambda   \n"
                                basline9 = str(Mol_sym.get()) + "    molsym   \n"
                                basline10 = str(c) + "    parité (0 pour g et 1 pour u)  \n"
                                basline11 = str(d) + "    isym +/-  (0 pour + et 1 pour -)  \n"
                                basline12 = str(Nbas_max.get()) + "    nbasmax taille maximale desiree    \n"
                                basline13 = str(E_coupure) + "    energie de coupure en Rydberg    \n"
                                basline14 = str(Open_func.get()) + "    nombre de fonction ouvertes    \n"

                                basL1 = str.encode(basline1)
                                basL2 = str.encode(basline2)
                                basL3 = str.encode(basline3)
                                basL4 = str.encode(basline4)
                                basL5 = str.encode(basline5)
                                basL6 = str.encode(basline6)
                                basL7 = str.encode(basline7)
                                basL8 = str.encode(basline8)
                                basL9 = str.encode(basline9)
                                basL10 = str.encode(basline10)
                                basL11 = str.encode(basline11)
                                basL12 = str.encode(basline12)
                                basL13 = str.encode(basline13)
                                basL14 = str.encode(basline14)
            
                                os.write(donbas, basL1)
                                os.write(donbas, basL2)
                                os.write(donbas, basL3)
                                os.write(donbas, basL4)
                                os.write(donbas, basL5)
                                os.write(donbas, basL6)
                                os.write(donbas, basL7)
                                os.write(donbas, basL8)
                                os.write(donbas, basL9)
                                os.write(donbas, basL10)
                                os.write(donbas, basL11)
                                os.write(donbas, basL12)
                                os.write(donbas, basL13)
                                os.write(donbas, basL14)
                                shutil.copy(Symetry_folder + r"\donbasR"+R_Number+"Xi"+str(Xi0[i])+"H2"+ str(Sym[k]) + ".txt", 'C:/Ham_HA/AbsoftHA/bas/Debug')
                                os.close(donbas)
                                listbox.insert(5+i*j*k, ("Closed donbasR"+R_Number+"Xi"+str(Xi0[i])+"H2"+ str(Sym[k]) + ".txt  file successfully!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"))


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
                    listbox.insert(5+i+j+i*j*k, ("donmovR" + str(R_Number)+"Xi"+str(Xi_Number)+"H2.txt" + " not found !" ) )     
            except:
                j+=1 # if file R=R[j] exist then j+=1
                listbox.insert(5+i+j+i*j*k, ("The donmovR" + str(R_Number)+"Xi"+str(Xi_Number)+"H2.txt file is already calculated"))
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
                                    if os.path.exists(r"C:\Ham_HA\AbsoftHA\bas\Debug\donbasR"+str(R_Number)+"Xi"+str(Xi_Number)+"H2"+ Sym[k] + ".txt"):
                                        exec_calc(cmd2)
                                    else:
                                        listbox.insert(5+i+j+i*j*k, ("donbasR"+str(R_Number)+"Xi"+str(Xi_Number)+"H2"+ str(Sym[k]) + ".txt" + " not found !" ))      
                                except:
                                    k+=1 # if file R=R[j] exist then j+=1
                                    listbox.insert(5+i+j+i*j*k, ("The donbasR"+str(R_Number)+"Xi"+str(Xi_Number)+"H2"+ str(Sym[k]) + ".txt file is already exist"))
                                    if k==len(Sym):
                                        break       
                                        
def run_bas():
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
                                    cmd_bas = "cd\ && cd Ham_HA/AbsoftHA/bas/Debug && bas.exe <donbasR"+str(R_Number)+"Xi"+str(Xi_Number)+"H2"+ Sym[k] + ".txt" 
                                    #if os.path.exists(r"C:\Ham_HA\AbsoftHA\mov\Debug\donbasR"+str(R_Number)+"Xi"+str(Xi_Number)+"H2"+ Sym[k]):
                                    #p = subprocess.Popen(command2,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                                    exec_calc(cmd_bas)
                                    #else:
                                        #print("donbasR"+str(R_Number)+"Xi"+str(Xi_Number)+"H2"+ str(Sym[k]) + ".txt" + " not found !" )      
                                except:
                                    k+=1 # if file R=R[j] exist then j+=1
                                    listbox.insert(5+i+j+i*j*k, ("The donbasR"+str(R_Number)+"Xi"+str(Xi_Number)+"H2"+ Sym[k] + ".txt file is already calculated"))
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

#Radiobutton for Symetries
Label(app, text = " ").grid(row=5, column=0, sticky=W)
Label(app, text = "Spin").grid(row=7, column=1,sticky=W)
Label(app, text = "Lambda").grid(row=7, column=2,sticky=W)
Label(app, text = "Symetries",width=10).grid(row=9, column=0,sticky=W)
Spin_param = Entry(app, textvariable=Spin_para, width=10)
Spin_param.grid(row=8, column=1, ipadx=1, ipady=4,sticky=W)
Spin_param.delete(0, END) # clear the entry field
Lambda_param = Entry(app, textvariable=Lambda_para, width=10)
Lambda_param.grid(row=8, column=2, ipadx=1, ipady=4,sticky=W)
Lambda_param.delete(0, END) # clear the entry field
Label(app, text = "Parity").grid(row=9, column=1,sticky=W)
Label(app, text = "Isym").grid(row=9, column=2,sticky=W)
Isym_param = Entry(app, textvariable=Isym_para, width=10)
Isym_param.grid(row=10, column=1, ipadx=1, ipady=4,sticky=W)
Isym_param.delete(0, END) # clear the entry field
Parite_param = Entry(app, textvariable=Parite_para, width=10)
Parite_param.grid(row=10, column=2, ipadx=1, ipady=4,sticky=W)
Parite_param.delete(0, END) # clear the entry field

# Others parameters
Label(app, text = "").grid(row=11, column=1,sticky=W)
Label(app, text = "Mol-Sym").grid(row=12, column=1,sticky=W)
Label(app, text = "NbasMax").grid(row=12, column=2,sticky=W)
Label(app, text = "Op-Fuc-Num").grid(row=12, column=3,sticky=W)
Label(app, text = "Rest of Parameters").grid(row=13, column=0,sticky=W)
Molsym = Entry(app, textvariable=Mol_sym, width=10)
Molsym.grid(row=13, column=1, ipadx=1, ipady=4,sticky=W)
Molsym.delete(0, END) # clear the entry field
Nbasmax = Entry(app, textvariable=Nbas_max, width=10)
Nbasmax.grid(row=13, column=2, ipadx=1, ipady=4,sticky=W)
Nbasmax.delete(0, END) # clear the entry field
Openfunc = Entry(app, textvariable=Open_func, width=10)
Openfunc.grid(row=13, column=3, ipadx=1, ipady=4,sticky=W)
Openfunc.delete(0, END) # clear the entry field




#Listbox)
Label(app, text = " ").grid(row=14, column=2, sticky=W)
listbox = Listbox(app, height=9, width=70, border=3)
listbox.grid(row=15, column=0,columnspan=3, pady=10, padx=10,sticky=W)

# Creating a Y Scrollbar 
Yscrollbar = Scrollbar(app)
Yscrollbar.grid(row=15, column=3,columnspan=4,ipady=40, sticky=W)#(side = RIGHT, fill = BOTH)
listbox.config(yscrollcommand = Yscrollbar.set)  
Yscrollbar.config(command = listbox.yview)


# Creating a X Scrollbar   
Xscrollbar = Scrollbar(app,orient=HORIZONTAL)
Xscrollbar.grid(row=17, column=0,columnspan=3,sticky=E+W)#(side = RIGHT, fill = BOTH)
listbox.config(xscrollcommand = Xscrollbar.set)  
Xscrollbar.config(command = listbox.xview)



#Buttons
Label(app, text = " ").grid(row=18, column=2, sticky=W)
clear_btn = Button(app, text = "Clear Input",width=10, command = clear_fuc).grid(row=19,ipadx=10, ipady=4)
register_btn = Button(app, text = "Register",width=10, command = register_fuc).grid(row=19,column=1,ipadx=10, ipady=4)
run_bas = Button(app, text = "Run Bas",width=10, command = run_bas).grid(row=19,column=2,ipadx=10, ipady=4,sticky=W)
Label(app, text = " ").grid(row=20, column=2, sticky=W)
run_btn = Button(app, text = "Run All",width=10, command = run_all).grid(row=21,column=0,ipadx=10, ipady=4)


mainloop()

