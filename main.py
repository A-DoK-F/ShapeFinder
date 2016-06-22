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


conn = mysql.connector.connect(host='94.76.204.85',user="alex_",password="alex_", database="ShapeFinder")
cursor = conn.cursor()

class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.filepath = ""
        self.phototemp = object
        self.entry_forme = object
        self.forme_image = ""
        self.action = ""
        self.scrollbar = Scrollbar(acceuil)
        self.listedisplayed = Listbox(acceuil, yscrollcommand = self.scrollbar.set)
        self.scrollbar.config( command = self.listedisplayed.yview )

        self.SuperUserDBFlag = 1

        self.logged = False

        self.label_cmpt = Label(self, text="Compte")
        self.label_pwd = Label(self, text="MotDePasse")
        self.label_name = Label(self, text="Nom")
        self.label_firstname = Label(self, text="Prenom")
        self.label_email = Label(self, text="Email")
        self.label_street = Label(self, text="Rue")
        self.label_zip = Label(self, text="Code Postal")
        self.label_city = Label(self, text="Ville")
        self.label_phone1 = Label(self, text="Tel.")
        self.label_phone2 = Label(self, text="Tel.Mobile")
        self.label_title = Label(self, text="Titre")
        self.label_payment = Label(self, text="Paiement")


        self.temp_label = ""
        self.temp_entry = ""

        self.entry_cmpt = Entry(self)
        self.entry_pwd = Entry(self, show='*')
        self.entry_name = Entry(self)
        self.entry_firstname = Entry(self)
        self.entry_email = Entry(self)
        self.entry_street = Entry(self)
        self.entry_zip = Entry(self)
        self.entry_city = Entry(self)
        self.entry_phone1 = Entry(self)
        self.entry_phone2 = Entry(self)
        self.entry_title = Entry(self)
        self.entry_payment = Entry(self)

        self.label_cmpt.grid(row=0, sticky=E)
        self.label_pwd.grid(row=1, sticky=E)
        self.entry_cmpt.grid(row=0, column=1)
        self.entry_pwd.grid(row=1, column=1)

        self.logbtn = Button(self, text="Login", command = self._login_btn_clickked)
        self.logbtn.grid(columnspan=2)

        self.pack()

    def _login_btn_clickked(self):
        #print("Clicked")
        global changed
        username = self.entry_cmpt.get()
        password = self.entry_pwd.get()

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
        self.listedisplayed.pack_forget()

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

    def add_user(self, usertype):
        self.clear_ui()

        self.label_cmpt = Label(self, text="Compte")
        self.label_pwd = Label(self, text="MotDePasse")
        self.label_name = Label(self, text="Nom")
        self.label_firstname = Label(self, text="Prenom")
        self.label_email = Label(self, text="Email")
        self.label_street = Label(self, text="Rue")
        self.label_zip = Label(self, text="Code Postal")
        self.label_city = Label(self, text="Ville")

        if usertype == "Normal":
            self.label_phone1 = Label(self, text="Tel.")
            self.label_phone2 = Label(self, text="Tel.Mobile")
            self.label_title = Label(self, text="Titre")
            self.label_payment = Label(self, text="Ville")


        self.entry_cmpt = Entry(self)
        self.entry_pwd = Entry(self, show='*')
        self.entry_name = Entry(self)
        self.entry_firstname = Entry(self)
        self.entry_email = Entry(self)
        self.entry_street = Entry(self)
        self.entry_zip = Entry(self)
        self.entry_city = Entry(self)

        if usertype == "Normal":
            self.entry_phone1 = Entry(self)
            self.entry_phone2 = Entry(self)
            self.entry_title = Entry(self)
            self.entry_payment = Entry(self)

        self.label_cmpt.grid(row=0, sticky=E)
        self.label_pwd.grid(row=1, sticky=E)
        self.entry_cmpt.grid(row=0, column=1)
        self.entry_pwd.grid(row=1, column=1)
        self.label_name.grid(row=2, sticky=E)
        self.label_firstname.grid(row=3, sticky=E)
        self.entry_name.grid(row=2, column=1)
        self.entry_firstname.grid(row=3, column=1)
        self.label_email.grid(row=4, sticky=E)
        self.label_street.grid(row=5, sticky=E)
        self.entry_email.grid(row=4, column=1)
        self.entry_street.grid(row=5, column=1)
        self.label_zip.grid(row=6, sticky=E)
        self.label_city.grid(row=7, sticky=E)
        self.entry_zip.grid(row=6, column=1)
        self.entry_city.grid(row=7, column=1)

        if usertype == "Normal":
            self.label_phone1.grid(row=8,stick=E)
            self.label_phone2.grid(row=9,stick=E)
            self.label_title.grid(row=10,stick=E)
            self.label_payment.grid(row=11,stick=E)
            self.entry_phone1.grid(row=8,column=1)
            self.entry_phone2.grid(row=9,column=1)
            self.entry_title.grid(row=10,column=1)
            self.entry_payment.grid(row=11,column=1)


        validbutn = Button(self, text ='Valider',command=lambda: self.add_userdb(usertype))
        validbutn.grid(row=12, column=1)

        self.pack()

    def add_userdb(self, usertype):
        compte = self.entry_cmpt.get()
        mdp = self.entry_pwd.get()
        nom = self.entry_name.get()
        prenom = self.entry_firstname.get()
        mail = self.entry_email.get()
        rue = self.entry_street.get()
        code = self.entry_zip.get()
        ville = self.entry_city.get()

        if usertype == "Normal":
            phone_fix = self.entry_phone1.get()
            phone_mobile = self.entry_phone2.get()
            titre = self.entry_title.get()
            payer = self.entry_payment.get()

        if usertype == "Admin":
            tabledb = "compte_admin"
        else:
            tabledb = "customer"

        if compte == "":
            tm.showinfo("Erreur", "Veuillez Indiqué un Nom de Compte")
        elif mdp == "":
            tm.showinfo("Erreur", "Veuillez Indiqué un Mot de Passe")
        elif nom == "":
            tm.showinfo("Erreur", "Veuillez Indiqué un Nom de Famille")
        elif prenom == "":
            tm.showinfo("Erreur", "Veuillez Indiqué un votre Prénom")
        elif mail == "":
            tm.showinfo("Erreur", "Veuillez Indiqué une Addresse E-mail")
        elif rue == "":
            tm.showinfo("Erreur", "Veuillez Indiqué Votre Rue")
        elif code == "":
            tm.showinfo("Erreur", "Veuillez Indiqué Votre Code Postale")
        elif ville == "":
            tm.showinfo("Erreur", "Veuillez Indiqué Votre Ville")
        else:
            if usertype == "Normal":
                req = "INSERT INTO {} (name, firstname, email, street, zip, city, phone1, phone2, title, payment, login, password) VALUES ({}, {}, {}, {}, {} ,{} , {}, {}, {} ,{} , {}, {})".format(tabledb, "'" + nom + "'", "'" + prenom + "'", "'" + mail + "'", "'" + rue + "'", "'" + code + "'", "'" + ville + "'", "'" + phone_fix + "'","'" + phone_mobile + "'","'" + titre + "'","'" + payer + "'", "'" + compte + "'", "'" + mdp + "'")
            else:
                req = "INSERT INTO {} (name, firstname, email, street, zip, city, login, password) VALUES ({}, {}, {}, {}, {} ,{} , {}, {})".format(tabledb, "'" + nom + "'", "'" + prenom + "'", "'" + mail + "'", "'" + rue + "'", "'" + code + "'", "'" + ville + "'", "'" + compte + "'", "'" + mdp + "'")
            print(req)
        try:
            cursor.execute(req)
            conn.commit()
            tm.showinfo("Succès!", "L'Enregistrement en Base de Données du Compte a réussi!")
            self.clear_ui()
            self.listedisplayed.pack_forget()
        except:
            conn.rollback()
            tm.showinfo("Erreur", "L'Enregistrement en Base de Données du Compte a échoué!")
            self.clear_ui()
            self.listedisplayed.pack_forget()

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
            req = "INSERT INTO `img` (NomImage, FormeImage) VALUES ({}, {})".format("'" + imagepath.name + "'", "'" + forme + "'")


        try:
            cursor.execute(req)
            conn.commit()
        except:
            conn.rollback()
            tm.showinfo("Erreur", "L'Enregistrement en Base de Données de l'Image a échoué!")

    def get_imagedb(self, actiondb = "youpi"):

        self.action = actiondb
        self.clear_ui()
        req = "SELECT * FROM img"

        cursor.execute(req)
        result = 0
        compteur = 0
        resultatreq = list()

        while result != None:
            result = cursor.fetchone()
            if result != None:
                resultatreq.append(result)

        self.display_listdb(resultatreq)

    def get_superuserdb(self, actiondb = "youpi"):

        self.action = actiondb
        self.clear_ui()
        req = "SELECT * FROM compte_admin"

        cursor.execute(req)
        result = 0
        compteur = 0
        resultatreq = list()

        while result != None:
            result = cursor.fetchone()
            if result != None:
                resultatreq.append(result)

        self.display_listdb(resultatreq)


    def display_listdb(self, resultatreq):

        self.clear_ui()

        for i in range(0,len(resultatreq)):
            self.listedisplayed.insert(i, resultatreq[i])

        self.scrollbar.pack(side= RIGHT,fill=Y)
        self.listedisplayed.pack(side=TOP, fill = BOTH)

        if self.action == "EditerSuperUser":
            selectbtn = Button(self, text ='Selectionner', command=lambda: self.rec_modify_superuserdb(self.listedisplayed))
        else:
            selectbtn = Button(self, text ='Selectionner', command=lambda: self.rec_modify_imagedb(self.listedisplayed))
        selectbtn.pack(side=TOP)

    def rec_modify_superuserdb(self, listSelection):
        self.clear_ui()

        listTemp = listSelection.get(listSelection.curselection())

        if self.action == "EditerSuperUser":

            self.label_cmpt = Label(self, text="Compte")
            self.label_pwd = Label(self, text="MotDePasse")
            self.label_name = Label(self, text="Nom")
            self.label_firstname = Label(self, text="Prenom")
            self.label_email = Label(self, text="Email")
            self.label_street = Label(self, text="Rue")
            self.label_zip = Label(self, text="Code Postal")
            self.label_city = Label(self, text="Ville")

            modify_cmpt = Button(self, text ='Modifier', command=lambda: self.modify_field_superuserdb("login", listTemp))
            modify_pwd = Button(self, text ='Modifier', command=lambda: self.modify_field_superuserdb("password", listTemp))
            modify_name = Button(self, text ='Modifier', command=lambda: self.modify_field_superuserdb("name", listTemp))
            modify_firstname = Button(self, text ='Modifier', command=lambda: self.modify_field_superuserdb("firstname", listTemp))
            modify_email = Button(self, text ='Modifier', command=lambda: self.modify_field_superuserdb("email", listTemp))
            modify_street = Button(self, text ='Modifier', command=lambda: self.modify_field_superuserdb("street", listTemp))
            modify_zip = Button(self, text ='Modifier', command=lambda: self.modify_field_superuserdb("zip", listTemp))
            modify_city = Button(self, text ='Modifier', command=lambda: self.modify_field_superuserdb("city", listTemp))

            self.label_cmpt.grid(row=0, sticky=E)
            self.label_pwd.grid(row=1, sticky=E)
            modify_cmpt.grid(row=0, column=1)
            modify_pwd.grid(row=1, column=1)
            self.label_name.grid(row=2, sticky=E)
            self.label_firstname.grid(row=3, sticky=E)
            modify_name.grid(row=2, column=1)
            modify_firstname.grid(row=3, column=1)
            self.label_email.grid(row=4, sticky=E)
            self.label_street.grid(row=5, sticky=E)
            modify_email.grid(row=4, column=1)
            modify_street.grid(row=5, column=1)
            self.label_zip.grid(row=6, sticky=E)
            self.label_city.grid(row=7, sticky=E)
            modify_zip.grid(row=6, column=1)
            modify_city.grid(row=7, column=1)


            cancelbtn = Button(self, text ='Terminer', command=self.clear_ui)
            cancelbtn.grid(row=8, sticky=N)

        else:
            pass

        self.pack()

    def modify_field_superuserdb(self, champ, listTemp):
        self.clear_ui()

        self.temp_label = Label(self, text=champ)

        if champ == "Password":
            self.temp_entry = Entry(self, show="*")
        else:
            self.temp_entry = Entry(self)

        self.temp_label.grid(row=0, sticky=E)
        self.temp_entry.grid(row=0, column=1)

        selectbtn = Button(self, text ='Valider', command=lambda: self.modify_info_superuserdb(champ, listTemp))
        cancelbtn = Button(self, text ='Annuler', command=self.clear_ui)
        cancelbtn.grid(row=2, sticky=E)
        selectbtn.grid(row=2, column=1)

        self.pack()



    def modify_info_superuserdb(self, champ, listSelection):

        variable = self.temp_entry.get()
        print(champ)
        print(variable)
        if variable == "":
            tm.showinfo("Erreur", "Veuillez Indiqué la Nouvelle Valeur")
        else:
            req = "UPDATE `compte_admin` SET {}={} WHERE idcompte_admin={}".format( champ, "'" + variable + "'","'" + str(listSelection[0]) + "'")
        try:
            cursor.execute(req)
            conn.commit()
            tm.showinfo("Succès!", "La mise a jour en Base de Données a réussi!")
            self.clear_ui()
            self.listedisplayed.pack_forget()
        except:
            conn.rollback()
            tm.showinfo("Erreur", "La mise a jour en Base de Données a échoué!")
            self.clear_ui()
            self.listedisplayed.pack_forget()


    def rec_modify_imagedb(self, listSelection):
        self.clear_ui()

        listTemp = listSelection.get(listSelection.curselection())
        if self.action == "EditerImage":
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
        menu8.add_command(label="Créer", command=lambda: self.add_user("Admin"))
        menu8.add_command(label="Editer", command=lambda: self.get_superuserdb("EditerSuperUser"))
        menu8.add_command(label="Supprimer")
        menubar.add_cascade(label="Administrateurs", menu=menu8)

        menu2 = Menu(menubar, tearoff=0)
        menu2.add_command(label="Créer", command=lambda: self.add_user("Normal"))
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
    originalphoto = PhotoImage(file="img/logo.png")
    resizedphoto = originalphoto.subsample(4,4)
    canvas = Canvas(acceuil,width=140, height=120)
    canvas.create_image(0, 0, anchor=NW, image=resizedphoto)
    canvas.pack(side = BOTTOM)

    lf = LoginFrame(acceuil)

    acceuil.update_idletasks()
    acceuil.title("Shape Finder by ShapeMasters")
    acceuil.mainloop()

    conn.close()
