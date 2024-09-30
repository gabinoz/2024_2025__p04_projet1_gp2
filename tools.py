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














































































































def dec_to_bin (c) :
    v = []
    while c // 2 != 0 :
        v.append ( c%2 )
        c = c // 2
    v.append ( c%2 )
    w = []
    w.append 
    return w
print (dec_to_bin (11))
def dec_to_hex () :
    pass





def bin_to_hex (b) :
    b = bin_to_dec (b)
    b = dec_to_bin (b)
    return b

def hex_to_bin (a) :
    a = hex_to_dec(a)
    a = dec_to_bin(a)
    return a