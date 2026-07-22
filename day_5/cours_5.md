# Jour 5: Programmation Orientée Objet (POO)

Félicitations pour être arrivé jusqu'ici ! La POO est un paradigme de programmation puissant qui consiste à modéliser le monde réel en créant des **Objets** issus de **Classes**. Vous passez ainsi au niveau intermédiaire.

## 1. Classes et Objets
- Une **Classe** est un plan de fabrication (ex: le concept d'une Voiture).
- Un **Objet** est une instance de ce plan (ex: ma voiture spécifique rouge).
- Les **Attributs** sont les caractéristiques (ex: couleur, marque).
- Les **Méthodes** sont les actions (ex: démarrer, freiner).

exemple de code:

class Voiture:
    # La méthode __init__ est le constructeur, appelé à la création de l'objet
    def __init__(self, marque, couleur):
        self.marque = marque    # self représente l'objet en cours de création
        self.couleur = couleur
        self.vitesse = 0        # Attribut par défaut

    def accelerer(self):
        self.vitesse += 10
        print(f"La {self.marque} roule à {self.vitesse} km/h.")

# Création d'objets (instances)
ma_voiture = Voiture("Renault", "Bleue")
ta_voiture = Voiture("Peugeot", "Rouge")

ma_voiture.accelerer()
ma_voiture.accelerer()

## 2. L'Héritage
L'héritage permet de créer une nouvelle classe qui réutilise les attributs et méthodes d'une classe existante (la classe parent).

class VoitureElectrique(Voiture):  # Hérite de Voiture
    def __init__(self, marque, couleur, autonomie):
        super().__init__(marque, couleur)  # Appelle le constructeur du parent
        self.autonomie = autonomie

    def recharger(self):
        print("Batterie en charge...")

tesla = VoitureElectrique("Tesla", "Blanche", 500)
tesla.accelerer()  # Héritée de Voiture
tesla.recharger()   # Spécifique à VoitureElectrique