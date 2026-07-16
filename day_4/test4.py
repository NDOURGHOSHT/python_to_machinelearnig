# etudiant = {
#     "nom": "marie",
#     "age": 15,
#     "filiaire": "informatique"
# }
# # print(etudiant["age"])
# etudiant["moyenne"]= 16
# print(etudiant)

# coordonnees = (48.8566, 2.3522) # Latitude, Longitude de Paris
# print("Latitude :", coordonnees[0])

# Version classique
# carres = []
# for i in range(6):
#     carres.append(i ** 2)

# # Version compréhension de liste
# carres_comp = [i ** 2 for i in range(5)]
# print(carres_comp)

# try:
#     # Code pouvant générer une erreur
#     nombre = int(input("Entrez un nombre : "))
#     resultat = 10 / nombre
#     print(f"Le résultat est : {resultat}")
# except ValueError:
#     print("Erreur : Veuillez entrer un entier valide.")
# except ZeroDivisionError:
#     print("Erreur : Vous ne pouvez pas diviser par zéro.")


# Toutes les clés sont enregistrées en minuscules
carnet = {
    "bob": "64534763468",
    "alice": "0612345678"
}

try:
    nom = input("Entrez le nom: ")
    # On transforme la saisie en minuscules pour correspondre aux clés
    nom_minuscule = nom.lower()
    
    print(f"Voilà le numéro de {nom} : {carnet[nom_minuscule]}")
    
except KeyError:
    print(f"Désolé, '{nom}' n'est pas dans le carnet.")

# Option 2 : 
# Ajouter automatiquement le nom s'il n'existe pasSi le nom est introuvable, 
# le bloc except prend le relais. Vous pouvez alors demander à l'utilisateur 
# s'il souhaite ajouter ce nouveau contact directement dans le dictionnaire.

# carnet = {
#     "bob": "64534763468",
#     "Alice": "0612345678"
# }

# try:
#     nom = input("Entrez le nom: ")
#     print(f"Voilà le numéro de {nom} : {carnet[nom]}")
    
# except KeyError:
#     print(f"'{nom}' n'est pas dans le carnet.")
#     # On propose de l'ajouter
#     reponse = input(f"Voulez-vous ajouter {nom} ? (oui/non) : ").lower()
    
#     if reponse == "oui":
#         numero = input(f"Entrez le numéro pour {nom} : ")
#         carnet[nom] = numero  # Ajout du nouveau couple clé:valeur
#         print(f"{nom} a bien été ajouté au carnet !")
#         print("Nouveau carnet :", carnet)
#     else:
#         print("Recherche abandonnée.")
