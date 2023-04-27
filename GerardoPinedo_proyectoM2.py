# LONGITUD DE UNA FRASE

while True:
    palabra = input("\nIngresa una palabra: ")
    longitud = len(palabra)

    if longitud >= 4 and longitud <= 8:
        print("\nPALABRA CORRECTA !!!\n")
        break
    elif longitud < 4:
        print(f"Hacen falta letras. La palabra {palabra} Solo tiene {longitud} letras.")
    else:
        print(f"Sobran letras. la palabra {palabra} Tiene {longitud} letras.")

print("\nPrograma terminado.\n")

# ENCUENTRA EL CUADRANTE

while True:
    x = float(input("\nIngrese el valor de la coordenada X: "))
    y = float(input("Ingrese el valor de la coordenada Y: "))

    if x == 0 or y == 0:
        print("\nLas coordenadas no pueden ser 0.")
    elif x > 0 and y > 0:
        print("\nEl punto se encuentra en el cuadrante I.")
    elif x < 0 and y > 0:
        print("\nEl punto se encuentra en el cuadrante II.")
    elif x < 0 and y < 0:
        print("\nEl punto se encuentra en el cuadrante III.")
    else:
        print("\nEl punto se encuentra en el cuadrante IV.")

    continuar = input("\n¿Desea ingresar otras coordenadas? (S/N): ")
    if continuar.upper() != "S":
        break


