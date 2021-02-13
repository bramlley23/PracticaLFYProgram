from VentanaEmergente import *
def menuPrincipal():

	print("\n")
	print("\t\t\t\t\t=========================================")
	print("\t\t\t\t\t=                                       =")
	print("\t\t\t\t\t=  BIENVENIDO A MENU PRINCIPAL          =")
	print("\t\t\t\t\t=                                       =")
	print("\t\t\t\t\t=========================================")

	while True:


		print("\t\t\t\t\t1. Ventana Emergente")
		print("\t\t\t\t\t2. Mostrar Listas Ordenadas")
		print("\t\t\t\t\t3. Mostrar Lista de Busqueda")
		print("\t\t\t\t\t4. Mostrar Todas las Listas")
		print("\t\t\t\t\t5. Mostrar Listas en HTML")
		print("\t\t\t\t\t6. Salir")

		opcion=int(input("Ingrese una opcion"))

		if(opcion==1):
			print("==================================")
			print("uno")
			ventanaEmergente()

		elif(opcion==2):
			print("==================================")
			print("dos")


		elif(opcion==3):
			print("==================================")
			print("tres")

		elif(opcion==4):
			print("==================================")
			print("cuatro")

		elif(opcion==5):
			print("==================================")
			print("cinco")

		elif(opcion==6):
				print("\t\t\t\t\t==========================================")
				print("\t\t\t\t\t=    Carnet:        199919737            =")
				print("\t\t\t\t\t=    Nombres:   Williams Bramlley        =")
				print("\t\t\t\t\t=    Apellidos: Constanza Oscal          =")
				print("\t\t\t\t\t=    Correo:    bramlley23@gmail.com     =")
				print("\t\t\t\t\t==========================================")
				break
menuPrincipal()
