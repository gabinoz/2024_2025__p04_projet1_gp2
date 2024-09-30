from tools import *
from data import *

def bin_dec_hex__to__bin_dec_hex (start_number, init_base, target_base):
    if init_base == 2 :
        pass
    if init_base == 10 :
        pass
    if init_base == 16 :
        pass
    target_number = None
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
