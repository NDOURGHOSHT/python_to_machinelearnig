nombre_secret = 6467
nbr = 0

while nbr != nombre_secret :

    nbr = int(input ("Deviner le nombre exacte ")) 
    if nbr < nombre_secret :
        print ("Donne un nombre plus grand")
    elif nbr > nombre_secret :
        print ("Donne un nombre plus petit")
    else :
        print( "Bravo, vous avez gagné")