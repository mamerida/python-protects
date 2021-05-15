def sumatoria(inicial, final, f):
"""
permite expresar una condición que ha de ser cierta siempre, ya que de no serlo se interrumpirá el programa. 
"""

	assert type(inicial) == int , " el numero inicial tiene que ser un entero"
	assert type(final) == int , " el numero final tiene que ser un entero"
	assert inicial < final , "el numero inicial debe ser mejor que el final"
	
	for i in range(inicial,final+1):
		f = f + i
	return print(f) 
	

