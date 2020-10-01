from tkinter import *
from random import randrange
import os
import time

#----------------FONCTIONS
def Clavier(event):
    global direction
    touche = event.keysym
    #si on va pas vers la direction oposée ni deja dans cette direction alors...
    # déplacement vers le haut 
    if touche == 'Up' and direction!=8  and direction!=2:
        direction=8
    # déplacement vers le bas
    if touche == 'Down' and direction!=2  and direction!=8:
        direction=2
    # déplacement vers la DROITE  								Faut rajouter que il puisse pas spam droite gauche
    if touche == 'Right' and direction!=6  and direction!=4:
        direction=6
    # déplacement vers la gauche
    if touche == 'Left' and direction!=4  and direction!=6:
        direction=4
    if touche == 'Return' and perdu==True:
    	rejouer()
    if touche =="space":
    	os.chdir("F:/Chethelan")
    	os.startfile("accueil.py")
    	Mafenetre.destroy()

def rejouer():
	global teteX, teteY, perdu, direction, score,serpent,PommeX,PommeY,highscore
	if perdu==True:	
		score=0
		framedroite.delete("tagscore")
		framedroite.create_text(230,350,font="Courier 20 bold",text=score,tag="tagscore")
		framedroite.delete("taghighscore")
		framedroite.create_text(230,245,font="Courier 20 bold",text=highscore,tag="taghighscore")

		for i in range (len(Canevas.find_all())):
					Canevas.delete(i+5)

		direction =0
		teteX = 340
		teteY = 340
		Canevas.coords(Tete,teteX,teteY)
		serpent= [Corps1,]
		Canevas.coords(Corps1,teteX-40,teteY)

		PommeX= teteX + 10*LargeurSnake
		PommeY = teteY
		Canevas.coords(Pomme,PommeX,PommeY)

		Canevas.delete("tagperdu")
		perdu =False
		animation()

def animation():
	global teteX, teteY, direction,perdu, PommeX, PommeY,score,serpent,highscore,kX,kY
	longeurserpent=score

	#Collision avec la pomme
	if 2 in Canevas.find_overlapping(PommeX-1,PommeY+1,PommeX-1,PommeY+1): #si tête (id=2) est sur la pomme alors :

		corps = Canevas.create_image(PommeX,PommeY,image=corpsserpent)
		serpent.append(corps)


		def coordspommealeatoire():
			global kX, kY
			kX= randrange(1,36)
			if kX%2 ==0 :
				kX=kX-1
			kY= randrange(1,36)
			if kY%2 ==0 :
				kY=kY-1
		coordspommealeatoire()
		while len(Canevas.find_overlapping(kX*LargeurSnake-1,kY*LargeurSnake+1,kX*LargeurSnake-1,kY*LargeurSnake+1))>1:
			print("Les coords était mauvais !")
			coordspommealeatoire()
		print("il y a :",len(Canevas.find_overlapping(kX*LargeurSnake-1,kY*LargeurSnake+1,kX*LargeurSnake-1,kY*LargeurSnake+1)))
		

		PommeX = kX*LargeurSnake
		PommeY = kY*LargeurSnake
		Canevas.coords(Pomme,PommeX, PommeY)
		score = score+1

		framedroite.itemconfigure("tagscore", text=score)
		if score>highscore:
			highscore=score
			framedroite.itemconfigure("taghighscore", text=highscore)
			fichier = open("Gestion_Highscore/highscore.txt", "w")
			fichier.write(str(score))
			fichier.close()
	#Deplacement serpent
	if direction == 8:#HAUT
		if teteY-40<LargeurSnake:
			fonctionperdu()
		else:
			Canevas.coords(serpent[longeurserpent],teteX, teteY)#on tp le dernier corps a la place de la tête
			teteY=teteY-(LargeurSnake*2)
			Canevas.coords(Tete,teteX, teteY)#on met la tete au nouveau coords
			serpent.append(serpent[0])# on agrandi le serpent du plus ancien (ce qui a pour effet de le possitionner a la fin de du serpent(liste))
			serpent.remove(serpent[0])#puis on le supprime pour qu'il soit uniquement a la fin

	if direction ==6:#DROITE
		if teteX+40>Largeur - LargeurSnake :
			fonctionperdu()
		else:
			Canevas.coords(serpent[longeurserpent],teteX, teteY)
			teteX=teteX+(LargeurSnake*2)
			Canevas.coords(Tete,teteX, teteY)
			serpent.append(serpent[0])
			serpent.remove(serpent[0])

	if direction == 2:#BAS
		if teteY+40>Largeur-LargeurSnake:
			fonctionperdu()
		else:
			Canevas.coords(serpent[longeurserpent],teteX,teteY)
			teteY=teteY+(LargeurSnake*2)
			Canevas.coords(Tete,teteX, teteY)
			serpent.append(serpent[0])
			serpent.remove(serpent[0])

	if direction == 4:#GAUCHE
		if teteX-40 <= LargeurSnake-1:
			fonctionperdu()
		else:
			Canevas.coords(serpent[longeurserpent],teteX, teteY)
			teteX=teteX-(LargeurSnake*2)
			Canevas.coords(Tete,teteX, teteY)
			serpent.append(serpent[0])
			serpent.remove(serpent[0])

	labcoordX.config(text=teteX)
	labcoordY.config(text=teteY)	



	#print(len(Canevas.find_all()))
	#print("La tête est en colision avec :",Canevas.find_overlapping(teteX-1,teteY+1,teteX-1,teteY+1))

	#Tout les élément en collision avec la tête son répertorés dans cette liste:
	collisionTete =Canevas.find_overlapping(teteX-1,teteY+1,teteX-1,teteY+1)
	#On additionne tout les éléments de cette liste , et si la somme est superieur a 6 alors c'est perdu car le fond vaut 1, la tête vaut 2 et la pomme 3, donc si c'est plus c'est que il ce touche lui même.
	if sum(collisionTete)>6 :
		fonctionperdu()

	if perdu==False:
		Mafenetre.after(200-score*2, animation)

def fonctionperdu():
	global perdu
	print("C'est perdu !")
	perdu =True
	Canevas.create_text(Largeur/2,Hauteur/2,fill="red",font="Courier 70 bold",text="PERDU",tag="tagperdu")
	Canevas.update
	if score == highscore:
		os.chdir("F:/Chethelan/Snake_PEREIRA/Snake_Clavier/")
		os.startfile("Nom_Highscore.py")
		time.sleep(2)
		Mafenetre.destroy()
	#if score ==highscore:
		#subprocess.run("pyton","Snake_PEREIRA.py")
		

#----------------AFFICHAGE
#FENETRE
Mafenetre = Tk()# on crée une instance d'objet Tk (cette objet s'appel donc Ma fenetre)
Hauteur = Largeur = 0.5*1440 # Pour avoir un carré (hauteur et largeur égales)
Mafenetre.attributes("-fullscreen", 1)
Mafenetre.config(bg="red")

framefenetre=Canvas(Mafenetre,bg="purple")#je peut enlever ?------------------------------------
framefenetre.grid(row=1,column=0)
framegauche=Canvas(framefenetre,bg="red",width=Hauteur/2,height=Mafenetre.winfo_screenheight(),highlightthickness=0)
framegauche.grid(row=1,column=1,)
framegauche.pack_propagate(False)
	#.pack_propagete permet que la frame ne s'adapte pas aux elements dedans mais garde réelement la taille que l'on lui defini.
framecentre=Canvas(framefenetre,bg="green",width=Hauteur,height=Mafenetre.winfo_screenheight(),highlightthickness=0)
framecentre.grid(row=1,column=2,)
framecentre.pack_propagate(False)

framedroite=Canvas(framefenetre,bg="blue",width=Hauteur/2,height=Mafenetre.winfo_screenheight(),highlightthickness=0)
framedroite.grid(row=1,column=3,)
framedroite.pack_propagate(False)

#FOND D'ECRAN

fondfenetre=PhotoImage(file="Images/Background/fond1.png")
framegauche.create_image(0, 0, image=fondfenetre, anchor=NW)
framecentre.create_image(-(Hauteur/2), 0, image=fondfenetre, anchor=NW)
framedroite.create_image(-(Hauteur/2+Hauteur), 0, image=fondfenetre, anchor=NW)


#COORDONNES
panneaucoords =PhotoImage(file="Images/Background/fondcoords.png")

labcoordX= Label(framedroite,text="coordonnéesX", image=panneaucoords,compound=CENTER,borderwidth=0,highlightthickness=0,font="Courier 11 bold")
labcoordX.place(rely=1.0, relx=1.0, x=-60, y=0, anchor=SE)

labcoordY= Label(framedroite,text="coordonnéesY", image=panneaucoords,compound=CENTER,borderwidth=0,highlightthickness=0,font="Courier 11 bold")
labcoordY.place(rely=1.0, relx=1.0, x=0, y=0, anchor=SE)

#PANNEAU SCORES
fondscores=PhotoImage(file="Images/Background/fondscores.png")
framedroite.create_image(80, 60, image=fondscores, anchor=NW)

pommescore=PhotoImage(file="Images/Background/pommescore.png")
framedroite.create_image(130, 310, image=pommescore, anchor=NW)

medaille =PhotoImage(file="Images/Background/medaille.png")
framedroite.create_image(130, 210, image=medaille, anchor=NW)

fichier = open("Gestion_Highscore/highscore.txt", "r")
highscore=int(fichier.read())
fichier.close()



#BOUTONS
fondboutons=PhotoImage(file="Images/Background/fondboutons.png")
framegauche.create_image(10, 255, image=fondboutons, anchor=NW)
framegauche.create_text(150,300,fill="yellow",font="Helvetica 20 bold",text="Rejouer",)
framegauche.create_image(10, 555, image=fondboutons, anchor=NW)
framegauche.create_text(150,600,fill="yellow",font="Helvetica 20 bold",text="Quitter",)

#Button(framegauche, text ='Quitter',font="Courier 11 bold", command = Mafenetre.destroy, ).pack(side=LEFT,padx=5,pady=5)
#Button(framegauche, text ='Rejouer',font="Courier 11 bold", command = rejouer).pack(side=LEFT,padx=5,pady=5)

#GRILLE


fondimage =PhotoImage(file="Images/Background/fond.png")
Canevas = Canvas(framecentre, width = Largeur, height =Hauteur, bg ='chartreuse2',highlightthickness=0,)#highlightthickness represente les bordures du canvas
fondimage =PhotoImage(file="Images/Background/fond.png")
fond = Canevas.create_image(360,360,image=fondimage)#obligé de mettre le fond meme si il est dans le fondglobal car le fond d'un canevas n'est pas invisible
Canevas.focus_set()
Canevas.bind('<Key>',Clavier)
Canevas.place(relx=0.5, rely=0.5, anchor=CENTER)

#SERPENT+POMME
teteserpent =PhotoImage(file="Images/Snake/teteserpent.png")
corpsserpent =PhotoImage(file="Images/Snake/corpsserpent.png")
imagepomme =PhotoImage(file="Images/Snake/pomme.png")

LargeurSnake=int(20)#cela correspond en réalité a son rayon et non pas son diamètre.
teteX = 340
teteY = 340
PommeX= teteX + 10*LargeurSnake# = 5 cases plus loin
PommeY = teteY

Tete = Canevas.create_image(teteX,teteY,image=teteserpent)
Pomme = Canevas.create_image(PommeX,PommeY, image=imagepomme)
Corps1 = Canevas.create_image(teteX-40,teteY,image=corpsserpent)

#----------------DEBUT
perdu=True




rejouer()



Mafenetre.mainloop()