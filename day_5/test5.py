class Voiture:
    def __init__(self, p_couleur, p_marque, p_vitesse = 0):
        self.couleur = p_couleur
        self.marque = p_marque
        self.vitesse = p_vitesse
    def accelerer(self, p_vitesse):
        self.vitesse += p_vitesse
    def decelerer(self, p_vitesse):
        self.vitesse -= p_vitesse
voiture_bleu = Voiture("bleu","TESLA")
voiture_rouge = Voiture("rouge","BMW")

print("la voiture bleu")
print(f"La marque est {voiture_bleu.marque} de couleur :{voiture_bleu.couleur}" )
print("ET de vitesse")
voiture_bleu.accelerer(10)
print(voiture_bleu.vitesse)
print("-"*10)
print(voiture_rouge.couleur)