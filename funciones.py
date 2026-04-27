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
        archivo.write(guardar)

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

            tostado = ""

            while True:
                datos = leer_json(archivo_productos)
                opc = int(input("""Ingrese el nivel de tostado del cafe
                      
                      1. Bajo
                      2. Medio
                      3. Oscuro """))
                
                
                if opc == 1:
                    tostado = "Bajo"
                if opc == 2:
                    tostado = "Medio"
                if opc == 3:
                    tostado = "Oscuro"
                else:
                    print("""Has salido de "Agregar" """)
                    continue
                    
                disponiblidad = True


                datos[nombre_producto] = {

                    "precio" : precio,
                    "cantidad": cantidad,
                    "disponibilidad": disponiblidad,
                    "descripcion": descripcion,
                    "tostado": tostado
                }

                escribir_json(archivo_productos, datos)
                print("Has agregado tu café con Éxito")
                return


def eliminar_producto():
    while True:
        print("\n\n---- Eliminar Productos Descontinuados ----\n")
        productos = leer_json(archivo_productos)

        if not productos:
            print("No hay productos en el inventario.")
            return
        
        productos_sin_dispo = {nombre: valores for nombre, valores in productos.items() if not valores["disponibilidad"]}
        list_keys = [nombre for nombre, valores in productos.items() if not valores["disponibilidad"]]

        if len(productos_sin_dispo) == 0:
            print("No hay productos descontinuados para eliminar.")
            return
        
        for i, nombre in enumerate(productos_sin_dispo, start=1):
            caffe_p = productos[nombre]

            nombre = caffe_p["descripcion"]
            dispo = caffe_p["disponibilidad"]
            stock = caffe_p["stock"]

            print(f'{i}. {nombre} - Stock: {stock} | Disponibilidad: {"Si" if dispo else "No"}')

        opt = input("\nIngrese el el numero de producto que desea elimminar: ")

        try:
            opt = int(opt)
        except ValueError:
            print("\nSolo puedes ingresar numeros...")
            input("Presione (Enter) para continuar...")
            continue

        if opt <= 0 or opt > len(productos_sin_dispo):
            print("\nOpción no disponible!")
            input("Presione (Enter) para continuar...")
            continue

        valor_s = productos[list_keys[opt - 1]]["stock"]    

        if valor_s > 0:
            while True:
                eliminar = input(f"\nEl producto aun tiene stock de {valor_s}, deseas eliminarlo (s/n): ").strip()

                if eliminar == "s":
                    productos.pop(list_keys[opt - 1])

                    escribir_json(archivo_productos, productos)

                    print("\nProducto Eliminado Correctamente!")
                    input("Presione (Enter) para continuar...")
                    return
                elif eliminar == "n":
                    print("\nEliminación Cancelada!")
                    input("Presione (Enter) para continuar...")
                    return
                else:
                    print("\nOpción no disponible!")
                    input("Presione (Enter) para continuar...")
                    continue