from math import pi
from typing import Callable

from matplotlib import markers, pyplot as plt
from numpy import around
from functions import *



# Définition de l'équation et des conditions initiales

def f(x, y, y1): # Équation différentielle, de la forme y''=f(x,y,y')
    return -y     

xa=0 # Position de la première condition initiale xa
xb= pi/2 # Position de la seconde condition initiale xb

ya=1 # Valeur de y(xa)
yb=1/2 # Valeur de y(xa)

dy1a=1/2 # Pas de tir

n= 100 # Permet de définir le pas utilisé dans l'algorithme d'Euler h = (xb-xa)/n


########################################################


def shot(f: Callable, xa: float, xb: float, ya: float, yb: float, dy1a: int, n: int):  # dy1a = m1-m0 /  n =
    tirs = []
    y1a = (yb-ya)/(xb-xa)   # initialisation de m0
    y1 = y1a
    yb_shot = Euler(f, xa, xb, ya, y1, n)["yb"]
    list_m = []
    list_yb = []

    if yb_shot < yb:  # on vérifie si le tir initial est trop court ou trop long
        while yb_shot < yb:  # on effectue des tirs par incrément tant que le tir
            #   est trop court en s'assurant de bien dépassé la cible
            new_shot = Euler(f, xa, xb, ya, y1, n)
            yb_shot = new_shot["yb"]
            tirs.append(new_shot)
            list_yb.append(yb_shot)
            list_m.append(y1)
            y1 += dy1a  # On incrémente la valeur de mk
    elif yb_shot > yb:
        while yb_shot > yb:
            new_shot = Euler(f, xa, xb, ya, y1, n)
            yb_shot = new_shot["yb"]
            tirs.append(new_shot)
            list_yb.append(yb_shot)
            list_m.append(y1)
            y1 -= dy1a  # On incrémente la valeur de mk

    return ({"tirs": tirs, "list_m": list_m, 'list_yb': list_yb, 'y1a': y1a})


new_shot = shot(f, xa,xb, ya, yb, dy1a, n)

tirs, list_m, list_yb, y1a = new_shot.values()


x = np.linspace(xa, xb, n, endpoint=True) # Axe des abcisses 


# Création avec matplotlib.pyplot de deux graphiques sur une même fenêtre


figure, (graph1,graph2) = plt.subplots(2)


# Trace la courbe de chaque tir

for i, tir in enumerate(tirs):
    graph1.plot(tir["x_array"],tir["y_array"], label = 'Tir '+str(i+1))



# Nous traçons la droite passant par le point de départ du tir et la cible 

graph1.plot(x, y1a*x + ya, label='Droite reliant les deux point',c="red") 
graph2.plot(x, y1a*x + ya, label='Droite reliant les deux point',c="red")




graph1.axis([xa-1/100, xb+1/10, 0, yb+ya]) # Recentre l'affichage du graphique


interpolation_m = lagrange(list_m, list_yb) # Polynôme de Lagrange avec noeuds: liste des m et image: liste des yb

for k in x:
    if np.around(interpolation_m(k)) == np.around(yb):
        best_y1a = k
print("La meilleure approximation de y'(b) est " + str(best_y1a))



best_shot = Euler(f, xa, xb, ya, best_y1a, n)

arounded_y1a = around(best_y1a,3)



# Définition des titres des graphs 

graph1.set_title('Graph des tirs effectués')
graph2.set_title('Graph du meilleur tir pour m='+str(arounded_y1a))

graph2.plot(best_shot["x_array"],best_shot["y_array"],label="Meilleur tir pour m=" + str(arounded_y1a))



# On place les points de départ et d'arrivée des tirs 

graph1.scatter(xa,ya, c="red",label="Point de départ du tir en (xa,ya)")
graph2.scatter(xa,ya, c="red",label="Point de départ du tir en (xa,ya)")

graph1.scatter(xb,yb, c="red",marker="x",label="Cible en (xb,yb)")
graph2.scatter(xb,yb, c="red",marker="x",label="Cible en (xb,yb)")

# Affichage des légendes et des graphiques

graph2.legend()
graph1.legend()

plt.show()



