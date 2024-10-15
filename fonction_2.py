def bin_to_dec (start_number):
    cpt = 0
    dec_number = 0 
    start_number = str (start_number)
    for digit in start_number [::-1]: #La notation [::-1] est utilisée pour inverser une séquence en Python (demandé à chat gpt)
        dec_number += int(digit)*2**cpt
        cpt+=1
    print (dec_number)


