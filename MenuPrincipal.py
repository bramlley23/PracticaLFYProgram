from VentanaEmergente import *
def menuPrincipal():

	print("\n")
	print("\t\t\t\t\t=========================================")
	print("\t\t\t\t\t=                                       =")
	print("\t\t\t\t\t=  BIENVENIDO A MENU PRINCIPAL          =")
	print("\t\t\t\t\t=                                       =")
	print("\t\t\t\t\t=========================================")

	while True:


		print("\t\t\t\t\t1. Modulo AFD")
		print("\t\t\t\t\t2. Modulo GR")
		print("\t\t\t\t\t3. Acerca de")
		print("\t\t\t\t\t4. Salir")

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
				print("\t\t\t\t\t==========================================")
				print("\t\t\t\t\t=    Has salido del programa principal   =")
				print("\t\t\t\t\t==========================================")
				break
menuPrincipal()
