# Fet per Daniel Paul Ivan.
# Also known as ysuyzuysu.

# Definim la funció per a demanar els números:

def obtenir_numeros():
    primer_numero = input("Escriu el primer número: ")
    segon_numero = input("Escriu el segon número: ")
    tercer_numero = input("Escriu el trecer número: ")
    return primer_numero, segon_numero, tercer_numero

# Cridem la funció i guardem els valors en variables:
primer_numero, segon_numero, tercer_numero = obtenir_numeros()

# Condicionals per a comparar-los                   
if int(primer_numero) >= int(segon_numero) and int(primer_numero) >= int(tercer_numero):
    print("El primer número és el més gran.")  
elif int(segon_numero) >= int(primer_numero) and int(segon_numero) >= int(tercer_numero):
    print("El segon número és el més gran.")
elif int(tercer_numero) >= int(primer_numero) and int(tercer_numero) >= int(segon_numero):
    print("El tercer número és el més gran.")

obtenir_numeros()