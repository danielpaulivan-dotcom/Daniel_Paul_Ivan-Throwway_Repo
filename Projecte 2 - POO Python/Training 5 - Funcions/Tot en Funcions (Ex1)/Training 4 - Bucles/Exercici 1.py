# Fet per Daniel Paul Ivan.
# Also known as ysuyzuysu.

# Funció per a imprimir els nombres parells de l'1 al 200:
def nombres_parells():
    for nombre in range(1, 201):
        if nombre / 2 == 0:
            print(nombre)  
        else:
            continue 