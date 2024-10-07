def dec_to_bin (start_number, init_base, target_base) :
    restes = ""
    while start_number > 0:
        reste = start_number % 2    
        restes = str(reste) + restes  #.append (reste)
        start_number = start_number//2
    return restes

#test

    





            

