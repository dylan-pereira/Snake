from tkinter import *
import os
import time
#----------------FONCTIONS
def validation():
	
	Nomjoueur1=Motdepasse.get()
	fichier = open("../Gestion_Highscore/nomhighscore.txt", "w")
	fichier.write(str(Nomjoueur1))
	fichier.close()
	time.sleep(2)
	FenetreNomJoueur.quit()
	os.chdir("F:/Chethelan/Snake_PEREIRA/")
	os.startfile("Snake_PEREIRA.py")
	


def Lettre(lettre):
	global longeurmot
	alphabet=["0","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","É","retour","Ù","entrer","È","À",";",":","-","?"," "]
	
	if alphabet[lettre] == "retour":
		longeurmot-=1
		Entree.delete(longeurmot)
		
	elif alphabet[lettre] == "entrer":
		validation()
	else:
		longeurmot+=1
		lettreconverti = str(alphabet[lettre])
		Entree.insert("end",lettreconverti)

def Clavier(event):
	global Xcurseur,Ycurseur,precedentetouchesurvolé
	touche = event.keysym
	if touche == "Right" or touche == "Left" or touche == "Up" or touche == "Down":
		if touche == 'Right' :
			Xcurseur+=65
			if Xcurseur>825:
				Xcurseur-=780
		if touche == 'Left' :
			Xcurseur-=65
			if Xcurseur<50:
				Xcurseur+=780
		if touche == 'Up' :
			Ycurseur-=60
			Xcurseur-=20
			if Ycurseur <40:
				Ycurseur=220
				Xcurseur+=15
			if Xcurseur == 45:
				Xcurseur=110
				Ycurseur= 220
		if touche == 'Down' :
			Ycurseur+=60
			Xcurseur+=20
			if Ycurseur >220:
				Ycurseur=40
				Xcurseur-=15
			if Xcurseur == 830:
				Xcurseur=765
				Ycurseur= 40

		frameclavier.coords(curseur,Xcurseur,Ycurseur)

		frameclavier.itemconfigure(frameclavier.find_overlapping(Xcurseur-10,Ycurseur-10,Xcurseur+10,Ycurseur+10)[0], image=listenegatif[frameclavier.find_overlapping(Xcurseur-10,Ycurseur-10,Xcurseur+10,Ycurseur+10)[0]])
		if precedentetouchesurvolé != frameclavier.find_overlapping(Xcurseur-10,Ycurseur-10,Xcurseur+10,Ycurseur+10)[0]:
			frameclavier.itemconfigure(precedentetouchesurvolé, image=listenormal[precedentetouchesurvolé])
			precedentetouchesurvolé=frameclavier.find_overlapping(Xcurseur-10,Ycurseur-10,Xcurseur+10,Ycurseur+10)[0]

	if touche=="space" or touche=="Return":#return correspond a entrer 
		
		Lettre(frameclavier.find_overlapping(Xcurseur-10,Ycurseur-10,Xcurseur+10,Ycurseur+10)[0])
#----------------GESTION AFFICHAGE
#Fenetre
FenetreNomJoueur = Tk()# on crée une instance d'objet Tk (cette objet s'appel donc fenetrenomjoueur)

FenetreNomJoueur.attributes("-fullscreen", 1)
FenetreNomJoueur.config(bg="grey30")
#FenetreNomJoueur.attributes("-transparentcolor", "dodger blue")

#Fond
frameclavier=Canvas(FenetreNomJoueur,bg="grey30",width=850,height=235,highlightthickness=0)
frameclavier.place(relx=0.5, rely=0.75, anchor=CENTER)
frameclavier.pack_propagate(False)

Motdepasse= StringVar()

Entree = Entry(FenetreNomJoueur, textvariable= Motdepasse, bg ='white',font="Courier 45 bold",)

Entree.place(relx=0.5, rely=0.4, anchor=CENTER)
#--Importation des images negatives
#Alphabet
imageAnegatif = PhotoImage(file="Images/Touches_Negatif/A.png")
imageBnegatif = PhotoImage(file="Images/Touches_Negatif/B.png")
imageCnegatif = PhotoImage(file="Images/Touches_Negatif/C.png")
imageDnegatif = PhotoImage(file="Images/Touches_Negatif/D.png")
imageEnegatif = PhotoImage(file="Images/Touches_Negatif/E.png")
imageFnegatif = PhotoImage(file="Images/Touches_Negatif/F.png")
imageGnegatif = PhotoImage(file="Images/Touches_Negatif/G.png")
imageHnegatif = PhotoImage(file="Images/Touches_Negatif/H.png")
imageInegatif = PhotoImage(file="Images/Touches_Negatif/I.png")
imageJnegatif = PhotoImage(file="Images/Touches_Negatif/J.png")
imageKnegatif = PhotoImage(file="Images/Touches_Negatif/K.png")
imageLnegatif = PhotoImage(file="Images/Touches_Negatif/L.png")
imageMnegatif = PhotoImage(file="Images/Touches_Negatif/M.png")
imageNnegatif = PhotoImage(file="Images/Touches_Negatif/N.png")
imageOnegatif = PhotoImage(file="Images/Touches_Negatif/O.png")
imagePnegatif = PhotoImage(file="Images/Touches_Negatif/P.png")
imageQnegatif = PhotoImage(file="Images/Touches_Negatif/Q.png")
imageRnegatif = PhotoImage(file="Images/Touches_Negatif/R.png")
imageSnegatif = PhotoImage(file="Images/Touches_Negatif/S.png")
imageTnegatif = PhotoImage(file="Images/Touches_Negatif/T.png")
imageUnegatif = PhotoImage(file="Images/Touches_Negatif/U.png")
imageVnegatif = PhotoImage(file="Images/Touches_Negatif/V.png")
imageWnegatif = PhotoImage(file="Images/Touches_Negatif/W.png")
imageXnegatif = PhotoImage(file="Images/Touches_Negatif/X.png")
imageYnegatif = PhotoImage(file="Images/Touches_Negatif/Y.png")
imageZnegatif = PhotoImage(file="Images/Touches_Negatif/Z.png")
#Caractéres spéciaux
imageénegatif = PhotoImage(file="Images/Touches_Negatif/é.png")
imageretournegatif = PhotoImage(file="Images/Touches_Negatif/retour.png")
imageùnegatif = PhotoImage(file="Images/Touches_Negatif/ù.png")
imageentrernegatif = PhotoImage(file="Images/Touches_Negatif/entrer.png")
imageènegatif = PhotoImage(file="Images/Touches_Negatif/è.png")
imageànegatif = PhotoImage(file="Images/Touches_Negatif/à.png")
imagepointvirgulenegatif = PhotoImage(file="Images/Touches_Negatif/pointvirgule.png")
imagedeuxpointsnegatif = PhotoImage(file="Images/Touches_Negatif/deuxpoints.png")
imagetiretnegatif = PhotoImage(file="Images/Touches_Negatif/tiret.png")
imagepointinterrogationnegatif = PhotoImage(file="Images/Touches_Negatif/pointinterrogation.png")
imageespacenegatif = PhotoImage(file="Images/Touches_Negatif/espace.png")
#Liste
listenegatif=[0,imageAnegatif,imageBnegatif,imageCnegatif,imageDnegatif,imageEnegatif,imageFnegatif,imageGnegatif,imageHnegatif,imageInegatif,imageJnegatif,imageKnegatif,imageLnegatif,imageMnegatif,imageNnegatif,imageOnegatif,imagePnegatif,imageQnegatif,imageRnegatif,imageSnegatif,imageTnegatif,imageUnegatif,imageVnegatif,imageWnegatif,imageXnegatif,imageYnegatif,imageZnegatif,imageénegatif,imageretournegatif,imageùnegatif,imageentrernegatif,imageènegatif,imageànegatif,imagepointvirgulenegatif,imagedeuxpointsnegatif,imagetiretnegatif,imagepointinterrogationnegatif,imageespacenegatif,]

#--Importation des images normales
#Alphabet
imageA = PhotoImage(file="Images/Touches/A.png")
imageB=PhotoImage(file="Images/touches/B.png")
imageC=PhotoImage(file="Images/touches/C.png")
imageD=PhotoImage(file="Images/touches/D.png")
imageE=PhotoImage(file="Images/touches/E.png")
imageF=PhotoImage(file="Images/touches/F.png")
imageG=PhotoImage(file="Images/touches/G.png")
imageH=PhotoImage(file="Images/touches/H.png")
imageI=PhotoImage(file="Images/touches/I.png")
imageJ=PhotoImage(file="Images/touches/J.png")
imageK=PhotoImage(file="Images/touches/K.png")
imageL=PhotoImage(file="Images/touches/L.png")
imageM=PhotoImage(file="Images/touches/M.png")
imageN=PhotoImage(file="Images/touches/N.png")
imageO=PhotoImage(file="Images/touches/O.png")
imageP=PhotoImage(file="Images/touches/P.png")
imageQ=PhotoImage(file="Images/touches/Q.png")
imageR=PhotoImage(file="Images/touches/R.png")
imageS=PhotoImage(file="Images/touches/S.png")
imageT=PhotoImage(file="Images/touches/T.png")
imageU=PhotoImage(file="Images/touches/U.png")
imageV=PhotoImage(file="Images/touches/V.png")
imageW=PhotoImage(file="Images/touches/W.png")
imageX=PhotoImage(file="Images/touches/X.png")
imageY=PhotoImage(file="Images/touches/Y.png")
imageZ=PhotoImage(file="Images/touches/Z.png")
#Caractéres spéciaux
imageé=PhotoImage(file="Images/touches/é.png")
imageretour=PhotoImage(file="Images/touches/retour.png")
imageù=PhotoImage(file="Images/touches/ù.png")
imageentrer=PhotoImage(file="Images/touches/entrer.png")
imageè=PhotoImage(file="Images/touches/è.png")
imageà=PhotoImage(file="Images/touches/à.png")
imagepointvirgule=PhotoImage(file="Images/touches/pointvirgule.png")
imagedeuxpoints=PhotoImage(file="Images/touches/deuxpoints.png")
imagetiret=PhotoImage(file="Images/touches/tiret.png")
imagepointinterrogation=PhotoImage(file="Images/touches/pointinterrogation.png")
imageespace=PhotoImage(file="Images/touches/espace.png")
#Liste
listenormal=[0,imageA,imageB,imageC,imageD,imageE,imageF,imageG,imageH,imageI,imageJ,imageK,imageL,imageM,imageN,imageO,imageP,imageQ,imageR,imageS,imageT,imageU,imageV,imageW,imageX,imageY,imageZ,imageé,imageretour,imageù,imageentrer,imageè,imageà,imagepointvirgule,imagedeuxpoints,imagetiret,imagepointinterrogation,imageespace,]

#Affichage des images importees
#Alphabetique car on respect ainsi les id afin que le 1 corresponde au A etc..
frameclavier.create_image(0, 0, image=imageAnegatif, anchor=NW)
frameclavier.create_image(60+65*4,120, image=imageB, anchor=NW)
frameclavier.create_image(60+65*2,120, image=imageC, anchor=NW)
frameclavier.create_image(20+65*2,60, image=imageD, anchor=NW)
frameclavier.create_image(65*2, 0, image=imageE, anchor=NW)
frameclavier.create_image(20+65*3,60, image=imageF, anchor=NW)
frameclavier.create_image(20+65*4,60, image=imageG, anchor=NW)
frameclavier.create_image(20+65*5,60, image=imageH, anchor=NW)
frameclavier.create_image(65*7, 0, image=imageI, anchor=NW)
frameclavier.create_image(20+65*6,60, image=imageJ, anchor=NW)
frameclavier.create_image(20+65*7,60, image=imageK, anchor=NW)
frameclavier.create_image(20+65*8,60, image=imageL, anchor=NW)
frameclavier.create_image(20+65*9,60, image=imageM, anchor=NW)
frameclavier.create_image(60+65*5,120, image=imageN, anchor=NW)
frameclavier.create_image(65*8, 0, image=imageO, anchor=NW)
frameclavier.create_image(65*9, 0, image=imageP, anchor=NW)
frameclavier.create_image(20,60, image=imageQ, anchor=NW)
frameclavier.create_image(65*3, 0, image=imageR, anchor=NW)
frameclavier.create_image(20+65,60, image=imageS, anchor=NW)
frameclavier.create_image(65*4, 0, image=imageT, anchor=NW)
frameclavier.create_image(65*6, 0, image=imageU, anchor=NW)
frameclavier.create_image(60+65*3,120, image=imageV, anchor=NW)
frameclavier.create_image(60,120, image=imageW, anchor=NW)
frameclavier.create_image(60+65*1,120, image=imageX, anchor=NW)
frameclavier.create_image(65*5, 0, image=imageY, anchor=NW)
frameclavier.create_image(65, 0, image=imageZ, anchor=NW)
#Caractéres spéciaux
frameclavier.create_image(65*10, 0, image=imageé, anchor=NW)
frameclavier.create_image(65*11, 0, image=imageretour, anchor=NW)
frameclavier.create_image(20+65*10, 60, image=imageù, anchor=NW)
frameclavier.create_image(20+65*11, 60, image=imageentrer, anchor=NW)
frameclavier.create_image(60+65*6, 120, image=imageè, anchor=NW)
frameclavier.create_image(60+65*7, 120, image=imageà, anchor=NW)
frameclavier.create_image(60+65*8, 120, image=imagepointvirgule, anchor=NW)
frameclavier.create_image(60+65*9, 120, image=imagedeuxpoints, anchor=NW)
frameclavier.create_image(60+65*10, 120, image=imagetiret, anchor=NW)
frameclavier.create_image(60+65*11, 120, image=imagepointinterrogation, anchor=NW)
frameclavier.create_image(100,180, image=imageespace, anchor=NW)


#----------------GESTION VARIABLES
Xcurseur=50
Ycurseur=40
longeurmot=0
precedentetouchesurvolé=1

#----------------GESTION CURSEUR
imagecurseur=PhotoImage(file="Images/curseur.png")
curseur=frameclavier.create_image(Xcurseur,Ycurseur,image=imagecurseur)
frameclavier.tag_raise(curseur)#le met au dessus





frameclavier.focus_set()
frameclavier.bind('<Key>',Clavier)
FenetreNomJoueur.mainloop()