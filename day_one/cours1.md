# Jour 1 : Premiers pas en Python et Bases de l'Algorithmique

Bienvenue dans ce parcours de 5 jours pour passer de zéro à intermédiaire en Python ! Aujourd'hui, nous posons les fondations.

## 1. Qu'est-ce que Python ?
Python est un langage de programmation **interprété**, ce qui signifie qu'un programme (l'interpréteur) lit et exécute votre code ligne par ligne. Il est réputé pour sa syntaxe claire qui ressemble à de l'anglais simplifié.

## 2. Les Variables
Une variable est comme une boîte avec une étiquette. On y range une donnée pour s'en servir plus tard.
________________________________________________________________________

# Assignation de variables
age = 25          # Un entier (int)
prenom = "Alice"  # Une chaîne de caractères (str)
taille = 1.65     # Un nombre à virgule flottante (float)
est_majeur = True # Un booléen (bool : True ou False)

print("Bonjour", prenom, "tu as", age, "ans.")

3. Les Listes (Première structure de données)
Une liste permet de stocker plusieurs éléments dans un ordre précis. On utilise des crochets [].

courses = ["Pommes", "Pain", "Lait"]
print(courses)

# Accéder aux éléments (l'index commence à 0 !)
print("Premier article :", courses[0])

# Ajouter un élément
courses.append("Oeufs")
print("Liste mise à jour :", courses)

4. Manipuler les chaînes de caractères (Slicing)
Le slicing (tranchage) permet d'extraire des morceaux d'une liste ou d'une chaîne de texte. Syntaxe : variable[début:fin:pas] (la fin n'est pas incluse).

alphabet = "abcdefghijklmnopqrstuvwxyz"

print("Les 5 premières lettres :", alphabet[0:5])
print("Tout sauf les 3 dernières :", alphabet[:-3])
print("Une lettre sur deux :", alphabet[::2])

5. Ajouter un ou plusieur truc dans une liste a diferente position
Pour ajouter un chiffre (ou un nombre) dans une liste en Python, vous devez utiliser la méthode .append(). Elle insère la nouvelle valeur tout à la fin de la liste existante:

# 1. Création d'une liste de nombres
notes = [12, 15, 14]

# 2. Ajout du nombre 18 à la fin de la liste
notes.append(18)

# 3. Affichage du résultat
print(notes)  
# Affiche : [12, 15, 14, 18]

Deux autres méthodes utiles pour votre coursSelon ce que les étudiants voudront faire, deux autres techniques sont indispensables en Data Science :
1. Insérer un chiffre à un endroit précis : .insert()Si vous ne voulez pas ajouter le chiffre à la fin, mais à une position précise (un index), utilisez .insert(index, valeur). En informatique, on commence à compter à partir de 0.

nombres = [10, 20, 30]

# Insérer le chiffre 15 à l'index 1 (donc en deuxième position)
nombres.insert(1, 15)

print(nombres)  
# Affiche : [10, 15, 20, 30]

2. Ajouter plusieurs chiffres d'un coup : .extend()Si vous essayez d'utiliser .append([5, 6]), Python va insérer une liste à l'intérieur de la liste. Pour fusionner proprement plusieurs nombres, utilisez .extend().
mes_nombres = [1, 2, 3]

# Ajouter une liste de plusieurs chiffres
mes_nombres.extend([4, 5, 6])

print(mes_nombres)  
# Affiche : [1, 2, 3, 4, 5, 6]


fin de cours.