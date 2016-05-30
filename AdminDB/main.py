#!/usr/bin/env python3
# coding: utf-8

#tkinter
from tkinter import *
from tkinter.filedialog import *
import tkinter.messagebox as tm


import mysql.connector

changed = False

conn = mysql.connector.connect(host="localhost",user="root",password="1234", database="ShapeFinder")
cursor = conn.cursor()

class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.logged = False

        self.label_1 = Label(self, text="Compte")
        self.label_2 = Label(self, text="MotDePasse")

        self.entry_1 = Entry(self)
        self.entry_2 = Entry(self, show="*")

        self.label_1.grid(row=0, sticky=E)
        self.label_2.grid(row=1, sticky=E)
        self.entry_1.grid(row=0, column=1)
        self.entry_2.grid(row=1, column=1)

        self.logbtn = Button(self, text="Login", command = self._login_btn_clickked)
        self.logbtn.grid(columnspan=2)

        self.pack()

    def _login_btn_clickked(self):
        #print("Clicked")
        global changed
        username = self.entry_1.get()
        password = self.entry_2.get()

        req = "SELECT * FROM compte_admin WHERE login={} AND password={}".format("'" + username + "'", "'" + password + "'")
        #labelcon = Label(acceuil, text=str(req))
        #labelcon.pack()

        cursor.execute(req)
        result = cursor.fetchone()

        if result == None:
            self.logged = False
            changed = False
            tm.showinfo("Login Error", "Verifiez votre Compte et MDP")
        else:
            self.logged = True
            changed = True
            tm.showinfo("Login info", "Welcome " + username + "!")
            for widget in self.winfo_children():
                widget.destroy()

            self.menu_bar()

    def menu_bar(self):

        menu8 = Menu(menubar, tearoff=0)
        menu8.add_command(label="Créer")
        menu8.add_command(label="Editer")
        menu8.add_command(label="Supprimer")
        menubar.add_cascade(label="Administrateurs", menu=menu8)

        menu2 = Menu(menubar, tearoff=0)
        menu2.add_command(label="Créer")
        menu2.add_command(label="Editer")
        menu2.add_command(label="Supprimer")
        menubar.add_cascade(label="Utilisateurs", menu=menu2)

        menu3 = Menu(menubar, tearoff=0)
        menu3.add_command(label="Créer")
        menu3.add_command(label="Editer")
        menu3.add_command(label="Supprimer")
        menubar.add_cascade(label="Séances", menu=menu3)

        menu4 = Menu(menubar, tearoff=0)
        menu4.add_command(label="Créer")
        menu4.add_command(label="Editer")
        menu4.add_command(label="Supprimer")
        menubar.add_cascade(label="Images", menu=menu4)

        menu5 = Menu(menubar, tearoff=0)
        menu5.add_command(label="Créer")
        menu5.add_command(label="Editer")
        menu5.add_command(label="Supprimer")
        menubar.add_cascade(label="Questions", menu=menu5)

        menu6 = Menu(menubar, tearoff=0)
        menu6.add_command(label="Créer")
        menu6.add_command(label="Editer")
        menu6.add_command(label="Supprimer")
        menubar.add_cascade(label="Questions", menu=menu6)

def hide_me(event):
    event.widget.pack_forget()

#def refreshui(frame):
#    frame.update_idletasks()

if __name__ == "__main__":

    acceuil = Tk()
    acceuil.geometry('1280x720')
    acceuil.resizable(width=FALSE, height=FALSE)

    menubar = Menu(acceuil)

    menu1 = Menu(menubar, tearoff=0)
    menu1.add_command(label="Quitter", command=acceuil.quit)
    menubar.add_cascade(label="Fichier", menu=menu1)

    menu7 = Menu(menubar, tearoff=0)
    menu7.add_command(label="A propos")
    menubar.add_cascade(label="Aide", menu=menu7)

    acceuil.config(menu=menubar)

    label = Label(acceuil, text="Shape Finder Administration Tool")
    label.pack()

    #Photo
    originalphoto = PhotoImage(file="src/logotest.png")
    resizedphoto = originalphoto.subsample(4,4)
    canvas = Canvas(acceuil,width=140, height=120)
    canvas.create_image(0, 0, anchor=NW, image=resizedphoto)
    canvas.pack(side = TOP)

    lf = LoginFrame(acceuil)

    acceuil.update_idletasks()
    acceuil.title("Shape Finder by ShapeMasters")
    acceuil.mainloop()

    conn.close()
