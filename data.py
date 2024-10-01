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



def verifier_binaire():
    nombre = input("Veuillez entrer un nombre: ")
    if all(char in '01' for char in nombre):
        print(f"L'utilisateur dit que le nombre est en base binaire : {nombre}. C'est vrai, on peut continuer le code")
    else:
        print(f"L'utilisateur dit que le nombre est en base binaire : {nombre}. C'est faux, veuillez entrer un nombre dans la base binaire pour continuer le code")

def verifier_decimal():
    nombre = input("Veuillez entrer un nombre: ")
    if all(char in '0123456789' for char in nombre):
        print(f"L'utilisateur a dit que le nombre est en base décimale : {nombre}. C'est vrai, on peut continuer le code")
    else:
        print(f"L'utilisateur a dit que le nombre est en base décimale : {nombre}. C'est faux, veuillez entrer un nombre dans la base binaire pour continuer le code")


