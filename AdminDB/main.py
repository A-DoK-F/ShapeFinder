#!/usr/bin/env python3
# coding: utf-8

#tkinter
from tkinter import *
from tkinter.filedialog import *
import tkinter.messagebox as tm

import shutil
from types import *
from pathlib import Path

import mysql.connector

#changed = False
srcfolder = "/img"
softwarefolder = str(os.getcwd())


conn = mysql.connector.connect(host="localhost",user="root",password="1234", database="ShapeFinder")
cursor = conn.cursor()

class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.filepath = ""
        self.phototemp = object
        self.entry_forme = object
        self.forme_image = ""
        self.listedisplayed = list()

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
            self.clear_ui()
            self.menu_bar()

    def clear_ui(self):
        for widget in self.winfo_children():
            widget.destroy()

    def add_image(self):
        self.clear_ui()
        #175x175
        self.filepath = askopenfilename(title="Ouvrir une image: Dimension 175x175",filetypes=[('png files','.png')])
        self.phototemp = PhotoImage(file=self.filepath)

        canvaPreview = Canvas(self, width=175, height=175)
        canvaPreview.create_image(0, 0, anchor=NW, image=self.phototemp)
        canvaPreview.pack(side=BOTTOM, padx=5, pady=5)

        Button(self, text ='Annuler', command=self.clear_ui).pack(side=LEFT, padx=5, pady=5)
        Button(self, text ='Valider', command=self.copy_image).pack(side=RIGHT, padx=5, pady=5)

        self.entry_forme = Entry(self, text="Forme", width=30)
        self.entry_forme.pack(side = BOTTOM)


    def copy_image(self):
        if self.phototemp.width() < 1:
            tm.showinfo("Erreur", "Ajout d'image Annulé")
        elif self.phototemp.width() != 175:
            tm.showinfo("Erreur", "Veuillez Redimensionner l'image, largeur inadéquat! (175x175)")
            self.add_image()
        elif self.phototemp.height() != 175:
            tm.showinfo("Erreur", "Veuillez Redimensionner l'image, hauteur inadéquat! (175x175)")
            self.add_image()
        else:
            try:
                shutil.copy2(self.filepath, softwarefolder + srcfolder)
                self.insert_imagedb()
            except EnvironmentError:
                tm.showinfo("Erreur", "La Copie de l'Image a échoué!")
                self.clear_ui()
            else:
                tm.showinfo("Succès", "La Copie de l'Image a Réussi!")
                self.clear_ui()

    def insert_imagedb(self):
        forme = self.entry_forme.get()
        if forme == "":
            tm.showinfo("Erreur", "Veuillez Indiqué une Forme pour Votre Image")
        else:
            imagepath = Path(str(self.filepath))
            req = "INSERT INTO `images` (NomImage, FormeImage) VALUES ({}, {})".format("'" + imagepath.name + "'", "'" + forme + "'")


        try:
            cursor.execute(req)
            conn.commit()
        except:
            conn.rollback()
            tm.showinfo("Erreur", "L'Enregistrement en Base de Données de l'Image a échoué!")

    def get_imagedb(self, action):

        self.clear_ui()
        req = "SELECT * FROM images"

        cursor.execute(req)
        result = 0
        compteur = 0
        resultatreq = list()

        while result != None:
            result = cursor.fetchone()
            if result != None:
                resultatreq.append(result)

        self.display_listdb(resultatreq, action)

    def display_listdb(self, resultatreq, action):

        self.clear_ui()

        self.listedisplayed = Listbox(acceuil)


        for i in range(0,len(resultatreq)):
            self.listedisplayed.insert(i, resultatreq[i])

        self.listedisplayed.pack(side=TOP)

        selectbtn = Button(self, text ='Selectionner', command=lambda: self.rec_modify_imagedb(self.listedisplayed, action))
        selectbtn.pack(side=TOP)

    def rec_modify_imagedb(self, listSelection, action):
        self.clear_ui()

        listTemp = listSelection.get(listSelection.curselection())
        if action == "EditerImage":
            self.forme_image = Entry(self, text=listTemp[2], width=30)
            self.forme_image.pack(side = TOP)
            selectbtn = Button(self, text ='Valider', command=lambda: self.modify_shape_imagedb(listTemp))
        else:
            selectbtn = Button(self, text ='Valider', command=lambda: self.sup_imagedb(listTemp))

        cancelbtn = Button(self, text ='Annuler', command=self.clear_ui)
        selectbtn.pack(side=TOP)
        cancelbtn.pack(side=TOP)

    def modify_shape_imagedb(self, listSelection):

        forme = self.forme_image.get()
        if forme == "":
            tm.showinfo("Erreur", "Veuillez Indiqué une Forme pour Votre Image")
        else:
            req = "UPDATE `images` SET FormeImage={} WHERE Id={}".format("'" + forme + "'", "'" + str(listSelection[0]) + "'")
        try:
            cursor.execute(req)
            conn.commit()
            tm.showinfo("Succès!", "L'Enregistrement en Base de Données de l'Image a réussi!")
            self.clear_ui()
            self.listedisplayed.pack_forget()
        except:
            conn.rollback()
            tm.showinfo("Erreur", "L'Enregistrement en Base de Données de l'Image a échoué!")
            self.clear_ui()
            self.listedisplayed.pack_forget()

    def sup_imagedb(self, listSelection):

        req = "DELETE FROM `images` WHERE Id={}".format("'" + str(listSelection[0]) + "'", "'" + str(listSelection[1]) + "'", "'" + str(listSelection[2]) + "'")
        try:
            cursor.execute(req)
            conn.commit()
            os.remove(softwarefolder + srcfolder + "/" + listSelection[1])
            tm.showinfo("Succès!", "La Suppression l'Image a réussi!")
            self.clear_ui()
            self.listedisplayed.pack_forget()
        except:
            conn.rollback()
            tm.showinfo("Erreur", "La Suppression l'Image a échoué!")
            self.clear_ui()
            self.listedisplayed.pack_forget()

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
        menu4.add_command(label="Ajouter", command=self.add_image)
        menu4.add_command(label="Editer", command=lambda: self.get_imagedb("EditerImage"))
        menu4.add_command(label="Supprimer", command=lambda: self.get_imagedb("SupprimerImage"))
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
    originalphoto = PhotoImage(file="img/logotest.png")
    resizedphoto = originalphoto.subsample(4,4)
    canvas = Canvas(acceuil,width=140, height=120)
    canvas.create_image(0, 0, anchor=NW, image=resizedphoto)
    canvas.pack(side = BOTTOM)

    lf = LoginFrame(acceuil)

    acceuil.update_idletasks()
    acceuil.title("Shape Finder by ShapeMasters")
    acceuil.mainloop()

    conn.close()
