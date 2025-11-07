# Exercici 1: Realitza un programa que mostri tots els nombres parells que hi ha entre 1 i 200. 

for nombre in range(1, 201):
    if nombre / 2 == 0:
        print(nombre)  
    else:
        continue 