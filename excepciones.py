while intentos < 5:
	valor = raw_input("Ingrese un número entero: ")
	try:
		valor = int(valor)
		return valor
	except ValueError:
		intentos += 1
		raise ValueError, "Valor incorrecto ingresado en 5 intentos"