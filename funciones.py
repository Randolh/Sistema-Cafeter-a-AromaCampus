from json import dumps, load, JSONDecodeError

archivo_productos = "coffee.json"


def leer_json(archivito):
    respuesta = {}
    try:
        with open(archivito, "r")as archivo:
            respuesta = load(archivo)
            return respuesta
    except FileNotFoundError:
        print("Archivo no encontrado, se creará uno nuevo al guardar el primer producto.")
        return respuesta
    except JSONDecodeError:
        print("Archivo vacío o con formato incorrecto, se creará uno nuevo al guardar el primer producto.")
        return respuesta
    
def escribir_json(archivito, contenido):
    with open(archivito, "w")as archivo:
        guardar = dumps(contenido, indent=4)
        

def agregar_coffee():
    
    while True:
        datos = leer_json(archivo_productos)
        nombre_producto = input("Ingrese el nombre del café: ").strip().title()

        if nombre_producto == "":
            print("Ingrese un nombre válido, no puede dejar espacios vacíos")
            continue

        if nombre_producto in datos:
            print("El producto ya existe en el inventario")
            continue
            


        while True:
            try:
                precio = int(input("Ingrese el precio por unidad del producto: "))
                cantidad = int(input("Ingrese la cantidad de productos en stock: "))
                break
            except:
                print("Ingrese una cantidad valida")
                continue
                
        
        while True:
            datos = leer_json(archivo_productos)
            descripcion = input("Ingrese la descripción del café a agregar ").strip()

            if descripcion == "":
                print("Ingrese un nombre válido, no puede dejar espacios vacíos")
                continue

            if descripcion in datos:
                print("El producto ya existe en el inventario")
                continue

            datos[nombre_producto]["Descripcion"] = descripcion
            print("Cantidad agregada correctamente")
        
            disponiblidad = True



            datos [nombre_producto] = {

                "Precio" : precio,
                "Cantidad": cantidad,
                "Disponibilidad": disponiblidad,
                "Descripcion":
            }

            escribir_json(archivo_productos, datos)
            break



agregar_coffee()