# Fet per Daniel Paul Ivan.
# Also known as ysuyzuysu.

# Funcio que demana l'edat de l'usuari i diu si es major o menor d'edat:

def edat_usuari():
    edad = input("Quina edat tens (Numeró): ")

    if int(edad) >= 18:
        print("Ets major d'edat.")

    elif int(edad) < 18:
        print("Ets menor d'edat.")

edat_usuari()