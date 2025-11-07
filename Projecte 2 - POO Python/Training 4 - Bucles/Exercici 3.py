hi_ha_negatiu = False

for _ in range(10):
    nombre = float(input("Introdueix un nombre: "))
    
    if nombre < 0:
        hi_ha_negatiu = True
if hi_ha_negatiu:
    print("Hi havia almenys un nombre negatiu")
else:
    print("No hi ha cap nombre negatiu")
