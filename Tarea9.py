def cinefacil():
    reservas = []
    funciones_disponibles = [
        {"pelicula": "Intensamente 2", "hora": "16:00"},
        {"pelicula": "Deadpool & Wolverine", "hora": "18:00"},
        {"pelicula": "Duna Parte 2", "hora": "20:00"},
    ]
    precio_boleto = 40

    def mostrar_funciones():
        print("\nFunciones disponibles:")
        for idx, funcion in enumerate(funciones_disponibles):
            print(f"{idx + 1}. {funcion['pelicula']} - {funcion['hora']}")

    def hacer_reserva():
        nombre = input("Ingrese su nombre: ").strip()
        mostrar_funciones()
        opcion = int(input("Seleccione el número de la función que desea: ")) - 1
        cantidad = int(input("¿Cuántos boletos desea comprar?: "))

        if 0 <= opcion < len(funciones_disponibles):
            funcion = funciones_disponibles[opcion]
            total = precio_boleto * cantidad
            reserva = {
                "cliente": nombre,
                "pelicula": funcion["pelicula"],
                "hora": funcion["hora"],
                "boletos": cantidad,
                "total": total
            }
            reservas.append(reserva)

            print("\nRESERVA EXITOSA")
            print(f"Cliente: {nombre}")
            print(f"Película: {funcion['pelicula']} - {funcion['hora']}")
            print(f"Boletos: {cantidad}")
            print(f"Total a pagar: Q{total:.2f}")
        else:
            print("Opción no válida.")

    def ver_reservas():
        if not reservas:
            print("\nNo hay reservas aún.")
        else:
            print("\nRESERVAS REALIZADAS:")
            for i, r in enumerate(reservas, 1):
                print(f"{i}. {r['cliente']} - {r['pelicula']} ({r['hora']}) - {r['boletos']} boletos - Q{r['total']}")

    while True:
        print("\nSISTEMA CINEFÁCIL")
        print("1. Hacer reserva")
        print("2. Ver reservas")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            hacer_reserva()
        elif opcion == "2":
            ver_reservas()
        elif opcion == "3":
            print("¡Gracias por usar CineFácil!")
            break
        else:
            print("Opción inválida.")

# Ejecutar programa
cinefacil()
