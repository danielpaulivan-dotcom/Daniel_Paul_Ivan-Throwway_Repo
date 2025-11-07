# Exercici 2: Escriu un programa que llegeixi una seqüència de notes (valors de 0 a 10) i finalitzarà la seqüència amb el valor -1. Quan finalitzi ens ha d'indicar si "Hi ha hagut alguna nota que té un 10" o "No hi ha cap 10".

hi_ha_deu = False

for i in range(100):  # Limitem a 100 iteracions per evitar bucles infinits en cas d'error.
    nota = float(input("Introdueix una nota (0-10) o -1 per finalitzar: "))
    
    if 0 <= nota <= 10:
        if nota == -1:
            break
    
        if nota < 10:
            print("No hi ha cap 10")

        if nota == 10:
            hi_ha_deu = True
        
        if hi_ha_deu == True:
            print("Hi ha hagut alguna nota que té un 10")
            break
            
    
    