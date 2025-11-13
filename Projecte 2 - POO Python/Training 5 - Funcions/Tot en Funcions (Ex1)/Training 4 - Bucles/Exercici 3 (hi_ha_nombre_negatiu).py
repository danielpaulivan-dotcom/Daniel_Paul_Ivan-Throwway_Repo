# Fet per Daniel Paul Ivan.
# Also known as ysuyzuysu.

# Funcio que comprova si hi ha algun nombre negatiu entre 10 nombres introduits per l'usuari.

def hi_ha_nombre_negatiu():
    hi_ha_negatiu = False

    for _ in range(10):
        nombre = float(input("Introdueix un nombre: "))
        if nombre < 0:
            hi_ha_negatiu = True

    if hi_ha_negatiu:
        print("Hi havia almenys un nombre negatiu")
    else:
        print("No hi ha cap nombre negatiu")

hi_ha_nombre_negatiu()

