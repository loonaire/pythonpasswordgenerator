from tkinter import Tk,Button,Label,PanedWindow,Spinbox,messagebox, Checkbutton,BooleanVar
import GenerateurMotDePasse


class Gui:
    
    def __init__(self):

        self.genereMDP = GenerateurMotDePasse.GenerateurMotDePasse(6,24)
        #configuration de la fenetre:
        self.gui = Tk()
        self.gui.title("Générateur de mot de passe")
        #self.gui.geometry('800x400')
        self.gui.resizable(False,False)
        # les différents éléments de la fenetre
        self.textAffichageMDP = Label(self.gui, text= "Mot de passe généré: ")
        self.affichageMDP = Label(self.gui,text=self.genereMDP.motDePasse)
        self.boutonGenereMDP = Button(self.gui,text="Générer un mot de passe",command=self.OnButtonClick, borderwidth = 1)

        self.textSaisieLongueurMin = Label(self.gui,text="Longueur minimale du mot de passe:")
        self.saisieLongueurMin = Spinbox(self.gui, from_ = 0, to = 50) #50 évite que ca soit super long
        self.textSaisieLongueurMax = Label(self.gui,text="Longueur maximale du mot de passe:")
        self.saisieLongueurMax = Spinbox(self.gui, from_ = 1, to = 50)

        self.varCheckMinuscule = BooleanVar()
        self.varCheckMaj = BooleanVar()
        self.varCheckNombre = BooleanVar()
        self.varCheckCaracSpec = BooleanVar()

        self.checkMinuscule = Checkbutton(self.gui, text = " Lettres minuscules", variable = self.varCheckMinuscule , onvalue = True , offvalue = False)
        self.checkMaj = Checkbutton(self.gui, text = " Lettres majuscules", variable = self.varCheckMaj , onvalue = True , offvalue = False)
        self.checkNombre = Checkbutton(self.gui, text = " Nombres", variable = self.varCheckNombre , onvalue = True , offvalue = False)
        self.checkCaracSpec = Checkbutton(self.gui, text = " Caractères spéciaux", variable = self.varCheckCaracSpec , onvalue = True , offvalue = False)

        self.copyButton = Button(self.gui, text= "Copier le mot de passe", command=self.passwordCopy, borderwidth = 1)
        
        # la mise en forme*
        self.textSaisieLongueurMin.grid(row = 0, column = 0)
        self.saisieLongueurMin.grid(row = 0, column = 1)

        self.textSaisieLongueurMax.grid(row = 1, column = 0)
        self.saisieLongueurMax.grid(row = 1, column = 1)

        self.checkMinuscule.grid(row = 2,column = 0, ipady = 0, sticky = "w")
        self.checkMaj.grid(row = 2, column = 1, sticky = "w")

        self.checkNombre.grid(row = 3, column = 0, sticky = "w")
        self.checkCaracSpec.grid(row = 3, column = 1, sticky = "w")

        self.boutonGenereMDP.grid(row = 4, column = 1)

        self.textAffichageMDP.grid(row= 6, column = 0)
        self.affichageMDP.grid(row = 6, column = 1)

        self.copyButton.grid(row = 7, column = 1)


    def exec(self):
        self.gui.mainloop()

    def passwordCopy(self):
		#Copie textecopie dans le press-papier
        self.gui.clipboard_clear() #on vide le presse papier
        self.gui.clipboard_append(self.genereMDP.motDePasse) # ajoute le mot de passe à la fin du presse papier (donc au final il n'y a que le mot de passe dans le presse papier)

    def OnButtonClick(self):
        if int(self.saisieLongueurMax.get()) > int(self.saisieLongueurMin.get()) :

            if(self.varCheckMinuscule.get() == True):
                self.genereMDP.lettreMin = True
            else:
                self.genereMDP.lettreMin = False

            if(self.varCheckMaj.get() == True):
                self.genereMDP.lettreMaj = True
            else:
                self.genereMDP.lettreMaj = False

            if(self.varCheckNombre.get() == True):
                self.genereMDP.nombre = True
            else:
                self.genereMDP.nombre = False

            if(self.varCheckCaracSpec.get() == True):
                self.genereMDP.caractereSpeciaux = True
            else:
                self.genereMDP.caractereSpeciaux = False

            self.genereMDP.longueurMin = int(self.saisieLongueurMin.get())
            self.genereMDP.longueurMax = int(self.saisieLongueurMax.get())

            self.genereMDP.genereMotDePasse()
            self.affichageMDP.configure(text=self.genereMDP.motDePasse)
        else:
            messagebox.showerror("Erreur", "Valeurs de longueurs incorrectes!")
