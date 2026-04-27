from json import dumps, load, JSONDecodeError

archivo_productos = "productos.json"


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