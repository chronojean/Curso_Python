def menu_principal():
    print("\n--- Menú Principal ---")
    print("1. Comprar Quesillo completo")
    print("2. Comprar Quesillo por porción")
    print("3. Ver menú de sabores")
    print("4. Cerrar el día.")


def menu_sabores():
    print("\n--- Menú de Quesillos ---")
    print("1. Quesillo Normal")
    print("2. Quesillo Parchita")
    print("3. Quesillo Piña")
    print("4. Quesillo Queso Crema")


precio_porcion = [5000, 6000, 6000, 8000]
precio_completo = [30000, 36000, 36000, 48000]

n_clientes = 0
ingresos_hoy = 0
opcion = 0
while (opcion != "4"):
    menu_principal()
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        n_clientes += 1

        menu_sabores()
        sabor = int(input("Seleccione el sabor del quesillo: "))
        print("Precio del quesillo completo: ", precio_completo[sabor-1])
        cantidad = int(input("Cuántos quesillos desea comprar? "))
        total_a_pagar = precio_completo[sabor-1] * cantidad

        ingresos_hoy = ingresos_hoy + total_a_pagar
        print("Total a pagar: ", total_a_pagar)
        input("Presione Enter para continuar...")

    elif opcion == "2":
    
        menu_sabores()
        sabor = input("Seleccione el sabor del quesillo: ")
        cantidad = int(input("Cuántas porciones desea comprar? "))
        
    elif opcion == "3":
        menu_sabores()

print("\n--- Resumen del día ---")
print("Número de clientes atendidos: ", n_clientes)
print("Ingresos totales del día: ", ingresos_hoy)
