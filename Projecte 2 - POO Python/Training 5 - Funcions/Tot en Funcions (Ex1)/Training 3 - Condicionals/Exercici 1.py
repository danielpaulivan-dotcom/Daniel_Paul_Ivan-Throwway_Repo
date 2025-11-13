# Fet per Daniel Paul Ivan.
# Also known as ysuyzuysu.

# Primer demanem la edat de l'usuari:

def edat_usuari():
    edad = input("Quina edat tens (Numeró): ")
    return edad

# Cridem la funció i guardem el valor en una variable:
edad = edat_usuari()

# Condcionals per si es major o menor

if int(edad) >= 18:
    print("Ets major d'edat.")

elif int(edad) < 18:
    print("Ets menor d'edat.")

edat_usuari()