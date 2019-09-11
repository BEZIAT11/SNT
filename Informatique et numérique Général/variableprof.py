# Une variable est une case dans la mémoire de l'ordinateur. Cette case contient 
# un objet (ce peut être un nombre, un texte) et cette case porte un nom.

# Exo 1 : Lance le programme, puis indique 
# a- quelles sont les variables dans ce programme 
# b- quel objet contient la 1ère variable
# c- quel type d'objet est-ce ?
# d- Quelle différence entre taper  
# print(variable) et print("variable")?
print ("Exo 1")
nombre1 = 5
nombre2 = 10
texte1 = "bonjour"
texte2 = "Tu as gagné"
texte3 = "donne"
print(nombre1)
print("nombre1")
print(texte1)
print("texte1")

# Exo 2 : Lance le programme
# Indique ce que fais chaque ligne et/ou explique pourquoi il y a une erreur
print ()
print ("Exo 2")
print(nombre1 + nombre2)
print("nombre1 + nombre2")
print("nombre1" + "nombre2")
print(texte1 + texte2)
print(texte1 + "texte2")

# Exo 3 : NE lance PAS le programme
# Indique ce que fait chaque ligne d'après toi et/ou
# explique pourquoi il y a une erreur.
print ()
print ("Exo 3")
print("nombre1" + "texte1" + "nombre2")
# print(nombre1 + texte1 + nombre2)

# Exo 4 : Ecrire la ligne de code permettant de 
# voir s'afficher dans l'interpréteur : 
# une 1ère ligne : "Bonjour" en utilisant seulement des variables
# une 2ème ligne : "5 + 10 donne" en utilisant seulement des variables et de la ponctuation
# une 3ème ligne avec le résultat qui s'affiche en utilisant seulement des variables et de la ponctuation
# la 4ème ligne : "Tu as gagné" en utilisant seulement des variables
print ()
print ("Exo 4")
print(texte1)
print(nombre1, " + ", nombre2, " ", texte3)
print(nombre1 + nombre2)
print(texte2)