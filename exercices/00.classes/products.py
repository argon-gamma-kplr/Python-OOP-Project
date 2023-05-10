class Products:
    def __init__(self, cost, price, marque):
        self.cost = cost
        self.price = price
        self.marque=marque

class Mobilier(Products):
    def __init__(self, cost, price, marque, materiaux, couleur, dimensions):
        super().__init__(cost, price, marque)
        self.materiaux = materiaux
        self.couleur = couleur
        self.dimensions = dimensions
    
class Canape(Mobilier):
    """from Mobilier"""
class Chaise(Mobilier):
    """from Mobilier"""
class Table(Mobilier):
    """from Mobilier"""

canape1 = Canape(1000,2000,"OKLM","Cuir","Blanc", (200,100,80))
canape2 = Canape(800,1600,"SIESTA","TISSU","Bleu", (150,90,70))
 
chaise1 = Chaise(50,100,"PEPOUSE","Plastique","Rouge",(50,50,70))
chaise2 = Chaise(75,150,"PEPOUSE","Metal","Gris",(60,60,80))
 
table1 = Table(250,500,"TEX","Bois","Chêne",(150,80,75))
table2 = Table(350,700,"TEX","Verre","Transparent",(120,60,75))