# def dec_to_bin (start_number) :
#     restes = ""
#     while start_number > 0:
#         reste = start_number % 2    
#         restes = str(reste) + restes  #.append (reste)
#         start_number = start_number//2
#     return restes

# def dec_to_hex(start_number):
#     base_hex = [0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]
#     nb_hex_final = ""
#     while start_number > 0:
#         reste = start_number % 16
#         nb_hex = base_hex[reste]
#         nb_hex_final =  str(nb_hex) + nb_hex_final
#         start_number = start_number// 16
#     return nb_hex_final

# def bin_to_dec(start_number):
#     cpt = 0
#     nombre_en_decimal = 0
#     start_number = str(start_number)
#     for chiffres in start_number[::-1]:
#         nombre_en_decimal += int(chiffres) * 2** cpt
#         cpt += 1
#     print(nombre_en_decimal)

# bin_to_dec(1001)

def hex_to_dec(start_number):
     base_hex_nombres= [0,1,2,3,4,5,6,7,8,9,]
     base_hex_chiffres = ["A","B","C","D","E","F"]
     nombre_en_decimal = 0
     cpt = 0
     start_number = str(start_number)
     for chiffres in start_number[::1]:
         if chiffres in base_hex_nombres:
             nombre_en_decimal += int(chiffres) * 16 ** cpt
         else:
             indice = base_hex_chiffres.index(chiffres)  # Obtenir l'indice
             nombre_en_decimal += (10 + indice) * (16 ** cpt)
         cpt += 1

hex_to_dec("2A3F")
         
         
        






    





            

