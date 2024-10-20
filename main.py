from tools import *
from data import *

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


# assert bin_dec_hex__to__bin_dec_hex (101, 2, 10) == 5

def do_the_job ():
    init_number = ask_for_the_init_number ()
    init_base = ask_for_the_init_base ()
    target_base = ask_for_the_target_base ()
    target_number = \
      bin_dec_hex__to__bin_dec_hex (init_number, \
                                    init_base, \
                                    target_base)
    print (f"Le nombre cxonverti est : {target_number}")

do_the_job ()
