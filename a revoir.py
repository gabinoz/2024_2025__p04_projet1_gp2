from tools import *
def dec_to_bin (start_number, init_base, target_base) :
    restes = ""
    while start_number // 2 != 0:
        reste = start_number % 2    
        restes = reste + restes  #.append (reste)
        reste = reste //2
        

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











from tools import *
from data import *

def bin_dec_hex__to__bin_dec_hex (start_number, init_base, target_base):
    if target_base == init_base:
        target_number = start_number
    else:
        if init_base == 2 :
            bin_to_target_number(target_base)
        if init_base == 10 :
            dec_to_target_number(target_base)
        if init_base == 16 :
            hex_to_target_number(target_base)
            
    return target_number


assert bin_dec_hex__to__bin_dec_hex (101, 2, 10) == 5

def do_the_job ():
    init_number = ask_for_the_init_number ()
    init_base = ask_for_the_init_base ()
    target_base = ask_for_the_target_base ()
    target_number = \
      bin_dec_hex__to__bin_dec_hex (init_number, \
                                    init_base, \
                                    target_base)

do_the_job ()










def ask_for_the_init_number () : # la fonction renvoie un int 
    init_nb = int (input ('Entrez le nombre de départ, qui doit être entier :'))
    return init_nb

def ask_for_the_init_base () : # Les bases sont des entiers
    init_base = int (input ("Entrez la base de départ (2 pour le binaire, 10 pour le décimal, 16 pour l'hexadécimal) :"))

def ask_for_the_target_base () : # La base est entière
    target_base = int (input ("Entrez la base visée (2 pour le binaire, 10 pour le décimal, 16 pour l'hexadécimal) :"))


    pass
#     v = [x]
#     for c in v :

#     return x

def hex_to_dec () :
    pass






