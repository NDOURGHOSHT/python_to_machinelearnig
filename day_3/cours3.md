# Jour 3 : Fonctions et Programmation Modulaire

Jusqu'ici, nous écrivions du code séquentiel. Aujourd'hui, nous apprenons à encapsuler ce code dans des **fonctions** réutilisables pour organiser nos programmes.

## 1. Définir et appeler une fonction
Une fonction est un bloc de code nommé. Elle peut prendre des *paramètres* en entrée et *retourner* un résultat.

def saluer(nom, age):
    """Ceci est une docstring : elle explique ce que fait la fonction."""
    message = "Bonjour " + nom + ", tu as " + str(age) + " ans."
    return message

# Appel de la fonction
resultat = saluer("Bob", 30)
print(resultat)
2. Paramètres par défaut
On peut donner des valeurs par défaut aux paramètres. Ils deviennent optionnels lors de l'appel.

def preparer_cafe(type_cafe="Espresso"):
    return "Voici votre " + type_cafe

print(preparer_cafe())               # Utilise la valeur par défaut
print(preparer_cafe("Cappuccino"))   # Surcharge la valeur par défaut

3. Portée des variables (Scope)
Les variables créées à l'intérieur d'une fonction n'existent pas à l'extérieur. C'est la portée locale.

x = 10  # Variable globale

def ma_fonction():
    x = 5  # Variable locale
    print("x à l'intérieur :", x)

ma_fonction()
print("x à l'extérieur :", x)

4. Les Modules
Un module est un fichier contenant des fonctions. On l'importe avec import.

import math

# On accède aux fonctions du module avec un point
racine = math.sqrt(16)
print("La racine carrée de 16 est", racine)