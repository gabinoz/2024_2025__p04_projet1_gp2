# from data import hexa
# def hexa_to_dec (start_number, init_base, target_base) :
#     final_number = 0
#     for nb in start_number :
#         if nb in hexa :
#             if nb == hexa[0] or nb == hexa [1] :
#                 nb1 = 10
#             elif nb == hexa [ 2, 3 ] :
#                 nb1 = 11
#             elif nb == hexa [ 4, 5] :
#                 nb1 = 12
#             elif nb == hexa [ 6, 7] :
#                 nb1 = 13
#             elif nb == hexa [ 8, 9] :
#                 nb1 = 14
#             elif nb == hexa [ 10, 11] :
#                 nb1 = 15
#         elif nb not in hexa :
#             nb1 = int (nb)
#         final_number = nb1 * 16**
# # assert hexa_to_dec ('23A', 16, 10) == 570
# #(23A)₁₆ = (2 × 16²) + (3 × 16¹)+ (10 × 16**0)
# #  assert hexa_to_dec ('2' , 16, 10) == 2 16⁰) = (570)₁₀ 

def hex_to_dec(hex_num):
    # cette fonction est gé&nérée par Chatgpt pour aider à comprendre sur le fonctionnement
    # Définir les valeurs des chiffres hexadécimaux
    hex_values = {
        '0': 0, '1': 1, '2': 2, '3': 3,
        '4': 4, '5': 5, '6': 6, '7': 7,
        '8': 8, '9': 9, 'A': 10, 'B': 11,
        'C': 12, 'D': 13, 'E': 14, 'F': 15
    }
    
    decimal_value = 0
    hex_num = hex_num.upper()  # Convertir en majuscules pour traiter A-F

    # Parcourir le nombre hexadécimal de droite à gauche
    for i, digit in enumerate(reversed(hex_num)):
        if digit in hex_values:
            decimal_value += hex_values[digit] * (16 ** i)
        else:
            raise ValueError(f"'{digit}' n'est pas un chiffre hexadécimal valide.")

    return decimal_value

# Exemple d'utilisation
hex_number = input("Entrez un nombre hexadécimal : ")
decimal_number = hex_to_dec(hex_number)
print(f"Le nombre décimal est : {decimal_number}")




def dec_to_hexa () : 
    pass