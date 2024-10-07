def bin_to_dec (init_number):
    target_number = 0
    nbr_de_chiffres_du_nombre_binaire = len(init_number)

    for i in range(nbr_de_chiffres_du_nombre_binaire):
        target_number = target_number + int(init_number[i]) * (2 ** (nbr_de_chiffres_du_nombre_binaire - 1 - i))
    resultat = bin_to_dec(init_number)
    print (resultat)

bin_to_dec(10101)



