from tools import *

#Convertit 
def bin_dec_hex__to__bin_dec_hex (start_number, init_base, target_base):
    if target_base == init_base:
        target_number = start_number
    else:
        if init_base == 2 :
            target_number = bin_to_target_number(target_base, start_number)
        if init_base == 10 :
            target_number = dec_to_target_number(target_base, start_number)
        if init_base == 16 :
            target_number = hex_to_target_number(target_base, start_number)
    return target_number

def do_the_job():
    # Demander le nombre de départ
    init_number = ask_for_the_init_number()
    
    # Demander la base source
    init_base = ask_for_the_init_base()

    # Demander la base cible
    target_base = ask_for_the_target_base ()
  
    if (verifParam(init_number,init_base,target_base)):
    # Effectuer la conversion
        target_number = bin_dec_hex__to__bin_dec_hex(init_number, init_base, target_base)

        # Afficher le résultat
        print(f"Le nombre converti est : {target_number}")


do_the_job ()
