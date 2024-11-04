# 2024_2025__p04_projet1_gp2


# Membres

* Albert Le Guillou
* Raphaël Poinsignon
* Gabin Ozaneaux


# Objectifs du programme

* L'objectif du programme est de permettre à l'utilisateur de convertir un nombre de la base binaire, décimale ou hexadécimale vers la base binaire, décimale ou héxadécimale (il tourne en continu tant que l'utilisateur ne l'a pas arrêté afin d'éviter des manipulations inutiles)


# Définitions 

* nombre binaire : Le binaire est un système de numération de base 2 représentant des nombres en utilisant un modèle de uns et de zéros. Le système de numération binaire ne fait appel qu'aux chiffres 1 et 0.
* nombre décimal : système de numération de base 10 représentant n'importe quel nombre en utilisant un modèle qui ne fait appel qu'aux chiffres zéro, un, deux, trois, quatre, cinq, six, sept, huit et neuf.
* nomnbre hexadécimal : système de numération de base 16 représantant n'importe quel nombre en utilisant un modèle qui ne fait appel qu'aux chiffres zéro, un, deux, trois, quatre, cinq, six, sept, huit et neuf et aux lettres A, B, C, D, E et F
## exemple
* le nombre 160 en base décimale s'écrit 10100000 en binaire et s'écrit A0 en base hexadécimale

# Méthode
## Passer de la base décimale à la base binaire
* Diviser le nombre par 2
* Noter le reste
* Répéter
* Lire les restes à l'envers
## Passer de la base binaire à la base décimale
* Lister les puissances de 2 : Associez chaque chiffre binaire à une puissance de 2, en commençant par 0 à droite
* Calculer les valeurs
* Additionner les résultats
## Passer de la base décimale à la base hexadécimale
* Diviser le nombre par 16
* Noter le reste : Écrivez le reste de cette division. Ce reste sera un chiffre hexadécimal, où les valeurs de 10 à 15 sont représentées par les lettres A à F
* Répéter
* Lire les restes à l'envers
## Passer de la base hexa décimale à la base décimale
* Lister les puissances de 16 : Associez chaque chiffre hexadécimal à une puissance de 16, en commençant par 0 à droite
* Calculer les valeurs
* Additionner les résultats

# Compatibilité du programme

* ce programme est codé avec le langage de programmation python
* il est utilisable sur  les systèmes d'exploitation Windows, Mac, Linux mais pas sur Ios et Android


# Comment utiliser le programme (à modifier en fonction de la version finale : ordre et peut-être plus détailler)

* sélectionnez la base de déprt dans laquelle est écrite le nombre de départ que vous voulez convertir
* entrez votre nombre de départ
* sélectionnez la base dans laquelle vous voulez que votre nombre soit converti


# Répertoires ( à compléter après avoir organisé le fichier et fini le programme)

notre programme s'appuie sur diférents répertoires :
* le répertoire main qui contient les fonctions ................ qui permmettent de ......................
* le répertoire data ...............................
* le répertoire tools qui ...................................................

# Documentation

* docstring pour des apprendre de nouvelles notions python
* chat gpt pour trouver quelques informations et comprendre des eurreus
* diverses vidéo youtube pour comprendre comment passer de base en base

# à faire

* organiser dans les bons répertoires
* ajouter une fonction pour que le prgramme tourne en continu tant que l'utilsateur n'a pas appuyer sur une commande pour arrêter
* ajout des input
* ajout pour la vérification si l'utilisateur ne se trompe pas quand il indique une base pour son nombre de départ
