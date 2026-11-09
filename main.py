from registrar import insertar_sala, registrar_reserva
from consultar import consultar_salas, consultar_reservas
from cancelar import cancelar_reserva
from crear_tablas import crear_tablas


def menu():
    while True:
        print("\nMenu de registro y consultas.")
        print("1. Registrar sala")
        print("2. Consultar salas")
        print("3. Registrar reserva")
        print("4. Consultar reservas")
        print("5. Cancelar reserva")
        print("0. Salir")

        try:
            opcion = int(input("Ingrese una opcion del menu: "))
        except ValueError:
            print("La opcion ingresada no es valida.")
            continue

        if opcion == 1:
            try:
                nombre = input("Ingrese el nombre de la sala: ")
                capacidad = int(input("Ingrese la capacidad de la sala: "))
                insertar_sala(nombre, capacidad)
            except ValueError as error:
                print(error)

        elif opcion == 2:
            consultar_salas()

        elif opcion == 3:
            try:
                estudiante = input("Ingrese el nombre del estudiante: ")
                sala_id = int(input("Ingrese el ID de la sala: "))
                fecha = input("Ingrese la fecha de la reserva (AAAA-MM-DD): ")
                registrar_reserva(estudiante, sala_id, fecha)
            except ValueError as error:
                print(error)
            except Exception as error:
                print(f"Error: {error}")

        elif opcion == 4:
            consultar_reservas()

        elif opcion == 5:
            try:
                reserva_id = int(input("Ingrese el ID de la reserva a cancelar: "))
                cancelar_reserva(reserva_id)
            except ValueError as error:
                print(error)

        elif opcion == 0:
            print("Saliendo del sistema.")
            break

        else:
            print("Opcion no valida. Intente nuevamente.")


if __name__ == "__main__":
    crear_tablas()
    menu()