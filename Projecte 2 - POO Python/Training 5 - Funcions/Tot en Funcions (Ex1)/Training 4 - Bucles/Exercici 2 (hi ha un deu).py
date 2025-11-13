# Fet per Daniel Paul Ivan.
# Also known as ysuyzuysu.

# Funcio que demana notes fins que l'usuari introdueix -1 i comprova si hi ha hagut algun 10:

def hi_ha_un_deu():
    hi_ha_deu = False

    for i in range(100):  # Limitem a 100 iteracions per evitar bucles infinits en cas d'error.
        nota = float(input("Introdueix una nota (0-10) o -1 per finalitzar: "))
        
        if nota == -1:
            break
        
        if nota == 10:
            hi_ha_deu = True
            print("Hi ha hagut alguna nota que té un 10")
            break
        
        if 0 <= nota < 10:
            print("No hi ha cap 10")

hi_ha_un_deu()
