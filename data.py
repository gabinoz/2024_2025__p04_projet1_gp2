from tools import *
# def dec_to_bin (start_number, init_base, target_base) :
#     start_number = 
#     target_number =
     
def reverse_chain (chain) :
    reversed_chain = ""
    for c in chain :
        reversed_chain = c + reversed_chain
    return reversed_chain

def bin_to_target_number(target_base):
    if target_base == 10:
        target_number = bin_to_dec(start_number)
    if target_base == 16:
        target_number = bin_to_dec(dec_to_bin (start_number))

def dec_to_target_number(target_base):
    if target_base== 2:
        target_number = dec_to_bin(start_number)
    if target_base == 16:
        target_number = dec_to_hex(start_number)

def hex_to_target_number(target_base):
    if target_base == 2:
        target_number = hex_to_dec(dec_to_bin(start_number))
    if target_base == 10:
        target_number = hex_to_dec(start_number)



def verifier_binaire(nb):  #utilisation de chat gpt pour la fonction
    # nombre = input("Veuillez entrer un nombre binaire: ")  #demande à l'utilisateur de rentrer un nombre
    if all(char in '01' for char in nb): # vérifier que le nombre ne contient que des 0 et/ou des 1, si c'est vrai alors le nombre ets bien en base binaire
        print(f"L'utilisateur dit que le nombre {nb} est en base binaire. C'est vrai, on peut continuer le code.")
    else: #si le nombre possède d'autres chiffres que 0 et 1 alors il n'est pas en base en binaire
        print(f"L'utilisateur dit que le nombre {nb} est en base binaire. C'est faux, veuillez entrer un nombre dans la base binaire pour continuer le code.")
print (verifier_binaire ('12'))
def verifier_decimal(nb): #fait sur le meme modèle sans chat gpt
    # nombre = input("Veuillez entrer un nombre décimal: ")
    if all(char in '0123456789' for char in nb):
        print(f"L'utilisateur a dit que le nombre {nb} est en base décimale. C'est vrai, on peut continuer le code.")
    else:
        print(f"L'utilisateur a dit que le nombre {nb} est en base décimale. C'est faux, veuillez entrer un nombre dans la base binaire pour continuer le code.")

def verifier_hexa(nb):  #fait sur le meme modèle sans chat gpt
    # nombre = input("Veuillez entrer un nombre en base hexadécimale : ")
    if all(char in '0123456789abcdefABCDEF' for char in nb): # l'utilisteur peut utiliser des lettres minuscules ou majuscules, il faut donc le prendre en compte
        print(f"L'utilisateur a dit que le nombre {nb} est en base hexadécimale. C'est vrai, on peut continuer le code.")
    else:
        print(f"L'utilisateur a dit que le nombre {nb} est en base hexadécimale. C'est faux, veuillez entrer un nombre dans la base héxadécimal pour continuer le code.")





hexa = [ 'A' , 'a' , 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f']

