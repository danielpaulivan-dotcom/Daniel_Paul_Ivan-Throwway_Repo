# Fet per Daniel Paul Ivan.
# Also known as ysuyzuysu.

# Primer demanem la mida lateral del quadrat:

def area_quadrat():
    mida_lateral = input("Introdueix la mida lateral: ")
    return mida_lateral

mida_lateral = area_quadrat()

# Convertim el la respota en un int i imprimim el resultat calculat.
# El f{string} ens ajuda a no utilitzar "+" cada vegada que volem ficar
# una variable en un string, apart, se veu millor :D.

print(f"{int(mida_lateral)**2} és la mida del area del quadrat")

area_quadrat()