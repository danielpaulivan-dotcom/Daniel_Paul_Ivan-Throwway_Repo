# Fet per Daniel Paul Ivan.
# Also known as ysuyzuysu.

# Funcio que demana dos numeros float, els converteix a enters i mostra la seva suma:

def numero_float_fun():
    primer_numero = float(input("Introdueix el primer numero no enter: "))
    segon_numero = float(input("Introdueix el segon numero no enter:"))

    resultat = int(primer_numero) + int(segon_numero)

    print(resultat)

numero_float_fun()