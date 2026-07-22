class Etudiant:
    def __init__(self, nom, age, note):
        # À COMPLÉTER : Assignez 'nom', 'age' et 'note' aux attributs de l'objet (ex: self.nom = nom)
        self.nom = nom
        self.age = age
        self.note = note

    def afficher_infos(self):
        # À COMPLÉTER : Retournez une chaîne de caractères qui combine les attributs
        # Exemple attendu : "Nom: Alice, Âge: 20, Note: 15"

        return f"Nom: {self.nom}, Age: {self.age}, Note: {self.note}"
e1 = Etudiant("FATOU", 22, 18)
print(e1.afficher_infos())