def mostrar_menu():
    print("\nNOTAS DE ESTUDIANTES ")
    print("1. Agregar o actualizar estudiante")
    print("2. Mostrar todos los estudiantes y notas")
    print("3. Buscar estudiante")
    print("4. Eliminar estudiante")
    print("5. Salir")
def gestionar_notas():
    notas_estudiantes = {
        "Ana": 9.5,
        "Luis": 8.0,
        "Carlos": 9.0
    }
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-5): ")
        if opcion == "1":
            nombre = input("Ingresa el nombre del estudiante: ").strip()
            try:
                nota = float(input(f"Ingresa la nota de {nombre}: "))
                notas_estudiantes[nombre] = nota
                print(f"¡Estudiante '{nombre}' registrado/actualizado con éxito!")
            except ValueError:
                print("Error: Por favor, introduce un número válido para la nota.")   
        elif opcion == "2":
            if not notas_estudiantes:
                print("No hay registros en el sistema.")
            else:
                print("\nListado de estudiantes y notas:")
                for nombre, nota in notas_estudiantes.items():
                    print(f"- {nombre}: {nota}")         
        elif opcion == "3":
            nombre = input("Ingresa el nombre del estudiante a buscar: ").strip()
            if nombre in notas_estudiantes:
                print(f"Resultado: El estudiante {nombre} tiene una nota de {notas_estudiantes[nombre]}.")
            else:
                print(f"El estudiante '{nombre}' no se encuentra registrado.")   
        elif opcion == "4":
            nombre = input("Ingresa el nombre del estudiante a eliminar: ").strip()
            if nombre in notas_estudiantes:
                del notas_estudiantes[nombre]
                print(f"El estudiante '{nombre}' ha sido eliminado correctamente.")
            else:
                print(f"No se encontró al estudiante '{nombre}' para eliminar.")
        elif opcion == "5":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, elige un número del 1 al 5.")
if __name__ == "__main__":
    gestionar_notas()