# Fet per Daniel Paul Ivan.
# Also known as ysuyzuysu.

# Funcio que fa operacions basiques amb dos numeros enters:

def calculadora():
    primer_numero = input("Introdueix el primer número: ")
    segon_numero = input("Introdueix el segon número: ")

    primer_numero = int(primer_numero)
    segon_numero = int(segon_numero)

    print("")
    print(f"La suma dels dos números: {primer_numero + segon_numero}")
    print(f"La resta dels dos números: {primer_numero - segon_numero}")
    print(f"La multiplicació dels dos números: {primer_numero * segon_numero}")
    print(f"La divisió dels dos números: {primer_numero / segon_numero}")
    

calculadora()