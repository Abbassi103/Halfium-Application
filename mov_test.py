#!/usr/bin/python
# -*- coding: utf-8 -*-
from tkinter import*
import numpy as np
from mov_db import Database
import subprocess
import os
import tkinter
import shutil
import tkinter.messagebox as msg

mov_db = Database('store.db')

app = Tk()
app.title('Mov Module')
icone = tkinter.PhotoImage(file=r'C:/Ham_HA/Halfium Calc/LSAMA.png')
app.iconphoto(True, icone)

#============== Variables ========================
w=600
h=600
ws = app.winfo_screenwidth()
hs = app.winfo_screenheight()
x = (ws/2) - (w/2)    
y = (hs/2) - (h/2)
app.geometry('%dx%d+%d+%d' % (w, h, x, y))

global R
global Xi0
global Pas
global R_Number
global Xi_Number
global mov_exe

mov_exe = ['mov1.exe','mov2.exe','mov3.exe','mov4.exe','mov5.exe']
R=[]
Xi0=[]
Pas = 8000
var0 = IntVar() # variable for R radiobutton
var0.set('None')
var1 = IntVar() # variable for Xi0 radiobutton
var1.set('None')

Rval = StringVar()
Rlist = StringVar()
Xi0_val = StringVar()
Xi0_list = StringVar()
Z1 = StringVar()
Z2 = StringVar()
n = StringVar()
l = StringVar()
m = StringVar()
nco = StringVar()
nop = StringVar()

#==================================== Toolbar Menu ===============================
mov_menu = Menu(app)
app.config(menu=mov_menu)

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
file_menu = Menu(mov_menu)
mov_menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New File', command=file_command)
file_menu.add_separator()
file_menu.add_command(label='Open', command=open_command)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=app.destroy)

#Create an edit menu item
edit_menu = Menu(mov_menu)
mov_menu.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label='Copy', command=edit_command)
edit_menu.add_separator()
edit_menu.add_command(label='Paste', command=app.destroy)

#Create an option menu item
option_menu = Menu(mov_menu)
mov_menu.add_cascade(label='Options', menu=option_menu)
option_menu.add_command(label='Configure App', command=options_command)
option_menu.add_separator()
option_menu.add_command(label='Code Context', command=app.destroy)

#Create an help menu item
help_menu = Menu(mov_menu)
mov_menu.add_cascade(label='Help', menu=help_menu)
help_menu.add_command(label='About Apps', command=help_command)
help_menu.add_separator()
help_menu.add_command(label='About Halfium', command=app.destroy)



#========================= Functions ============================
def populate_list():
    listbox.delete(0, END)
    for row in mov_db.fetch():
        listbox.insert(END, row)
    

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
   Z1_val.delete(0,END)
   Z2_val.delete(0,END)
   n_val.delete(0,END)
   l_val.delete(0,END)
   m_val.delete(0,END)
   nco_val.delete(0,END)
   nop_val.delete(0,END)

def register_fuc():
    mov_db.insert(Rval.get(), Rlist.get(),Xi0_val.get(), Xi0_list.get(),Z1.get(), Z2.get(), n.get(), l.get(),m.get(), nco.get(), nop.get())
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
        listbox.insert(2, ("Xi0 = "+Xi0_val.get()))
        Xi0.append(Xi0_val.get())
    else:
        listbox.insert(2, ( "Xi0 = ["+Xi0_list.get()+"]"))
        OMG0 = Xi0_list.get()
        for j in OMG0:
            if j != ',':
                Xi0.append(j)
    listbox.insert(3, ("Z1 = "+Z1.get() + "; Z2 = "+Z2.get() + "; n = "+n.get() + "; l = "+l.get() + "; m = "+m.get() + "; nco = "+nco.get() + "; nop = "+nop.get()))
    
############################################################################################################################################
#################### Création des dossiers pour chaque R et pour chaque Xi_0 ###############################################################
############################################################################################################################################
    for i in range(len(Xi0)):
        Xi_Number = str(Xi0[i]) #(Xi0=3,5,8,........) 
        Xi0_folder = r"C:\Ham_HA\AbsoftHA\xi="+Xi_Number  # xi=3 ; xi=5 ; xi=8; ......
        try:
            os.mkdir(Xi0_folder)
        except:
            i+=1 # if file xi=Xi0[i] exist then i+=1
            listbox.insert(3+i,("The folder xi = " + str(Xi_Number) + " is already exist"))
            if i==len(Xi0):
                break
        for j in range(len(R)):
            R_Number = str(R[j]) #(R=1,2,3,........)
            R_folder = Xi0_folder+"\R="+R_Number  # R=1 ; R=2 ; R=3; ........
            mono_folder = R_folder + r"\mono"
            try:
                os.mkdir(R_folder)
                os.mkdir(mono_folder)
            except:
                j+=1 # if file R=R[j] exist then j+=1
                listbox.insert(5+i+j,("The folder R = " + str(R_Number) + " is already exist"))
                if j==len(R):
                    break
############ Création du fichier donmov #########################################        
            donmov = os.open(mono_folder + r"\donmovR"+R_Number+"Xi"+str(Xi_Number)+"H2.txt", os.O_RDWR|os.O_CREAT) # openning of the file        
            movline1 = mono_folder + r"\rad.txt" + "\n"
            movline2 = mono_folder + r"\ang.txt" + "\n"
            movline3 = mono_folder + r"\over.txt" + "\n"
            movline4 = mono_folder + r"\dip.txt" + "\n"
            movline5 = R_Number + "     R(u.a.)\n"
            movline6 = str(Z1.get()) +". "+ str(Z2.get()) + ".   z1  z2 \n"
            movline7 = str(0) + "       iprt \n"
            movline8 = str('1.d-1') + "   " + str('1.d-6') + "    debu eps \n"
            movline9 = str(float(Xi0[i])/Pas)+ " " + str(float(Xi0[i])/Pas) + " " + str(float(Xi0[i])-1) + " " + str(.01) + " " + str(0.) + " " + str(-0.0000) + " " + str(0.) + " " + str(0) +   "    hmin hmax rmax rbegf rendf rcr emax nthm \n "
            movline10 = str(4) + "     nmo  \n"   
            movline11 = str(0)+ " " + str(0) + " " + str(4) + "         m=0    l=0-4         mm  ldeb  lfin  \n"
            movline12 = str(1)+ " " + str(1) + " " + str(4) + "         m=1    l=1-4         mm  ldeb  lfin  \n"
            movline13 = str(2)+ " " + str(2) + " " + str(4) + "         m=2    l=2-4         mm  ldeb  lfin  \n"
            movline14 = str(3)+ " " + str(3) + " " + str(4) + "         m=3    l=3-4         mm  ldeb  lfin  \n"
            movline15 = str(nco.get())+ " " + str(nop.get()) + "        nco=10 nop=0  \n"
            movline16 = str(1)+ "       0 sans 1 avec moments dipolaires  \n" 


            movL1 = str.encode(movline1)
            movL2 = str.encode(movline2)
            movL3 = str.encode(movline3)
            movL4 = str.encode(movline4)
            movL5 = str.encode(movline5)
            movL6 = str.encode(movline6)
            movL7 = str.encode(movline7)
            movL8 = str.encode(movline8)
            movL9 = str.encode(movline9)
            movL10 = str.encode(movline10)
            movL11 = str.encode(movline11)
            movL12 = str.encode(movline12)
            movL13 = str.encode(movline13)
            movL14 = str.encode(movline14)
            movL15 = str.encode(movline15)
            movL16 = str.encode(movline16)

            os.write(donmov, movL1)
            os.write(donmov, movL2)
            os.write(donmov, movL3)
            os.write(donmov, movL4)
            os.write(donmov, movL5)
            os.write(donmov, movL6)
            os.write(donmov, movL7)
            os.write(donmov, movL8)
            os.write(donmov, movL9)
            os.write(donmov, movL10)
            os.write(donmov, movL11)
            os.write(donmov, movL12)
            os.write(donmov, movL13)
            os.write(donmov, movL14)
            os.write(donmov, movL15)
            os.write(donmov, movL16)
            shutil.copy(mono_folder + r"\donmovR"+R_Number+"Xi"+str(Xi_Number)+"H2.txt", 'C:/Ham_HA/AbsoftHA/mov/Debug')                     
            os.close( donmov)
            listbox.insert(4+i*j,("Closed donmovR"+R_Number+"Xi"+str(Xi_Number)+"H2.txt file successfully!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"))
            

def run_fuc():
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
        for j in range(len(R)):
            R_Number = str(R[j]) #(R=1,2,3,........)
            R_folder = Xi0_folder+"\R="+R_Number  # R=1 ; R=2 ; R=3; ........
            mono_folder = R_folder + r"\mono"
            try:
                cmd = "cd\ && cd Ham_HA\AbsoftHA\mov\Debug && mov.exe <donmovR"+str(R_Number)+"Xi"+str(Xi_Number)+"H2.txt"
                if os.path.exists(r"C:\Ham_HA\AbsoftHA\mov\Debug\donmovR" + str(R_Number)+"Xi"+str(Xi_Number)+"H2.txt"):
                    exec_calc(cmd)
                else:
                    listbox.insert(5+i+j, ("donmovR" + str(R_Number)+"Xi"+str(Xi_Number)+"H2.txt" + " not found !" ) )     
            except:
                j+=1 # if file R=R[j] exist then j+=1
                listbox.insert(5+i+j, ("The donmovR" + str(R_Number)+"Xi"+str(Xi_Number)+"H2.txt file is already calculated"))
                if j==len(R):
                    break
            '''R_Xi=[(R[j],Xi0[i])]   
            for N_R,N_Xi0 in R_Xi:
                for k in range(len(R_Xi)):
                    try:
                        shutil.copy(mono_folder + r"\donmovR"+str(N_R[k])+"Xi"+str(N_Xi0[k])+"H2.txt", "C:\Ham_HA\AbsoftHA\mov"+str[k]+"\Debug")
                        command1 = "cd\ && cd Ham_HA\AbsoftHA\mov"+str[k]+"\Debug && mov.exe <donmovR"+str(N_R[k])+"Xi"+str(N_Xi0[k])+"H2.txt"
                        #if os.path.exists(r"C:\Ham_HA\AbsoftHA\mov1\Debug\donmovR" + str(N_R[k])+"Xi"+str(N_Xi0[k])+"H2.txt"):
                        exec_mov(command1)
                            #p= subprocess.Popen(["start", "cmd", "/c",command1], shell = True,stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                        #else:
                            #listbox.insert(6,("donmovR" + str(N_R[k])+"Xi"+str(N_Xi0[k])+"H2.txt  not found !" ))
                    except:
                        print("donmovR" + str(N_R[k])+"Xi"+str(N_Xi0[k])+"H2.txt is calculated")
                        if k==len(R_Xi):
                            break    
                    k==2
                    try:
                        shutil.copy(mono_folder + r"\donmovR"+str(N_R[k])+"Xi"+str(N_Xi0[k])+"H2.txt", "C:\Ham_HA\AbsoftHA\mov2\Debug")
                        command2 = "cd\ && cd Ham_HA\AbsoftHA\mov2\Debug && mov.exe <donmovR"+str(N_R[k])+"Xi"+str(N_Xi0[k])+"H2.txt"
                        if os.path.exists(r"C:\Ham_HA\AbsoftHA\mov2\Debug\donmovR" + str(N_R[k])+"Xi"+str(N_Xi0[k])+"H2.txt"):
                                    #exec_calc(command1)
                            p= subprocess.Popen(["start", "cmd", "/c",command2], shell = True,stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                        else:
                            listbox.insert(7,("donmovR" + str(N_R[k])+"Xi"+str(N_Xi0[k])+"H2.txt  not found !" ))
                    except:
                        print("donmovR" + str(N_R[k])+"Xi"+str(N_Xi0[k])+"H2.txt is calculated")
                        k+=5
                        if k==len(R_Xi):
                            break 
                    
                        
                    k+=5
                    if k==len(R_Xi):
                        break
                    try:
                        shutil.copy(mono_folder + r"\donmovR"+str(N_R[k])+"Xi"+str(N_Xi0[k])+"H2.txt", "C:\Ham_HA\AbsoftHA\mov"+str(k)+"\Debug")
                        command = "cd\ && cd Ham_HA\AbsoftHA\mov"+str(k)+"\Debug && mov.exe <donmovR"+str(N_R[k])+"Xi"+str(N_Xi0[k])+"H2.txt"
                        if os.path.exists(r"C:\Ham_HA\AbsoftHA\mov"+str(k)+"\Debug\donmovR" + str(N_R[k])+"Xi"+str(N_Xi0[k])+"H2.txt"):
                            exec_calc(command)
                        else:
                            listbox.insert(6+j*i+i+j,("donmovR" + str(N_R[k])+"Xi"+str(N_Xi0[k])+"H2.txt  not found !" ))
                        if k==len(mov_exe):
                            break
                    except:
                        k+=5
                        if k==len(R_Xi):
                            break'''


#Radiobutton for R distance 
Label(app, text = "Select R distance").grid(row=1, column=0, sticky=W)
Radiobutton(app, text = "Single value", variable = var0, value = 1, width=10,font=('bold',9), command = R_val_entry).grid(row=0, column=1,sticky=W)
Radiobutton(app, text = "List of values", variable = var0, value = 2,width=25, command = R_list_entry).grid(row=0, column=2,sticky=W)
R_val = Entry(app, textvariable=Rval, width=10)
R_val.grid(row=1, column=1, ipadx=1, ipady=4)
R_val.delete(0, END) # clear the entry field
R_list = Entry(app, textvariable=Rlist, width=25)
R_list.grid(row=1, column=2, ipadx=1, ipady=4)
R_list.delete(0, END) # clear the entry field

#Radiobutton for Xi0
Label(app, text = " ").grid(row=2, column=0, sticky=W)
Label(app, text = "Select Xi0").grid(row=4, column=0, sticky=W)
Radiobutton(app, text = "Single value", variable = var1, value = 1, width=10,font=('bold',9), command = Xi_val_entry).grid(row=3, column=1,sticky=W)
Radiobutton(app, text = "Tuple of values", variable = var1, value = 2,width=25, command = Xi_list_entry).grid(row=3, column=2,sticky=W)
Xi_val = Entry(app, textvariable=Xi0_val, width=10)
Xi_val.grid(row=4, column=1, ipadx=1, ipady=4)
Xi_val.delete(0, END) # clear the entry field
Xi_list = Entry(app, textvariable=Xi0_list, width=25)
Xi_list.grid(row=4, column=2, ipadx=1, ipady=4)
Xi_list.delete(0, END) # clear the entry field

#Forms for Z1 and Z2 values
Label(app, text = " ").grid(row=5, column=0, sticky=W) 
Label(app, text = "Enter Z1, Z2").grid(row=6, column=0, sticky=W)
Z1_val = Entry(app, textvariable=Z1, width=10)
Z1_val.grid(row=6, column=1, ipadx=1, ipady=4)
Z1_val.delete(0, END) # clear the entry field
Z2_val = Entry(app, textvariable=Z2, width=10)
Z2_val.grid(row=6, column=2, ipadx=1, ipady=4)
Z2_val.delete(0, END) # clear the entry field

#Forms for n, l, m 
Label(app, text = " ").grid(row=7, column=0, sticky=W) 
Label(app, text = "Enter n,l,m").grid(row=8, column=0, sticky=W)
n_val = Entry(app, textvariable=n, width=10)
n_val.grid(row=8, column=1, ipadx=0.1, ipady=4)
n_val.delete(0, END) # clear the entry field
l_val = Entry(app, textvariable=l, width=10)
l_val.grid(row=8, column=2, ipadx=0.1, ipady=4)
l_val.delete(0, END) # clear the entry field
m_val = Entry(app, textvariable=m, width=10)
m_val.grid(row=8, column=3, ipadx=0.1, ipady=4)
m_val.delete(0, END) # clear the entry field

#Forms for nco and nop values
Label(app, text = " ").grid(row=9, column=0, sticky=W) 
Label(app, text = "Enter nco, nop").grid(row=10, column=0, sticky=W)
nco_val = Entry(app, textvariable=nco, width=10)
nco_val.grid(row=10, column=1, ipadx=1, ipady=4)
nco_val.delete(0, END) # clear the entry field
nop_val = Entry(app, textvariable=nop, width=10)
nop_val.grid(row=10, column=2, ipadx=1, ipady=4 )
nop_val.delete(0, END) # clear the entry field

#Create a Scrollable Listbox)
Label(app, text = " ").grid(row=11, column=2, sticky=W)
listbox = Listbox(app, height=8, width=70, border=3)
listbox.grid(row=12, column=0,columnspan=3, pady=10, padx=10,sticky=W)
listbox.delete(0, END) # clear the entry field

# Creating a X Scrollbar   
Xscrollbar = Scrollbar(app,orient=HORIZONTAL)
Xscrollbar.grid(row=13, column=0,columnspan=3,sticky=E+W)#(side = RIGHT, fill = BOTH)
listbox.config(xscrollcommand = Xscrollbar.set)  
Xscrollbar.config(command = listbox.xview)

# Creating a Y Scrollbar 
Yscrollbar = Scrollbar(app)
Yscrollbar.grid(row=12, column=3,columnspan=4,ipady=40, sticky=W)#(side = RIGHT, fill = BOTH)
listbox.config(yscrollcommand = Yscrollbar.set)  
Yscrollbar.config(command = listbox.yview)


#Buttons
Label(app, text = " ").grid(row=15, column=2, sticky=W)
clear_btn = Button(app, text = "Clear Input",width=10, command = clear_fuc).grid(row=16,column=0,ipadx=10, ipady=4)
register_btn = Button(app, text = "Register",width=10, command = register_fuc).grid(row=16,column=1,ipadx=10, ipady=4)
run_btn = Button(app, text = "Run",width=10, command = run_fuc).grid(row=16,column=2,ipadx=10, ipady=4,sticky=W)
#run_btn = Button(app, text = "Run",width=10, command = run_fuc).grid(row=17,column=1,ipadx=60, ipady=4,sticky=W)

#Populate data
#populate_list()

mainloop()

