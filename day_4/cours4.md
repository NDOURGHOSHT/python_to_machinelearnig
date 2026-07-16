Jour 4: Structures de Données Avancées et Gestion des Erreurs
Pour devenir un programmeur intermédiaire, il faut savoir choisir la bonne structure de données et anticiper les erreurs.

1. Les Dictionnaires
Contrairement aux listes (indexées par des numéros), les dictionnaires sont indexés par des clés (comme un vrai dictionnaire mot/définition). Très rapides et très utilisés en Python.

etudiant = {
    "nom": "Marie",
    "age": 21,
    "filiere": "Informatique"
}

print(etudiant["nom"])

# Ajouter/modifier une entrée
etudiant["moyenne"] = 15.5
print(etudiant)

## 2. Les Tuples
Comme les listes, mais **immuables** (on ne peut pas les modifier après création). Plus rapides et sécurisent les données.

coordonnees = (48.8566, 2.3522) # Latitude, Longitude de Paris
print("Latitude :", coordonnees[0])
# coordonnees[0] = 50.0  # ERREUR ! Les tuples ne se modifient pas.

## 3. Les Compréhensions de Listes
Une façon élégante et 'Pythonique' de créer des listes à partir de boucles.

# Version classique
carres = []
for i in range(5):
    carres.append(i ** 2)

# Version compréhension de liste
carres_comp = [i ** 2 for i in range(5)]
print(carres_comp)

## 4. Gestion des Exceptions (try/except)
Pour éviter que le programme ne plante, on 'attrape' les erreurs.
Le bloc else
Le code dans le bloc else s'exécute uniquement si aucune exception n'a été levée dans le bloc try.
    try:
    resultat = 10 / 2
        except ZeroDivisionError:
            print("Division par zéro")
        else:
            print("L'opération a réussi sans erreur.")

 Le bloc finally
 Le code dans le bloc finally s'exécute dans tous les cas, qu'une erreur se soit produite ou non. Il est idéal pour les actions de nettoyage, comme fermer un fichier ouvert ou clôturer une connexion réseau.
    fichier = open("donnees.txt", "r")
        try:
            contenu = fichier.read()
        finally:
            fichier.close()  # Toujours exécuté


try:
    nombre = int("Ce n'est pas un nombre")
except ValueError:
    print("Erreur : vous n'avez pas entré un entier valide.")
finally:
    print("Ce bloc s'exécute dans tous les cas.")

Bonnes pratiques
Spécifier le type d'erreur : 
Il est fortement déconseillé d'écrire un bloc except: vide car il intercepte toutes les erreurs (y compris les erreurs système), masquant ainsi des bugs critiques. Ciblez toujours des exceptions spécifiques (comme ValueError ou KeyError).
Utilisation de raise : 
Vous pouvez déclencher manuellement une exception dans votre code à l'aide de l'instruction raise.
