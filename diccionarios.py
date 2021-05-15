materias = {}
materias["lunes"] = [6103, 7540]
materias["martes"] = [6201]
materias["miércoles"] = [6103, 7540]
materias["jueves"] = []
materias["viernes"] = [6201]
print(materias.items())
print("--------------------------")
for dia, codigos in materias.items():
	print(dia, ":", codigos)