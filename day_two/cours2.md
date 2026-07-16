# Jour 2: Logique et Structures de Contrôle

Aujourd'hui, nous donnons un cerveau à notre programme. Nous allons apprendre à prendre des décisions et à répéter des actions.

## 1. Opérateurs de comparaison et Logique
Pour prendre des décisions, il faut comparer des choses.
- `==` (égal à), `!=` (différent de), `>` (supérieur), `<` (inférieur)
- `and` (et), `or` (ou), `not` (non)

age = 18
print("Est majeur ?", age >= 18)
print("A un permis mais moins de 25 ans ?", age >= 18 and age < 25)

## 2. Les conditions : if, elif, else
Permettent d'exécuter du code uniquement si une condition est vraie. **Attention à l'indentation (les espaces au début de la ligne) !** C'est ainsi que Python délimite ses blocs de code.

meteo = "pluie"

if meteo == "soleil":
    print("Je vais à la plage.")
elif meteo == "pluie":
    print("Je reste lire un livre.")
else:
    print("Je ne sais pas quoi faire.")

## 3. Les Boucles : while et for
- **while** : Répète tant qu'une condition est vraie.
- **for** : Parcourt les éléments d'une séquence (comme une liste).

# Boucle for
fruits = ["pomme", "banane", "cerise"]
for fruit in fruits:
    print("J'aime les", fruit + "s")

# Boucle while
compteur = 3
while compteur > 0:
    print("Décompte :", compteur)
    compteur -= 1
print("Décollage !")

fin de cours