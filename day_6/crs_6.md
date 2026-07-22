# Jour 6: Introduction à NumPy

Bienvenue dans la semaine Data Science ! Aujourd'hui, nous découvrons **NumPy** (Numerical Python). C'est la bibliothèque de référence pour manipuler des données numériques en Python.

## 1. Pourquoi NumPy ?
En Python classique, on utilise des listes. Mais pour faire des calculs mathématiques sur de grandes quantités de données, les listes sont lentes. NumPy introduit le **ndarray** (tableau N-dimensionnel), qui est beaucoup plus rapide et occupe moins de mémoire.

import numpy as np # On importe numpy et on lui donne le surnom 'np' (une convention universelle)

# Création d'un tableau numpy à partir d'une liste
notes = np.array([12, 15, 9, 18, 11])
print(notes)
print("Type de l'objet :", type(notes))

## 2. Dimensions et Formes (Shape)
Un tableau NumPy peut avoir 1 dimension (une ligne), 2 dimensions (une matrice avec lignes et colonnes) ou plus. La méthode `.shape` nous donne sa forme.

matrice = np.array([[1, 2, 3], [4, 5, 6]])
print(matrice)
print("Forme (lignes, colonnes) :", matrice.shape)

## 3. Opérations vectorisées
La vraie magie de NumPy : on peut faire des opérations mathématiques directement sur le tableau entier sans écrire de boucle `for` !

print("Notes + 2 (points bonus) :", notes + 2)
print("Notes multipliées par 2 :", notes * 2)
print("Moyenne des notes :", notes.mean())