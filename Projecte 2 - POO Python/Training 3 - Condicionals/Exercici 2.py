# Fet per Daniel Paul Ivan.
# Also known as ysuyzuysu.

# Preguntem pels numerós individualment:

primer_numero = input("Escriu el primer número: ")
segon_numero = input("Escriu el segon número: ")
tercer_numero = input("Escriu el trecer número: ")

# Condicionals per a comparar-los                   
if int(primer_numero) >= int(segon_numero) and int(primer_numero) >= int(tercer_numero):
    print("El primer número és el més gran.")  
elif int(segon_numero) >= int(primer_numero) and int(segon_numero) >= int(tercer_numero):
    print("El segon número és el més gran.")
elif int(tercer_numero) >= int(primer_numero) and int(tercer_numero) >= int(segon_numero):
    print("El tercer número és el més gran.")
