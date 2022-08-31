
Age= []
def main():
    print("¡Hola! Elige una opción:\n\
             1. Crear Protocolo\n\
             2. Mostrar protocolo\n\
             3. Agregar un paso al final de la lista\n\
             4. Borrar algún paso\n\
             5. Salir")
while True:
    main()
    opc = int(input( "Elige una opcion para continuar (escribe el número): " ))    
    if opc == 1:
        num = int (input ("Escribe el número de pasos"))
        for _ in range(num):
            paso = input ("Escribe el protocolo: ")
    elif opc==2:
        print ("El protocolo es: "+ str (paso))
    elif opc == 3:
       paso = print("Escribe el nuevo paso: ")
    elif opc == 4:
        print(paso)
        bor= int(input ("Escribela posición del dato que deseas borrar(recuerda que la primera posición es 0): "))
        paso.pop(bor)
    elif opc == 5:
        print ("Hasta luego :]")
        break
else:
        print ("Esa opción no es válida")

