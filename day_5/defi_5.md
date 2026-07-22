Défi : Système de surveillance d'un poulailler

Tu dois créer un programme orienté objet qui gère plusieurs capteurs.

Partie 1 : La classe mère

Crée une classe appelée Capteur.

Elle doit contenir :

Attributs
nom
unite
valeur (initialisée à 0)
Méthodes
lire() qui affiche :
Nom : Température
Valeur : 28 °C

(en adaptant selon le capteur).

Partie 2 : Héritage

Crée trois classes qui héritent de Capteur :

CapteurTemperature
CapteurHumidite
CapteurGaz

Chaque classe doit posséder une méthode spécifique.

Par exemple :

CapteurTemperature
    mesurer_temperature()

CapteurHumidite
    mesurer_humidite()

CapteurGaz
    mesurer_gaz()

Ces méthodes peuvent simplement afficher un message, par exemple :

Mesure de la température...
Partie 3 : Les objets

Crée les objets suivants :

température
humidité
gaz

Puis attribue les valeurs suivantes :

Température = 29
Humidité = 67
Gaz = 320
Partie 4 : Affichage

Affiche les informations de chaque capteur grâce à la méthode lire().

Tu devrais obtenir quelque chose comme :

Nom : Température
Valeur : 29 °C

Nom : Humidité
Valeur : 67 %

Nom : Gaz
Valeur : 320 ppm
Bonus (niveau supérieur)

Ajoute une méthode appelée alerte().

Pour la température :
si la température > 35 → afficher "Alerte : température élevée !"
Pour l'humidité :
si l'humidité < 40 → afficher "Humidité trop faible !"
Pour le gaz :
si la valeur > 500 → afficher "Gaz dangereux !"
Super bonus (si tu veux te challenger)

Fais en sorte que les méthodes mesurer_temperature(), mesurer_humidite() et mesurer_gaz() modifient automatiquement la valeur du capteur (par exemple avec des valeurs aléatoires grâce au module random), puis appelle lire() pour afficher la nouvelle mesure.

💪 Règle du défi : essaie de le faire sans regarder d'exemple. Écris ton code de mémoire. Ensuite, envoie-moi ton programme, et je le corrigerai comme un professeur : je te dirai ce qui est bien, ce qui peut être amélioré et je t'expliquerai les erreurs éventuelles, sans simplement te donner la solution.