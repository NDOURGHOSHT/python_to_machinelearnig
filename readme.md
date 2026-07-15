Voici les commandes exactes à taper dans le terminal de VS Code pour lier votre projet à GitHub.
1. Initialiser le projet local
bash
    git init
2. Vérifier le statut des fichiers
bash
    git status
3. Préparer les fichiers (Staging)
bash
    git add index.html "pour un fichier particulier, par contre pour tout les fichier use " git add .
4. Enregistrer les modifications (Commit)
bash
    git commit -m "Mon tout premier commit"
5. Connecter le projet local à GitHub
bash
    git remote add origin https://github.com 
    Note : Vous ne tapez cette commande qu'une seule fois par projet.
6. Envoyer le code sur GitHub (Push)
bash
    git branch -M main
    git push -u origin main

