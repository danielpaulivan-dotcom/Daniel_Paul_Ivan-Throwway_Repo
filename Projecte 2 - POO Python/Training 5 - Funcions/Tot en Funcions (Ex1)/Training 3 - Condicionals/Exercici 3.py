# Fet per Daniel Paul Ivan.
# Also known as ysuyzuysu.

# Definim la funció per a demanar un número:
def obtenir_paraules():
    numero = input("Escriu un número: ")
    return numero

# Cridem la funció i guardem el valor en una variable:
numero = obtenir_paraules()

# Condicionals per a saber si és positiu o negatiu.
if int(numero) >= 0:
    print("El número és positiu.")
elif int(numero) < 0:
    print("El número és negatiu.")

obtenir_paraules()