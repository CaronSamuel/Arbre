################################
################################
########CARON Samuel APP########
#######TP3/ Arbre Binaire#######
################################
################################

class ArbreBinaire:
    def __init__(self, data) -> None:
        self.data = data
        self.enfantDroite = None
        self.enfantGauche = None
        self.parent = None
        
    def __repr__(self) -> str:
        return str(self.data)
    
    # Fonction qui ajoute un noeuf à l'arbre
    def ajouterNoeud(self, data : int) -> None :
        if data < self.data :
            if self.enfantGauche == None :
                self.enfantGauche = ArbreBinaire(data)
                self.enfantGauche.parent = self
            else :
                self.enfantGauche.ajouterNoeud(data)
        else :
            if self.enfantDroite == None :
                self.enfantDroite = ArbreBinaire(data)
                self.enfantDroite.parent = self
            else :
                self.enfantDroite.ajouterNoeud(data)
                
    # Parcours infixe
    def parcoursInfixe(self) -> None :
        if self == None :
            return "L'arbre est vide"
        if self.enfantGauche != None :
            self.enfantGauche.parcoursInfixe()
        if self.enfantDroite != None :
            self.enfantDroite.parcoursInfixe()
        print(self)
            
    # Recherche valeur
    def recherche(self, valeur : int) -> str:
        if self == None :
            return "L'arbre est vide"
        else : 
            if self.data == valeur :
                return "La valeur est bel est bien dans l'arbre"
            else :
                if valeur < self.data :
                    if self.enfantGauche != None :
                        return self.enfantGauche.recherche(valeur)
                    else :
                        return "Valeur non trouvée"
                elif valeur > self.data :
                    if self.enfantDroite != None :
                        return self.enfantDroite.recherche(valeur)
                    else :
                        return "Valeur non trouvée"
        return "Valeur non trouvée"
            
                
if __name__ == "__main__":
    arb = ArbreBinaire(10)
    arb.ajouterNoeud(3)
    arb.ajouterNoeud(15)
    arb.ajouterNoeud(34)
    arb.ajouterNoeud(2)
    print(arb)
    print(arb.enfantDroite)
    print(arb.enfantDroite.enfantDroite)
    print(arb.enfantDroite.enfantGauche)
    print()
    print("Parcours Infixe :")
    print(arb.parcoursInfixe())
    print()
    print("Recherche :")
    print(arb.recherche(4))
    print(arb.recherche(10))