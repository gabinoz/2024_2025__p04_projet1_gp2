# def dec_to_bin (start_number) :
#     restes = ""
#     while start_number > 0:
#         reste = start_number % 2    
#         restes = str(reste) + restes  #.append (reste)
#         start_number = start_number//2
#     return restes

def dec_to_hex(start_number):
    base_hex = [0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]
    nb_hex_final = ""
    while start_number > 0:
        reste = start_number % 16
        nb_hex = base_hex[reste]
        nb_hex_final =  str(nb_hex) + nb_hex_final
        start_number = start_number// 16
    return nb_hex_final





    





            
