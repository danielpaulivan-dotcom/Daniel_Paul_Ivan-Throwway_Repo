# Fet per Daniel Paul Ivan.
# Also known as ysuyzuysu.

# Usuari te que introduir dos nombres NO ENTERS i els convertim en float:

def numero_float():
    primer_numero = float(input("Introdueix el primer numero no enter: "))
    segon_numero = float(input("Introdueix el segon numero no enter:"))
    return primer_numero, segon_numero

primer_numero, segon_numero = numero_float()

# Sumem els dos números i imprimim el resultat:
resultat = int(primer_numero) + int(segon_numero)

print(resultat)

numero_float()