# Fet per Daniel Paul Ivan.
# Also known as ysuyzuysu.

# dEfinim la funció per a demanar les paraules:

def obtenir_paraules():
    primera_paraula = input("Introdueix un nom: ")
    segona_paraula = input("Introdueix un adejectiu : ")
    tercera_paraula = input("Introdueix un altre adjectiu: ")

    return primera_paraula, segona_paraula, tercera_paraula

    print("")
    print(f"{primera_paraula} és un politic español {segona_paraula} y participa en un partit politic {tercera_paraula}.")

obtenir_paraules()