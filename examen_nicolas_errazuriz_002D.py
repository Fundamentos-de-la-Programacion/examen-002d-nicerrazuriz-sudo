

diccionario_prendas = {
"S001": ["Polera Basica", "polera", "M", "negro", "algodon", True],
"S002": ["Jeans Slim", "pantalon", "L", "azul", "denim", False],
"S003": ["Chaqueta Urban", "chaqueta", "M", "gris", "poliester", True],
"S004": ["Vestido Sol", "vestido", "S", "rojo", "lino", False],
"S005": ["Poleron Cozy", "poleron", "XL", "verde", "algodon", True],
"S006": ["Camisa Formal", "camisa", "M", "blanco", "algodon", False],
}

# cada uno representa respectivamente [7990, 12] 7990=precio y 12=unidades
diccionario_bodega = {
"S001": [7990, 12],
"S002": [19990, 0],
"S003": [29990, 3],
"S004": [24990, 6],
"S005": [17990, 8],
"S006": [14990, 2],
}


lista_opcion2= {

}

'''def unidades_categoria(categoria):
    #categoria= 
    print(categoria)'''

def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Unidades por categoría")
    print("2. Búsqueda de prendas por rango de precio")
    print("3. Actualizar precio de prenda")
    print("4. Agregar prenda")
    print("5. Eliminar prenda")
    print("6. Salir")
    print("=====================================")

def opcion1():
    categoria= input("Ingrese el nombre de la categoria: ").lower()
    contador_categoria=0
    contador_unidades_disponibles=0

    if categoria in diccionario_prendas["S001"]:
        contador_categoria+=1
        contador_unidades_disponibles+=diccionario_bodega["S001"][1]

    if categoria in diccionario_prendas["S002"]:
        contador_categoria+=1
        contador_unidades_disponibles+=diccionario_bodega["S002"][1]
    if categoria in diccionario_prendas["S003"]:
        contador_categoria+=1
        contador_unidades_disponibles+=diccionario_bodega["S003"][1]
    if categoria in diccionario_prendas["S004"]:
        contador_categoria+=1
        contador_unidades_disponibles+=diccionario_bodega["S004"][1]
    if categoria in diccionario_prendas["S005"]:
        contador_categoria+=1
        contador_unidades_disponibles+=diccionario_bodega["S005"][1]
    if categoria in diccionario_prendas["S006"]:
        contador_categoria+=1
        contador_unidades_disponibles+=diccionario_bodega["S006"][1]
    
    print(f"Hay {contador_unidades_disponibles} unidades de prendas con la categoria {categoria}")




def opcion2(p_min, p_max):
    if diccionario_bodega["S001"][0] in range(p_min, p_max+1) and diccionario_bodega["S001"][1]>0:
        lista_opcion2[diccionario_prendas["S001"][0]]=" - S001"
    if diccionario_bodega["S002"][0] in range(p_min, p_max+1) and diccionario_bodega["S002"][1]>0:
        lista_opcion2[diccionario_prendas["S002"][0]]=" - S002"
    if diccionario_bodega["S003"][0] in range(p_min, p_max+1) and diccionario_bodega["S003"][1]>0:
        lista_opcion2[diccionario_prendas["S003"][0]]=" - S003"
    if diccionario_bodega["S004"][0] in range(p_min, p_max+1) and diccionario_bodega["S004"][1]>0:
        lista_opcion2[diccionario_prendas["S004"][0]]=" - S004"
    if diccionario_bodega["S005"][0] in range(p_min, p_max+1) and diccionario_bodega["S005"][1]>0:
        lista_opcion2[diccionario_prendas["S005"][0]]=" - S005"
    if diccionario_bodega["S006"][0] in range(p_min, p_max+1) and diccionario_bodega["S006"][1]>0:
        lista_opcion2[diccionario_prendas["S006"][0]]=" - S006"

        print(lista_opcion2)
        


def buscar_codigo(codigo):
    if codigo in diccionario_bodega:
        return True
    else:
        return False
    



def opcion3(codigo_prenda_user, nuevo_precio):
    repetir= "s"
    while repetir=="s":
        buscar_codigo(codigo_prenda_user)
        if buscar_codigo==True:
            nuevo_precio= int(input("Ingrese el nuevo precio para la prenda: "))
            diccionario_bodega[codigo_prenda_user][0]= nuevo_precio
        else:
            print("Codigo de producto inexistente")
        repetir= input("Desea actualizar otro precio (s/n)? ")


def opcion4(codigo, nombre, categoria, talla, color, material, es_unisex, precio, unidades):
        if codigo not in diccionario_bodega or codigo in diccionario_prendas:
            diccionario_prendas[codigo]= [nombre, categoria, talla, color, material, es_unisex]
            diccionario_bodega[codigo]= [precio, unidades]
            print("Prenda agregada")
        elif codigo in diccionario_bodega or codigo in diccionario_prendas:
            print(f"Ya existe un producto con el codigo {codigo}, no se pudo realizar su solicitud")


def opcion5(codigo):
    codigo= input("Ingrese el codigo de la prenda que desea eliminar: ")
    if codigo in diccionario_bodega or codigo in diccionario_prendas:
        del diccionario_prendas[codigo]
        del diccionario_bodega[codigo]
        print("¡Eliminacion completada!")
    else:
        print(f"El producto asociado al codigo {codigo} no existe, no se pudo procesar su solicitud")



opcion=0
while opcion!=6:
    mostrar_menu()

    try:
        opcion= int(input("Ingrese una opcion del menu: "))
    except ValueError:
        print("Opcion no existente, intente de nuevo")
        continue


    if opcion==1:
        opcion1()

    elif opcion==2:
        try:
            p_min= int(input("Introduzca el precio minimo: "))
        except ValueError:
            print("Debe ingresar valores enteros")
            continue
        try:
            p_max= int(input("Introoduzca el precio maximo: "))
        except ValueError:
            print("Debe ingresar valores enteros")
            continue
        opcion2(p_min, p_max)

    elif opcion==3:
        codigo= input("Ingrese el codigo de la prenda a actualizar: ")
        nuevo_precio= 2
        opcion3(codigo, nuevo_precio)

    elif opcion==4:
        codigo= input("Ingrese el codigo de la nueva prenda: ")
        if codigo not in diccionario_bodega or codigo in diccionario_prendas:
            nombre= input("Ingrese el nombre de la nueva prenda: ")
            categoria= input("Ingrese la categoria de la nueva prenda: ")
            talla= input("Ingrese la talla de la nueva prenda: ")
            color= input("Ingrese el color de la nueva prenda: ")
            material= input("Ingrese el material de la nueva prenda: ")
            es_unisex= input("Ingrese si la nueva prenda es unisex (s/n): ")
            if es_unisex.lower()=="s":
                es_unisex= True
            elif es_unisex.lower()=="n":
                es_unisex= False
            precio= int(input("Ingrese el precio de la nueva prenda: "))
            unidades= int(input("Ingrese las unidades disponibles de la nueva prenda: "))
        opcion4(codigo, nombre, categoria, talla, color, material, es_unisex, precio, unidades)

    elif opcion==5:
        opcion5

    elif opcion==6:
        print("Gracias por usar el programa de administracion de catalogo de Style Shop")
        print("Programa Finalizado")
        break




