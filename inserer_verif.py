from data import *
def dec_to_bin (start_number) :
    restes = ""
    if verifier_decimal == f"L'utilisateur a dit que le nombre {start_number} est en base décimale. C'est vrai, on peut continuer le code.":
        print (verifier_decimal (start_number) )
        start_number = int (start_number)
        while start_number > 0:
            reste = start_number % 2    
            restes = str(reste) + restes  #.append (reste)
            start_number = start_number//2
        return restes
    else :
        return verifier_decimal
# print (dec_to_bin ('2'))
def dec_to_hex(start_number):
    base_hex = [0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]
    nb_hex_final = ""
    if verifier_decimal == f"L'utilisateur a dit que le nombre {start_number} est en base décimale. C'est vrai, on peut continuer le code.":
        print (verifier_decimal (start_number))
        start_number = int (start_number)
        while start_number > 0:
            reste = start_number % 16
            nb_hex = base_hex[reste]
            nb_hex_final =  str(nb_hex) + nb_hex_final
            start_number = start_number// 16
        return nb_hex_final
    else :
        return verifier_decimal
#print (dec_to_hex ('11'))

def bin_to_dec(start_number):
    cpt = 0
    nombre_en_decimal = 0
    if verifier_binaire == f"L'utilisateur dit que le nombre {start_number} est en base binaire. C'est vrai, on peut continuer le code." :
        print (verifier_binaire)
        for chiffres in start_number[::-1]:
            nombre_en_decimal += int(chiffres) * 2** cpt
            cpt += 1
        print(nombre_en_decimal)
    else :
        return verifier_binaire
# print (bin_to_dec ('10'))

def hex_to_dec(start_number):
     base_hex_chiffres = ["0","1","2","3","4","5","6","7","8","9","A","a","B","b","C","c","D","d","E","e","F","f"]
     nombre_en_decimal = 0
     cpt = 0
     for chiffres in start_number[::1]:
         if chiffres in base_hex_chiffres:
             nombre_en_decimal += int(chiffres) * 16 ** cpt
         else:
             indice = base_hex_chiffres.index(chiffres)  # Obtenir l'indice
             nombre_en_decimal += (10 + indice) * (16 ** cpt)
         cpt += 1

print (hex_to_dec ('1a'))