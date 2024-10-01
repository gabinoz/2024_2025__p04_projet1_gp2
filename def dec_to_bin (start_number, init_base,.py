def dec_to_bin (start_number, init_base, target_base) :
    restes = ""
    while start_number > 0:
        reste = start_number % 2    
        restes = str(reste) + restes  #.append (reste)
        start_number = start_number//2
    return restes

def dec_to_target_number(start_number, init_base, target_base):
    if target_base == 2:
        return dec_to_bin(start_number, init_base, target_base) 
    



def bin_dec_hex__to__bin_dec_hex (start_number, init_base, target_base):
    if init_base == 10:
        return dec_to_target_number(start_number, init_base, target_base)

            




resultat = bin_dec_hex__to__bin_dec_hex(27, 10, 2)
print(resultat)