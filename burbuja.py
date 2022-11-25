print("Bienvenid@, este es un algoritmo para ordenar un array (lista, para los panas), admite solo tipos de datos enteros y con decimales, adelante.")
print("   ")

salir = 2
while salir == 2:
    #inicio del programa
    lista = [] #lista vacia para ingresar los numeros del usuario
    numero = float(input("Introducir primer valor: "))
    print(" ")
    lista.append(numero) #agrega el numero al array
    
    #pregunta para volver agregar numero 
    print("¿Desea añadir otro Valor?")
    print("1. Si  2. No")
    op = float(input("Ingrese su opcion: ")) #variable de opcion para saber si ingrear otro o no
    print("   ")
    #bucle en caso de la respuesta ser si
    while op == 1:
            numero = float(input("introducir numero: "))
            print("  ") 
            lista.append(numero)
            op = 0
            print("¿Desea añadir otro?")
            print("1. Si 2. No")
            op = int(input("Ingrese su opcion: "))
            print("  ")
        
    print("  ")
    print("antes de ordenar: ")
    print(lista)

    def metodo(array):
        longitud = len(array) -1 #esto se usa para evitar error con el ultimo elemento
        for i in range(0, longitud): #para contar los intentos 
            print("  ")
            print(f"intento numero {i + 1}") 
            for j in range(0, longitud):  #para comparar los elementos 
                print("  ")
                print(f"comparando: {array[j]} > {array [j + 1]}")
                if array[j] > array [j + 1]: #si es mayor que el otro cambaira de posicion con esto
                    print(f"intercambiando: {array[j]} x {array[j + 1]} ")
                    #para poder cambiar de posicion 
                    aux = array[j] 
                    array[j] = array[j + 1]
                    array[j + 1] = aux
                    print(f"lista: {array}")

            print("  ")
            print(f"lista ordenada: {array}")
        return array

    (metodo(lista))
    print("  ")
    print("¿desea salir?")
    print("1. Si 2. No")
    salir = int(input("ingrese su opcion: "))
    print("  ")
    print("un cambio")

    #(metodo(lista))
