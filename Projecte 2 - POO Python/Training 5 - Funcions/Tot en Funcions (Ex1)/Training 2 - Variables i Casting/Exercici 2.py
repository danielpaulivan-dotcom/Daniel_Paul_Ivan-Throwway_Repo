# Fet per Daniel Paul Ivan.
# Also known as ysuyzuysu.

# Definim la funció per a demanar els números:

def obtenir_numeros():
    primer_numero = input("Introdueix el primer número: ")
    segon_numero = input("Introdueix el segon número: ")

    return primer_numero, segon_numero

# Cridem la funció i guardem els valors en variables:

primer_numero, segon_numero = obtenir_numeros()

primer_numero = int(primer_numero)
segon_numero = int(segon_numero)

# Variables per a imprir:

def calcular_operacions(primer_numero, segon_numero):
    suma = (primer_numero + segon_numero)
    resta = (primer_numero - segon_numero)
    multiplicacio = (primer_numero * segon_numero)
    divisio = (primer_numero / segon_numero)
    return suma, resta, multiplicacio, divisio

suma, resta, multiplicacio, divisio = calcular_operacions(primer_numero, segon_numero)

# Resultat:

print("")
print(f"La suma dels dos números: {suma}")
print(f"La resta dels dos números: {resta}")
print(f"La multiplicació dels dos números: {multiplicacio}")
print(f"La divisió dels dos números: {divisio}")

obtenir_numeros()