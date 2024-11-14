def bin_to_target_number(target_base, start_number):
    if target_base == 10:
        target_number = bin_to_dec(start_number)
    if target_base == 16:
        target_number = dec_to_hex(bin_to_dec(start_number))
    return target_number

def bin_to_dec(start_number):
    cpt = 0
    nombre_en_decimal = 0
    start_number = str(start_number)
    for chiffres in start_number[::-1]:
        nombre_en_decimal += int(chiffres) * 2** cpt
        cpt += 1
    return nombre_en_decimal


def dec_to_target_number(target_base, start_number):
    if target_base == 2:
        target_number = dec_to_bin(start_number)
    if target_base == 16:
        target_number = dec_to_hex(start_number)
    return target_number

def hex_to_target_number(target_base, start_number):
    if target_base == 2:
        target_number = hex_to_dec(dec_to_bin(start_number))
    if target_base == 10:
        target_number = hex_to_dec(start_number)
    return target_number

def hex_to_dec(start_number):
    # Définit les valeurs hexadécimales pour les chiffres de 0 à F
    base_hex_lettres = "0123456789ABCDEF"
    nombre_en_decimal = 0
    cpt = 0

    # Parcourt les chiffres du nombre hexadécimal de droite à gauche
    for chiffre in start_number[::-1]:
        # Trouver la valeur décimale correspondant au chiffre hexadécimal
        valeur = base_hex_lettres.index(chiffre)
        # Calculer la contribution de chaque chiffre en base 16
        nombre_en_decimal += valeur * (16 ** cpt)
        cpt += 1

    return nombre_en_decimal


def dec_to_bin(start_number) :
    restes = ""
    while start_number > 0:
        reste = start_number % 2    
        restes = str(reste) + restes  #.append (reste)
        start_number = start_number//2
    return restes

def dec_to_hex(start_number):
    base_hex = [0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]
    nb_hex_final = ""
    while start_number > 0:
        reste = start_number % 16
        nb_hex = base_hex[reste]
        nb_hex_final =  str(nb_hex) + nb_hex_final
        start_number = start_number// 16
    return nb_hex_final


def ask_for_the_init_number():
    init_nb = input('Entrez le nombre de départ : ')
    return init_nb
        
def ask_for_the_init_base () : 
    init_base = int (input ("Entrez la base de départ (2 pour le binaire, 10 pour le décimal, 16 pour l'hexadécimal) :"))
    return init_base

def ask_for_the_target_base () : 
    target_base = int (input ("Entrez la base visée (2 pour le binaire, 10 pour le décimal, 16 pour l'hexadécimal) :"))
    return target_base


def verifParam(init_number,init_base,target_base) :

    if init_base == 2:
        if not all(char in '01' for char in init_number):
            print("Erreur : le nombre saisi n'est pas en base binaire.")
            return False
    elif init_base == 10:
        if not all(char in '01234567890' for char in init_number):
            print("Erreur : le nombre saisi n'est pas en base décimale.")
            return False
    elif init_base == 16:
        if not all(char in '0123456789ABCDEFabcdef' for char in init_number):
            print("Erreur : le nombre saisi n'est pas en base hexadécimale.")
            return False
    else:
        print("Base initiale invalide. Seules les bases 2, 10 et 16 sont supportées.")
        return False
    
    if target_base != 10 and target_base!=2 and target_base!=16 :
        print("Base target invalide. Seules les bases 2, 10 et 16 sont supportées.")
        return False
    
    #tout est ok
    return True