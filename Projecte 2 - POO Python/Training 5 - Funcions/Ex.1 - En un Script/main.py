# Training 1 - Ex.1
def hola_mon():
    print("Hola món")

hola_mon()

# Training 2 - Ex.1
def calcular_area_quadrat():
    mida_lateral = input("Introdueix la mida lateral: ")

    print(f"{int(mida_lateral)**2} és la mida del area del quadrat")

calcular_area_quadrat()

# Training 2 - Ex.2
def calculadora():
    primer_numero = input("Introdueix el primer número: ")
    segon_numero = input("Introdueix el segon número: ")

    primer_numero = int(primer_numero)
    segon_numero = int(segon_numero)

    print("")
    print(f"La suma dels dos números: {primer_numero + segon_numero}")
    print(f"La resta dels dos números: {primer_numero - segon_numero}")
    print(f"La multiplicació dels dos números: {primer_numero * segon_numero}")
    print(f"La divisió dels dos números: {primer_numero / segon_numero}")
    

calculadora()

# Training 2 - Ex.3
def joc_de_paraules():
    primera_paraula = input("Introdueix un nom: ")
    segona_paraula = input("Introdueix un adejectiu : ")
    tercera_paraula = input("Introdueix un altre adjectiu: ")

    print("Has introduït les paraules:", primera_paraula, segona_paraula, tercera_paraula)
    print(f"{primera_paraula} és un politic español {segona_paraula} y participa en un partit politic {tercera_paraula}.")

joc_de_paraules()

# Training 2 - Ex.4
def numero_float_fun():
    primer_numero = float(input("Introdueix el primer numero no enter: "))
    segon_numero = float(input("Introdueix el segon numero no enter:"))

    resultat = int(primer_numero) + int(segon_numero)

    print(resultat)

numero_float_fun()

# Training 3 - Ex.1
def edat_usuari():
    edad = input("Quina edat tens (Numeró): ")

    if int(edad) >= 18:
        print("Ets major d'edat.")

    elif int(edad) < 18:
        print("Ets menor d'edat.")

edat_usuari()

# Training 3 - Ex.2
def quin_es_major():
    primer_numero = input("Escriu el primer número: ")
    segon_numero = input("Escriu el segon número: ")
    tercer_numero = input("Escriu el trecer número: ")
                   
    if int(primer_numero) >= int(segon_numero) and int(primer_numero) >= int(tercer_numero):
        print("El primer número és el més gran.")  
    elif int(segon_numero) >= int(primer_numero) and int(segon_numero) >= int(tercer_numero):
        print("El segon número és el més gran.")
    elif int(tercer_numero) >= int(primer_numero) and int(tercer_numero) >= int(segon_numero):
        print("El tercer número és el més gran.")

quin_es_major()

# Training 3 - Ex.3
def positiu_o_no():
    numero = input("Escriu un número: ")

    if int(numero) >= 0:
        print("El número és positiu.")
    elif int(numero) < 0:
        print("El número és negatiu.")

positiu_o_no()

# Training 4 - Ex.1
def nombres_parells():
    for nombre in range(1, 201):
        if nombre / 2 == 0:
            print(nombre)  
        else:
            continue 
    
nombres_parells()

# Training 4 - Ex.2
def hi_ha_un_deu():
    hi_ha_deu = False

    for i in range(100):  # Limitem a 100 iteracions per evitar bucles infinits en cas d'error.
        nota = float(input("Introdueix una nota (0-10) o -1 per finalitzar: "))
        
        if nota == -1:
            break
        
        if nota == 10:
            hi_ha_deu = True
            print("Hi ha hagut alguna nota que té un 10")
            break
        
        if 0 <= nota < 10:
            print("No hi ha cap 10")

hi_ha_un_deu()

# Training 4 - Ex.3
def hi_ha_nombre_negatiu():
    hi_ha_negatiu = False

    for _ in range(10):
        nombre = float(input("Introdueix un nombre: "))
        if nombre < 0:
            hi_ha_negatiu = True

    if hi_ha_negatiu:
        print("Hi havia almenys un nombre negatiu")
    else:
        print("No hi ha cap nombre negatiu")

hi_ha_nombre_negatiu()
