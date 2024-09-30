from tools import *
# def dec_to_bin (start_number, init_base, target_base) :
#     start_number = 
#     target_number =
     


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
