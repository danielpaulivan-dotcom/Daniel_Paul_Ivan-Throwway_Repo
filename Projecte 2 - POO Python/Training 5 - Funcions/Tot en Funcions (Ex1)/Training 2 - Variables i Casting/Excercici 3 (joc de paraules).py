# Fet per Daniel Paul Ivan.
# Also known as ysuyzuysu.

# Funcio que demana tres paraules i les utilitza en una frase:

def joc_de_paraules():
    primera_paraula = input("Introdueix un nom: ")
    segona_paraula = input("Introdueix un adejectiu : ")
    tercera_paraula = input("Introdueix un altre adjectiu: ")

    print("Has introduït les paraules:", primera_paraula, segona_paraula, tercera_paraula)
    print(f"{primera_paraula} és un politic español {segona_paraula} y participa en un partit politic {tercera_paraula}.")

joc_de_paraules()