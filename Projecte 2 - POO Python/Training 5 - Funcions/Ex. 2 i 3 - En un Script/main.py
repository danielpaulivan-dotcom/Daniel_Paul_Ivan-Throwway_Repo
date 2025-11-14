# Fet per Daniel Paul Ivan
# Also known as ysuyzuysu.

# Training 1 - Ex.1
def hola_mon():
        print("Hola món")

# Training 2 - Ex.1
def calcular_area_quadrat():
    mida_lateral = input("Introdueix la mida lateral: ")

    print(f"{int(mida_lateral)**2} és la mida del area del quadrat")

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

# Training 2 - Ex.3
def joc_de_paraules():
    primera_paraula = input("Introdueix un nom: ")
    segona_paraula = input("Introdueix un adejectiu : ")
    tercera_paraula = input("Introdueix un altre adjectiu: ")

    print("Has introduït les paraules:", primera_paraula, segona_paraula, tercera_paraula)
    print(f"{primera_paraula} és un politic español {segona_paraula} y participa en un partit politic {tercera_paraula}.")

# Training 2 - Ex.4
def numero_float_fun():
    primer_numero = float(input("Introdueix el primer numero no enter: "))
    segon_numero = float(input("Introdueix el segon numero no enter:"))

    resultat = int(primer_numero) + int(segon_numero)

    print(resultat)


# Training 3 - Ex.1
def edat_usuari():
    edad = input("Quina edat tens (Numeró): ")

    if int(edad) >= 18:
        print("Ets major d'edat.")

    elif int(edad) < 18:
        print("Ets menor d'edat.")

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

# Training 3 - Ex.3
def positiu_o_no():
    numero = input("Escriu un número: ")

    if int(numero) >= 0:
        print("El número és positiu.")
    elif int(numero) < 0:
        print("El número és negatiu.")

# Training 4 - Ex.1
def nombres_parells():
    for nombre in range(1, 201):
        if nombre / 2 == 0:
            print(nombre)  
        else:
            continue 

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

import time

print("Benvingut al meu script que conté totes les solucions dels exercicis de les diferents sessions de training.")

time.sleep(5)

print("Quina opció vols executar?")
time.sleep(2)

while True:
    print("\n"
      "1. Training 1 - Ex.1\n"
      "2. Training 2 - Ex.1\n"
      "3. Training 2 - Ex.2\n"
      "4. Training 2 - Ex.3\n"
      "5. Training 2 - Ex.4\n"
      "6. Training 3 - Ex.1\n"
      "7. Training 3 - Ex.2\n"
      "8. Training 3 - Ex.3\n"
      "9. Training 4 - Ex.1\n"
      "10. Training 4 - Ex.2\n"
      "11. Training 4 - Ex.3\n"
      "\n"
      "12. (S)ortir"
      )
    
    time.sleep(0.5)
    opcio_training = input("Introdueix el número de l'opció que vols executar (o '12' o '(S)ortir per acabar): ")
# Training 1 - Ex.1

    match opcio_training:
        
            case "1":
                time.sleep(1)
                print("Executant Training 1 - Ex.1...")
                time.sleep(2)
                hola_mon()
                time.sleep(1)
        
            case "2":
                time.sleep(1)
                print("Executant Training 2 - Ex.1...")
                time.sleep(2)
                calcular_area_quadrat()
                time.sleep(1)
        
            case "3":
                time.sleep(1)
                print("Executant Training 2 - Ex.2...")
                time.sleep(2)
                calculadora()
                time.sleep(1)
        
            case "4":
                time.sleep(1)
                print("Executant Training 2 - Ex.3...")
                time.sleep(2)
                joc_de_paraules()
                time.sleep(1)
        
            case "5":
                time.sleep(1)
                print("Executant Training 2 - Ex.4...")
                time.sleep(2)
                numero_float_fun()
                time.sleep(1)
        
            case "6":
                time.sleep(1)
                print("Executant Training 3 - Ex.1...")
                time.sleep(2)
                edat_usuari()
                time.sleep(1)
        
            case "7":
                time.sleep(1)
                print("Executant Training 3 - Ex.2...")
                time.sleep(2)
                quin_es_major()
                time.sleep(1)
        
            case "8":
                time.sleep(1)
                print("Executant Training 3 - Ex.3...")
                time.sleep(2)
                positiu_o_no()
                time.sleep(1)
        
            case "9":
                time.sleep(1)
                print("Executant Training 4 - Ex.1...")
                time.sleep(2)
                nombres_parells()
                time.sleep(1)
        
            case "10":
                time.sleep(1)
                print("Executant Training 4 - Ex.2...")
                time.sleep(2)
                hi_ha_un_deu()
                time.sleep(1)
        
            case "11":
                time.sleep(1)
                print("Executant Training 4 - Ex.3...")
                time.sleep(2)
                hi_ha_nombre_negatiu()
                time.sleep(1)
    
            case "S" | "s" | "12":
                time.sleep(1)
                print("Adeu!")
                break
        
            case _:
                time.sleep(1)
                print("Opció no vàlida. Si us plau, intenta-ho de nou.")
                time.sleep(1)
