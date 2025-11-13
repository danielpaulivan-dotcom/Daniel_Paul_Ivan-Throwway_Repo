# Fet per Daniel Paul Ivan.
# Also known as ysuyzuysu.

# Hi ha algun nombre negatiu entre els 10 nombres introduïts pels usuaris?
hi_ha_negatiu = False

# Funció per a comprovar si hi ha algun nombre negatiu entre els 10 nombres introduïts:
def hi_ha_nombre_negatiu():
    # Declareu la variable com a global per poder modificar-la dins de la funció
    global hi_ha_negatiu
   
    for _ in range(10):
        nombre = float(input("Introdueix un nombre: "))
        if nombre < 0:
            hi_ha_negatiu = True

hi_ha_nombre_negatiu()

if hi_ha_negatiu:
    print("Hi havia almenys un nombre negatiu")
else:
    print("No hi ha cap nombre negatiu")

