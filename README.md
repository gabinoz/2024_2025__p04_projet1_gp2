# 2024_2025__p04_projet1_gp2


# Membres

* Albert Le Guillou
* Raphaël Poinsignon
* Gabin Ozaneaux


# Objectifs du programme

* L'objectif du programme est de permettre à l'utilisateur de convertir un nombre de la base binaire, décimale ou hexadécimale vers la base binaire, décimale ou héxadécimale 


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
* Répéter jusqu'à ce que le quotient de la division euclidienne soit égal  0
* Lire les restes à l'envers
## Passer de la base binaire à la base décimale
* Lister les puissances de 2 : Associez chaque chiffre binaire à une puissance de 2, en commençant par 0 à droite
* Calculer les valeurs
* Additionner les résultats
## Passer de la base décimale à la base hexadécimale
* Diviser le nombre par 16
* Noter le reste : Écrivez le reste de cette division. Ce reste sera un chiffre hexadécimal, où les valeurs de 10 à 15 sont représentées par les lettres A à F
* Répéter jusqu'à ce que le quotient de la division euclidienne soit égal  0
* Lire les restes à l'envers
## Passer de la base hexa décimale à la base décimale
* Lister les puissances de 16 : Associez chaque chiffre hexadécimal à une puissance de 16, en commençant par 0 à droite
* Calculer les valeurs
* Additionner les résultats

# Compatibilité du programme

* ce programme est codé avec le langage de programmation python
* il est utilisable sur  les systèmes d'exploitation Windows, Mac, Linux mais pas sur Ios et Android


# Comment utiliser le programme 

* entrez votre nombre de départ
* sélectionnez la base de départ dans laquelle est écrite le nombre de départ que vous voulez convertir
* sélectionnez la base dans laquelle vous voulez que votre nombre soit converti


# Répertoires 

notre programme s'appuie sur diférents répertoires :
* le répertoire main qui contient les fonctions in_dec_hex__to__bin_dec_hex et do_the_job qui permettent d'appeler les d'appeler les fonctions de tools et d'éxécuter le programme.

* le répertoire tools qui contient toutes les fonctions calculatoires, les fonctions ask et la fonction verifParam qui permet de vérifier que les variables entées sont justes.

# Documentation

* docstring pour apprendre de nouvelles notions python
* chat gpt pour trouver quelques informations et comprendre des erreurs
* diverses vidéo youtube pour comprendre comment passer d'une base donnée vers une autre base


