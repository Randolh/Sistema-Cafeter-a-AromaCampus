from funciones import eliminar_producto, agregar_coffee

def main_menu():
    while True:
        print("""---- Cafetería AromaCampus ----\n
1. Agregar nuevo café
2. Editar información
3. Eliminar producto descontinuado
4. Salir
    """)

        opt = input("\nIngres la opción que desea realizar: ")

        if opt == "1":
            agregar_coffee()
        elif opt == "2":
            print("Editar")
        elif opt == "3":
            eliminar_producto()
        elif opt == "4":
            print("\nSaliendo del sistema...")
            break 
        else:
            input("Opción no disponible, presione (Enter) para continuar...")