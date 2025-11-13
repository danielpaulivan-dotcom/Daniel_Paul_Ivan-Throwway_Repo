# Fet per Daniel Paul Ivan.
# Also known as ysuyzuysu.

# Funcio que demana un número i diu si és positiu o negatiu:

def positiu_o_no():
    numero = input("Escriu un número: ")

    if int(numero) >= 0:
        print("El número és positiu.")
    elif int(numero) < 0:
        print("El número és negatiu.")

positiu_o_no()